import cv2
import numpy as np
filename = "trapezoid_10.png"
img1 = cv2.imread(f'Dataset/Gambar Geometri/{filename}')

vektor_skala = [2, 2]

tinggi_baru = int(img1.shape[0] * vektor_skala[1])
lebar_baru = int(img1.shape[1] * vektor_skala[0])

img2 = np.zeros((tinggi_baru, lebar_baru, 3))

for i in range(img2.shape[0]) :
    for j in range(img2.shape[1]) :

        sumber_i = int(i / vektor_skala[1])
        sumber_j = int(j / vektor_skala[0])

        if img1.shape[0] > sumber_i and img1.shape[1] > sumber_j :
            img2[i,j,:] = img1[sumber_i,sumber_j,:]

cv2.imwrite(
    f"Transformasi Geometri Image/Hasil/Skala {vektor_skala} {filename}",
    img2
)

print("Rampung")

"""
    Batasan Batasan Program :

    1. Faktor skala harus bernilai lebih dari 0.

    2. Program menggunakan metode nearest neighbor,
       sehingga nilai piksel hasil diambil dari piksel
       terdekat pada citra asli.

    3. Program hanya melakukan perubahan ukuran citra
       dan tidak melakukan rotasi atau translasi.
"""