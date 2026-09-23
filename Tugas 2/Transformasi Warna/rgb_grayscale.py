import cv2
import numpy as np
import matplotlib.pyplot as plt 

filename = "Dog.jpg"

img1 = cv2.imread(f"Dataset/Gambar Non Geometri/{filename}")

a = img1.shape[0]
b = img1.shape[1]

img2 = np.zeros((a, b), dtype=np.uint8)

for i in range(a):
    for j in range(b):

        B = int(img1[i,j,0])
        G = int(img1[i,j,1])
        R = int(img1[i,j,2])

        img2[i,j] = int(round(
            0.114 * B +
            0.587 * G +
            0.299 * R
        ))

cv2.imwrite(
    f"Transformasi Warna/Hasil/Grayscale_{filename}",
    img2
)

print("Selesai")

plt.imshow(img2, cmap="gray")
plt.title("Grayscale")
plt.axis("off")
plt.show()