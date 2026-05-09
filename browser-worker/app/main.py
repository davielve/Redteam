from fastapi import FastAPI, HTTPException
import os
import logging
from .models import BrowseRequest, AuditResponse, ReportSaveRequest
from .storage import create_run_folder, save_json, REPORTS_DIR
from .explorer import run_audit

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Local AI App Red Team - Browser Worker")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/browse", response_model=AuditResponse)
async def browse(request: BrowseRequest):
    try:
        logger.info(f"Starting audit for {request.url}")
        run_id, run_path = create_run_folder()
        
        main_audit = await run_audit(request.url, run_id, run_path, request.is_mobile)
        
        response = AuditResponse(
            run_id=run_id,
            main_audit=main_audit
        )
        
        save_json(run_path, "raw_audit.json", response.model_dump())
        
        return response
    except Exception as e:
        logger.error(f"Audit failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/save-report")
async def save_report(request: ReportSaveRequest):
    try:
        logger.info(f"Saving report for run {request.run_id}")
        run_path = os.path.join(REPORTS_DIR, request.run_id)
        if not os.path.exists(run_path):
            raise HTTPException(status_code=404, detail="Run ID not found")
        
        report_path = os.path.join(run_path, request.filename)
        with open(report_path, "w") as f:
            f.write(request.report_markdown)
            
        return {"status": "success", "path": report_path}
    except Exception as e:
        logger.error(f"Failed to save report: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
