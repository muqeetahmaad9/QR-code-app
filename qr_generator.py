import qrcode
import IPython.display as display
from PIL import Image

# Function to generate QR Code
def generate_qr(data, filename="qrcode_colab.png"):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    
    # Display QR Code in Google Colab
    display.display(img)
    print(f"✅ QR Code saved as {filename}")

# User Input for QR Code
data = input("Enter text or URL to generate QR Code: ")
generate_qr(data)
