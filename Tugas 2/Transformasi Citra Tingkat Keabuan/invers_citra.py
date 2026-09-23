import cv2
import numpy as np

filename = "Dog.jpg"

img1 = cv2.imread(f"Dataset/Gambar Non Geometri/{filename}")

a = img1.shape[0]
b = img1.shape[1]

# Mengubah citra RGB menjadi grayscale
img_gray = np.zeros((a, b), dtype=np.uint8)

for i in range(a):
    for j in range(b):

        B = int(img1[i,j,0])
        G = int(img1[i,j,1])
        R = int(img1[i,j,2])

        img_gray[i,j] = int(round(
            0.114 * B +
            0.587 * G +
            0.299 * R
        ))

# Membuat citra hasil invers
img2 = np.zeros((a, b), dtype=np.uint8)

for i in range(a):
    for j in range(b):

        r = int(img_gray[i,j])

        img2[i,j] = 255 - r

cv2.imwrite(
    f"Transformasi Tingkat Keabuan/Hasil/Invers_{filename}",
    img2
)

print("selesai")