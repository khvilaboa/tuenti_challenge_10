
import os
import sys
from PIL import Image

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

matplotlib.use("TkAgg")

data_path = os.path.join("data", os.path.splitext(os.path.basename(sys.argv[0]))[0])
tc_path = os.path.join(data_path, "index.png")

im = Image.open(tc_path)
pix = im.load()
width, height = im.size

colors = set()
colors_count = defaultdict(int)
for x in range(width):
    for y in range(height):
        colors.add(pix[x, y])
        colors_count[pix[y,x]] += 1

for c in colors:
    print(np.array(c) - np.array([255]*4))
    print(c)

color_codes = {v:k for k, v in enumerate(colors)}
m = []

def conv(p):
    def sp(v):
        if v == 252:
            return 0
        elif v == 253:
            return 80
        elif v == 254:
            return 160
        else:
            return 255

    return (sp(p[0]), sp(p[1]), sp(p[2]), 255)

for x in range(width):
    m.append([])
    for y in range(height):
        #m[-1].append(color_codes[pix[y, x]])
        #m[-1].append(0 if pix[y,x] else 100)
        if pix[y,x] != (252,252,252,255):
            pix[y,x] = conv(pix[y,x])

        #pix[y,x] = (0,0,0,0) if pix[y,x][0] == pix[y,x][1] == pix[y,x][2] else (255,255,255,255)

        """if pix[y,x][0] == pix[y,x][1] == pix[y,x][2]:
            pix[y, x] = (0,0,0,0)
        else:
            pix[y, x] = conv(pix[y, x])
"""
im.show()
print(colors_count)

"""plt.imshow(m)
plt.colorbar()
plt.savefig(os.path.join(data_path, "out.png"))
plt.show()"""