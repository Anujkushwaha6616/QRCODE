import qrcode
qr = qrcode.QRCode(version=1,box_size=10)
url = input("enter url to create a Qr code :")
qr.add_data(url)
qr.make()
img = qr.make_image(fill_color="yellow",back_color="black")
img.save("qrcode1.png")
print("make succesfully")
