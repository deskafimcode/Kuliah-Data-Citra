import cv2
import numpy as np
import matplotlib.pyplot as plt 

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
C = img2[:,:,0]
M = img2[:,:,1]
Y = img2[:,:,2]

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(img2)
plt.title("Hasil CMY")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(C, cmap="gray")
plt.title("Cyan (C)")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(M, cmap="gray")
plt.title("Magenta (M)")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(Y, cmap="gray")
plt.title("Yellow (Y)")
plt.axis("off")

plt.show()