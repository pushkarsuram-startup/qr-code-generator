from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
from configurations import qr_code_to_url_mapping

app = FastAPI()

# Calculate the base project directory path from this file's location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Mount your static PDFs folder
app.mount("/static-documents", StaticFiles(directory=os.path.join(BASE_DIR, "documents")), name="documents")

# Configure the HTML template directory location
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


# The {qr_id} parameter captures "hooks_law_document" automatically from the browser URL
@app.get("/{qr_id}", response_class=HTMLResponse)
def serve_mapped_pdf(request: Request, qr_id: str):
    # Search the list for a dictionary where the 'id' matches the URL parameter
    matched_config = next(
        (item for item in qr_code_to_url_mapping if item['id'] == qr_id),
        None
    )

    # If the user types a random endpoint that doesn't exist, show a clean 404 error
    if not matched_config:
        raise HTTPException(status_code=404, detail="This document link does not exist.")

    # Build the path to the physical PDF asset
    pdf_web_url = f"/static-documents/{matched_config['pdf']}"

    # Format the file name into a clean webpage title heading
    clean_title = matched_config['pdf'].replace('_', ' ').replace('.pdf', '').title()

    return templates.TemplateResponse(
        "viewer.html",
        {
            "request": request,
            "pdf_url": pdf_web_url,
            "doc_title": clean_title
        }
    )
