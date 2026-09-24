import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

IMAGE_PATH = r"C:\D\Dokumen\Analisis Citra Data\Dataset\tanaman_warnawarni.jpg"
OUTPUT_DIR = r"C:\D\Dokumen\Analisis Citra Data\Tugas 2\Hasil"
filename = os.path.basename(IMAGE_PATH)
img1 = cv2.imread(IMAGE_PATH)

a, b, _ = img1.shape
Y = np.zeros((a,b,3),np.int32)
Cr = np.zeros((a,b,3),np.int32)
Cb = np.zeros((a,b,3),np.int32)


for i in range(a):
    for j in range(b):
        R = int(img1[i, j, 0])
        G = int(img1[i, j, 1])
        B = int(img1[i, j, 2])

        Y[i,j,0] = round(0.299*R,0) + round(0.578*G,0) + round(0.114*B,0)
        Y[i,j,1] = round(0.299*R,0) + round(0.578*G,0) + round(0.114*B,0)
        Y[i,j,2] = round(0.299*R,0) + round(0.578*G,0) + round(0.114*B,0)
        Cr[i,j,0] = 128 + round(0.701*R,0) - round(0.587*G,0) - round(0.114*B,0)
        Cr[i,j,1] = 128 - round(0.357*R,0) + round(0.2989*G,0) + round(0.0581*B,0)
        Cr[i,j,2] = 128
        Cb[i,j,0] = 128 + round(0.0581*R,0) + round(0.114*G,0) - round(0.1721*B,0)
        Cb[i,j,1] = 128 + round(0.0581*R,0) + round(0.114*G,0) - round(0.1721*B,0)
        Cb[i,j,2] = 128 - round(0.299*R,0) - round(0.587*G,0) + round(0.886*B,0)

# Simpan Hasil
# save_path_cmy = os.path.join(OUTPUT_DIR, f"CMY_{filename}")
# cv2.imwrite(save_path_cmy, img_cmy)
# print(f"Selesai! Disimpan ke: {save_path_cmy}")

# Display

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img1)
plt.title("Gambar Asli")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(Y)
plt.title("Y")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(Cb)
plt.title("Cb")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(Cr)
plt.title("Cr")
plt.axis("off")

plt.show()