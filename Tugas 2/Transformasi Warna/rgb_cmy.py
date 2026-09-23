import cv2
import numpy as np

filename = "Dog.jpg"

img1 = cv2.imread(f"Dataset/Gambar Non Geometri/{filename}")

a = img1.shape[0]
b = img1.shape[1]

img2 = np.zeros((a, b, 3), dtype=np.uint8)

for i in range(a):
    for j in range(b):

        B = int(img1[i,j,0])
        G = int(img1[i,j,1])
        R = int(img1[i,j,2])

        Rn = R / 255
        Gn = G / 255
        Bn = B / 255

        C = 1 - Rn
        M = 1 - Gn
        Y = 1 - Bn

        img2[i,j,0] = int(round(C * 255))
        img2[i,j,1] = int(round(M * 255))
        img2[i,j,2] = int(round(Y * 255))

cv2.imwrite(
    f"Transformasi Warna/Hasil/CMY_{filename}",
    img2
)

print("selesai")