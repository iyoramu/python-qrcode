import qrcode
from PIL import Image  # Only needed if you want to customize further

def generate_qr(data, filename="qrcode.png", fill_color="black", back_color="white", size=10, border=4):
    """
    Generate a QR code and save it as an image.
    
    Args:
        data (str): Text/URL to encode in the QR code.
        filename (str): Output file name (e.g., 'qrcode.png').
        fill_color (str): Color of the QR code (e.g., 'red', '#FF0000').
        back_color (str): Background color (e.g., 'white', '#FFFFFF').
        size (int): Pixel size per module (default: 10).
        border (int): Border size in modules (default: 4).
    """
    # Configure QR code
    qr = qrcode.QRCode(
        version=1,  # Controls size (1-40, higher = bigger)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # L/M/Q/H (7%/15%/25%/30%)
        box_size=size,
        border=border,
    )
    
    # Add data
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create and save image
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)
    print(f"QR code saved as '{filename}'")

# Example usage
if __name__ == "__main__":
    generate_qr(
        data="https://github.com",  # Text or URL
        filename="github_qr.png",
        fill_color="blue",
        back_color="white",
        size=12,
        border=2,
    )
