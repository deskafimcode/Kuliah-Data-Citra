import cv2
import numpy as np

filename = "Dog.jpg"

img1 = cv2.imread(f'Dataset/Gambar Non Geometri/{filename}')

img2 = np.zeros(img1.shape)

vertikal = False

horizontal = True

for i in range(img2.shape[0]) :
    for j in range(img2.shape[1]) :
        if vertikal :
            a = img2.shape[0] - 1 - i
        else :
            a = i
        if horizontal :
            b = img2.shape[1] - 1 - j
        else :
            b = j
        
        img2[i,j,:] = img1[a,b,:]

cv2.imwrite(f"Transformasi Geometri Image/Hasil/Refleksi V{vertikal} H{horizontal} {filename}",img2)

print("Rampung")

""" 
    Batasan Batasan Program :
    1. Hanya dapat refleksi terhadap sumbu-Y dan sumbu-X (Horizontal dan Vertikal), Tidak menerima input terhadap refleksi persamaan garis
"""