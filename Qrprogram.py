import qrcode

data = "hello world"

image=qrcode.make(data)

image.save("Myfiles\Downloads\qr.png")



