#QR code generator for a website
import qrcode
url="https://music.youtube.com/"
image = qrcode.make(url)
image.save("music_qr.jpeg")

from IPython import display
display.Image("music_qr.jpeg")
