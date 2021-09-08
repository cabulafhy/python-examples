from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter


img = Image.open('./wings.jpg')

img = ImageOps.autocontrast(img)
img = ImageOps.equalize(img)
img = img.filter(ImageFilter.EDGE_ENHANCE)

img.thumbnail((843,512),Image.ANTIALIAS)

img = ImageOps.expand(img, border=1,fill=0)

img.save('wingsTreated.png')