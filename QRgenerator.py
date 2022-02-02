import qrcode
img = qrcode.make('Sheikh Sharique bin haque\nNFT King \n way to the Metaverse \n\t Follow me up!')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
