from PIL import Image
import dashie

colours = [(255, 255, 255)
         , (228, 228, 228)
         , (136, 136, 136)
         , (34, 34, 34)
         , (255, 167, 209)
         , (229, 0, 0)
         , (229, 149, 0)
         , (160, 106, 66)
         , (229, 217, 0)
         , (148, 224, 68)
         , (2, 190, 1)
         , (0, 211, 211)
         , (0, 131, 199)
         , (0, 0, 234)
         , (207, 110, 228)
         , (130, 0, 128)]

img = Image.new("RGB", (42, 69))
try:
    for y in range(69):
        for x in range(42):
            img.putpixel((x, y), colours[dashie.img[y][x]])
except:
    pass

img = img.resize((42*8, 69*8))
with open("dashie.png", "wb") as f:
    img.save(f, "PNG")



