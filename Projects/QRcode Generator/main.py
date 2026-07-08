#QR code generator for a website
import qrcode
url = input("Enter a URL: ")

image = qrcode.make(url)
image.save("qr_code.png")

from IPython import display
display.Image("qr_code.png")
