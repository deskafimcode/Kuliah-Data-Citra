import cv2
import numpy as np

filename = "Dog.jpg"
img1 = cv2.imread(f"Dataset/Gambar Non Geometri/{filename}")
a = img1.shape[0]
b = img1.shape[1]
img2 = np.zeros((a,b))

for i in range(a) :
    for j in range(b) :
        img2[i,j] = int(round((int(img1[i,j,0]) + int(img1[i,j,1]) + int(img1[i,j,2])) /3 ))
        
cv2.imwrite(f"Binerisasi Image/Hasil/Grayscale_{filename}",img2)

maks = 0
min = 255

for i in range(a) :
    for j in range(b) :
        if img2[i,j] > maks :
            maks = img2[i,j]
        if img2[i,j] < min :
            min = img2[i,j]
            
mid = min + round((maks-min)/2)

img3 = np.zeros((a,b))

for i in range(a) :
    for j in range(b) :
        if img2[i,j] >= mid :
            img3[i,j] = 255
        else :
            img3[i,j] = 0
            
cv2.imwrite(f"Binerisasi Image/Hasil/Biner_{filename}",img3)

print("Rampung")