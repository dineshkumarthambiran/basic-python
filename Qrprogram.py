import qrcode

from pyzbar.pyzbar import decode
from PIL import Image

# encoding

# data = "hello world"

# image=qrcode.make(data)

# image.save("qr.png")

# decoding

img = Image.open("qr.png")

result = decode(img)

print(result)







