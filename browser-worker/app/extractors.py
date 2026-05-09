from bs4 import BeautifulSoup

def extract_metadata(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    
    headings = [h.get_text().strip() for h in soup.find_all(['h1', 'h2', 'h3'])]
    
    important_elements = []
    # Capture buttons, links, and forms
    for tag in soup.find_all(['button', 'a', 'input', 'select']):
        # Filter out empty or invisible-like elements to keep token count sane
        text = tag.get_text().strip() or tag.get('placeholder', '') or tag.get('value', '')
        if not text and tag.name == 'a' and not tag.find('img'):
            continue
            
        important_elements.append({
            "tag": tag.name,
            "text": text[:100], # Truncate long text
            "id": tag.get('id'),
            "classes": " ".join(tag.get('class', [])),
            "attributes": {k: v for k, v in tag.attrs.items() if k not in ['class', 'id']}
        })
        
    return headings, important_elements
