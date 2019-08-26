import cv2 
  
img = cv2.imread('rgb.png')  
height, width, depth = img.shape

for l in img:
    for c in l:
        (b,g,r) = c
        print(r, g, b)

