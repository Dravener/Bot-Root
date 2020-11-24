from PIL import Image

img = Image.open('images/0--page_img.png')
img = img.resize((1000, 1000))
img.show()
size = w, h = img.size

data = img.load()

pieces = []

for x in range(w):
    for y in range(h):
        hex_color = '#' + ''.join([ hex(it)[2:].zfill(2).upper() for it in data[x, y]])
        pieces.append((x, y, hex_color))

print(pieces)
