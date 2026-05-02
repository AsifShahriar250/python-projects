import qrcode

data = input("Enter text or url: ").strip()
fileName = input("Enter the fileName: ").strip()

qr =qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)

image =qr.make_image(fill_color ="black", back_color ='white')
image.save(fileName)

print(f'QR code saved as {fileName}')





