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
R = np.zeros((a,b,3),dtype=np.uint8)
G = np.zeros((a,b,3),dtype=np.uint8)
B = np.zeros((a,b,3),dtype=np.uint8)

R[:,:,0] = img1[:, :, 0] 
G[:,:,1] = img1[:, :, 1]
B[:,:,2] = img1[:, :, 2]


plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img1)
plt.title("Gambar Asli")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(R)
plt.title("Red")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(G)
plt.title("Green")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(B)
plt.title("Blue")
plt.axis("off")

plt.show()