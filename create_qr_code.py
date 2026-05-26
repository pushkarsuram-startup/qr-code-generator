from qrCodeGenerator import generate_custom_qr


if __name__ == "__main__":
    target_data = "https://onrender.com"

    # We use a double backslash "\\" at the end so Python treats it as a literal character
    # instead of escaping the closing quote block.
    generate_custom_qr(target_data, target_dir="data/qr_codes", filename="custom_qr.png")