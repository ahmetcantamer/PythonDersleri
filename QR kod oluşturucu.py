import segno
from PIL.ImageOps import scale

myqr = segno.make_qr("https://www.google.com.tr/?hl=tr")

myqr.save("QR kodu.png", scale = 15)