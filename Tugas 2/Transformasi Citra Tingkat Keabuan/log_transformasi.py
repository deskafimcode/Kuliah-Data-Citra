import cv2
import numpy as np

filename = "Dog.jpg"

img1 = cv2.imread(f"Dataset/Gambar Non Geometri/{filename}")

a = img1.shape[0]
b = img1.shape[1]

# Mengubah citra menjadi grayscale
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

# Menentukan konstanta c
c = 255 / np.log(1 + 255)

# Membuat citra hasil
img2 = np.zeros((a, b), dtype=np.uint8)

for i in range(a):
    for j in range(b):

        r = int(img_gray[i,j])

        s = c * np.log(1 + r)

        img2[i,j] = int(round(s))

cv2.imwrite(
    f"Transformasi Tingkat Keabuan/Hasil/Log_{filename}",
    img2
)

print("selesai")