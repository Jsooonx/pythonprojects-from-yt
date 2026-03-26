import qrcode
import os

data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename: (without extension such as jpg) ").strip()

output_dir = "qr-code-output"
os.makedirs(output_dir, exist_ok=True)

filepath = os.path.join(output_dir, f"{filename}.png")

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filepath)
print(f"QR code saved as {filepath}")