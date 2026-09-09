import cv2
import numpy as np

filename = "trapezoid_10.png"

img1 = cv2.imread(f'Dataset/Gambar Geometri/{filename}')

img2 = np.zeros(img1.shape)

vektor_translasi = [50,0]

for i in range(img2.shape[0]) :
    for j in range(img2.shape[1]) :
        if img1.shape[1] > j - vektor_translasi[0] >= 0 and img1.shape[0] > i + vektor_translasi[1] >= 0 :
            img2[i,j,:] = img1[i + vektor_translasi[1],j - vektor_translasi[0],:]
        else :
            img2[i,j] = np.array([255,255,255])

cv2.imwrite(f"Transformasi Geometri Image/Hasil/Translasi {vektor_translasi} {filename}",img2)

print("Rampung")

""" 
    Batasan Batasan Program :
    1. -         
"""        
