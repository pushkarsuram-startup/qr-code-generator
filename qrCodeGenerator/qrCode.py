import os
import qrcode
from configurations import BASE_DIR


def generate_custom_qr(data, target_dir="data/qr_codes/", filename="custom_qr.png"):
    # Normalize the path to handle mixed forward slashes and backslashes safely
    safe_dir = os.path.normpath(os.path.join(BASE_DIR, target_dir))

    # 1. Create the directory path if it does not exist
    if not os.path.exists(safe_dir):
        os.makedirs(safe_dir)
        print(f"Created directory: {safe_dir}")

    # 2. Combine the safe folder path and file name cleanly
    full_path = os.path.join(safe_dir, filename)

    # 3. Check if the exact file already exists in that folder
    if os.path.exists(full_path):
        print(
            f"'{full_path}' already exists! Skipping generation to keep the same code."
        )
        return

    # Configure the QR code properties
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Inject the data into the object
    qr.add_data(data)
    qr.make(fit=True)

    # Render the matrix with custom foreground and background colors
    img = qr.make_image(fill_color="navy", back_color="white")
    #
    # # 4. Save the file directly to the folder
    img.save(full_path)
    print(f"Custom QR code successfully saved to: '{full_path}'")


# Execute the function
if __name__ == "__main__":
    target_data = "https://onrender.com"

    # We use a double backslash "\\" at the end so Python treats it as a literal character
    # instead of escaping the closing quote block.
    generate_custom_qr(target_data, target_dir="data/qr_codes", filename="custom_qr.png")
