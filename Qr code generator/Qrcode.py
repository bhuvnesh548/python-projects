import qrcode as qr
data=input("enter the information here : \n")
qrc=qr.make(data)
qrc.save("QRCODE.png")
print("QR saved successfully")

