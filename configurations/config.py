from pathlib import Path


BASE_DIR = Path("/var/opt/qr-code-generator/")
qr_code_to_url_mapping = [
    {
        'url': 'http://127.0.0.1:8000/hooks_law_document',
        'id': 'hooks_law_document',
        'qr_image': 'hooks_law.png',       # The physical QR code file
        'pdf': 'hooks_law_lecture.pdf'      # The actual PDF shown on the webpage
    },
]
