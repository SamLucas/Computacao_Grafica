import cv2 
  
img = cv2.imread('rgb.png')  
height, width, depth = img.shape

for l in img:
    for c in l:
        
        (b,g,r) = c
        print(r, g, b)

        c[0] += 10
        c[1] += 10
        c[2] += 10

cv2.imwrite('resultado.png',img)   
cv2.imshow('rgb2.png',img)   
cv2.waitKey()
