import cv2
from google.colab import files
import numpy as np

# Upload QR Code Image
uploaded = files.upload()
file_name = list(uploaded.keys())[0]

# Function to scan QR Code from an image
def scan_qr_image(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)

    if data:
        print(f"✅ QR Code Data: {data}")
    else:
        print("⚠️ No QR Code detected!")

# Run Scanner on Uploaded Image
scan_qr_image(file_name)
