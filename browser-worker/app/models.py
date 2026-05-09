from pydantic import BaseModel
from typing import List, Optional, Dict

class BrowseRequest(BaseModel):
    url: str
    goal: Optional[str] = "Find UX friction and bugs"
    is_mobile: bool = False

class ElementInfo(BaseModel):
    tag: str
    text: str
    id: Optional[str]
    classes: Optional[str]
    attributes: Dict[str, str]

class PageAudit(BaseModel):
    url: str
    title: str
    screenshot_path: str
    console_logs: List[str]
    network_failures: List[str]
    important_elements: List[ElementInfo]
    headings: List[str]

class AuditResponse(BaseModel):
    run_id: str
    main_audit: PageAudit
    sub_pages: List[PageAudit] = []

class ReportSaveRequest(BaseModel):
    run_id: str
    report_markdown: str
    filename: Optional[str] = "audit_report.md"
