import qrcode

url = "https://www.instagram.com/iivan_rld/"

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save("instagram_qr.png")