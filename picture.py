from PIL import Image

image = Image.open("./moon.jpg")

print(image.filename)
print(image.format)
print(image.size)
print(image.height)
print(image.width)
print(image.mode)

outfile = "./moon.png"
image.save(outfile, "PNG")
with Image.open(outfile) as im:
    print("Image format: ", im.format)