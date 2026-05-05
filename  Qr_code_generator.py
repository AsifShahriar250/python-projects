# This Python code snippet is creating a QR code based on user input. Here's a breakdown of what each
# part does:
 
import qrcode

data = input("Enter text or url: ").strip()
fileName = input("Enter the fileName(like(a.jgp)): ").strip()

qr =qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)

image =qr.make_image(fill_color ="black", back_color ='white')
image.save(fileName)

print(f'QR code saved as {fileName}')





