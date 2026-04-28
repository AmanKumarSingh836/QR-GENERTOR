# We are going to use python library qrcode to convert url and other file to QR-CODE
import qrcode

url=input("Enter the link to convert into: ")
filename=input("Enter the name for qr code file")
filename=filename+".png"

image=qrcode.make(url)
image.save(filename)