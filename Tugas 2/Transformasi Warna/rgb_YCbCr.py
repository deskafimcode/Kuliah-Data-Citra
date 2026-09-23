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

        Y = 0.299 * R + 0.587 * G + 0.114 * B

        Cb = -0.168736 * R - 0.331264 * G + 0.5 * B + 128

        Cr = 0.5 * R - 0.418688 * G - 0.081312 * B + 128

        img2[i,j,0] = np.clip(round(Y), 0, 255)
        img2[i,j,1] = np.clip(round(Cb), 0, 255)
        img2[i,j,2] = np.clip(round(Cr), 0, 255)

cv2.imwrite(
    f"Transformasi Warna/Hasil/YCbCr_{filename}",
    img2
)

print("selesai")

Y = img2[:,:,0]
Cb = img2[:,:,1]
Cr = img2[:,:,2]

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_YCrCb2RGB))
plt.title("Hasil YCbCr")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(Y, cmap="gray")
plt.title("Y (Luminance)")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(Cb, cmap="gray")
plt.title("Cb")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(Cr, cmap="gray")
plt.title("Cr")
plt.axis("off")

plt.show()