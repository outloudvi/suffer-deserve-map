import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

xaxis = 2000
yaxis = 198
sizex = 97

# https://i.redd.it/kqiydnscn70z.png
img = cv2.imread("./kqiydnscn70z.png")
xlen = img.shape[0]
ylen = img.shape[1]
print(img.shape)

def display(clip, size = 5, title="output"):
    RGB_im = cv2.cvtColor(clip, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(size,size))
    plt.imshow(RGB_im)
    plt.title(title)
    plt.show()
    
display(img, 20)

def giveImageAt(pos):
    xlb = pos[0]
    ylb = pos[1]
    return img[xlb-sizex:xlb, ylb:ylb+sizex]

for y in range(200, ylen - sizex, 100):
    for x in range(1999, sizex, -100):
        cv2.imwrite(os.path.join("res", f"s{int((x+1) / (-20) + 105)}_d{int(y / 20 - 5)}.jpg"), giveImageAt((x, y)))