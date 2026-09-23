import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

IMAGE_PATH = r"C:\D\Dokumen\Analisis Citra Data\Dataset\tanaman_warnawarni.jpg"
OUTPUT_DIR = r"C:\D\Dokumen\Analisis Citra Data\Tugas 2\Hasil"
filename = os.path.basename(IMAGE_PATH)
img1 = cv2.imread(IMAGE_PATH)
a, b, _ = img1.shape

# Simpan Hasil
# save_path_cmy = os.path.join(OUTPUT_DIR, f"CMY_{filename}")
# cv2.imwrite(save_path_cmy, img_cmy)
# print(f"Selesai! Disimpan ke: {save_path_cmy}")

# Display
C = np.zeros((a,b,3))
M = np.zeros((a,b,3))
Y = np.zeros((a,b,3))
C[:,:,1] = img1[:, :, 1] //2
C[:,:,2] = img1[:, :, 2] //2
M[:,:,0] = img1[:, :, 0] //2
M[:,:,2] = img1[:, :, 2] //2
Y[:,:,0] = img1[:, :, 0] //2
Y[:,:,1] = img1[:, :, 1] //2

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img1)
plt.title("Gambar Asli")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(C)
plt.title("Cyan (C)")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(M)
plt.title("Magenta (M)")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(Y)
plt.title("Yellow (Y)")
plt.axis("off")

plt.show()