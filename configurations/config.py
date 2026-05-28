from pathlib import Path


BASE_DIR = Path("/var/opt/qr-code-generator/")
qr_code_to_url_mapping = [
    {
        'url': 'https://qr-code-generator-x09s.onrender.com/hooks_law_document',
        'id': 'hooks_law_document',
        'qr_image': 'hooks_law.png',       # The physical QR code file
        'pdf': 'hooks_law_lecture.pdf'      # The actual PDF shown on the webpage
    },
]
