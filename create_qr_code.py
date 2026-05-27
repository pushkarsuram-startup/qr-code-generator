from qrCodeGenerator import generate_custom_qr
from configurations import qr_code_to_url_mapping


if __name__ == "__main__":
    for qr_config in qr_code_to_url_mapping:
        generate_custom_qr(qr_config['url'], target_dir="data/qr_codes", filename=qr_config['qr_image'])