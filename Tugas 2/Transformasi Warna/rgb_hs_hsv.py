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

        maks = max(Rn, Gn, Bn)
        minimum = min(Rn, Gn, Bn)

        delta = maks - minimum

        # Value
        V = maks

        # Saturation
        if maks == 0:
            S = 0
        else:
            S = delta / maks

        # Hue
        if delta == 0:
            H = 0

        elif maks == Rn:
            H = 60 * (((Gn - Bn) / delta) % 6)

        elif maks == Gn:
            H = 60 * (((Bn - Rn) / delta) + 2)

        else:
            H = 60 * (((Rn - Gn) / delta) + 4)

        img2[i,j,0] = int(H / 360 * 255)
        img2[i,j,1] = int(S * 255)
        img2[i,j,2] = int(V * 255)

cv2.imwrite(
    f"Transformasi Warna/Hasil/HSV_{filename}",
    img2
)

print("selesai")