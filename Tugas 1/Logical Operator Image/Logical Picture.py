import cv2
import sys
import numpy as np
import pandas as pd
np.set_printoptions(threshold=sys.maxsize)

img1 = cv2.imread('trapezoid_1.png', cv2.IMREAD_GRAYSCALE)
img1 = (img1 == 255).astype(int) * 255
img2 = cv2.imread('trapezoid_10.png', cv2.IMREAD_GRAYSCALE)
img2 = (img2 == 255).astype(int) * 255

if (img1.shape != img2.shape) :
    print("Ukuran Gambar Berbeda")
    exit(0)
    
for i in range(img1.shape[0]) :
    for j in range(img1.shape[1]) :
        skip = False
        for k in range(3) :
            a = i -1 + k
            if a < 0 or a >= img1.shape[0] :
                continue
            for l in range(3) :
                b = j -1 + l
                if b < 0 or b >= img1.shape[1] or (a == b and a == 1) :
                    continue
                if img1[a][b] == 255 :
                    skip = True
                    break
            if skip :
                break
        if skip :
            continue
        else :
            img1[i][j] = 128
            
for i in range(img2.shape[0]) :
    for j in range(img2.shape[1]) :
        skip = False
        for k in range(3) :
            a = i -1 + k
            if a < 0 or a >= img2.shape[0] :
                continue
            for l in range(3) :
                b = j -1 + l
                if b < 0 or b >= img2.shape[1] or (a == b and a == 1) :
                    continue
                if img2[a][b] == 255 :
                    skip = True
                    break
            if skip :
                break
        if skip :
            continue
        else :
            img2[i][j] = 128
            
cv2.imwrite('Hasil/Gambar A.png', img1)
cv2.imwrite('Hasil/Gambar B.png', img2)
    
img3 = []
for i in range(img1.shape[0]) :
    p = []
    for j in range(img1.shape[1]) :
        if img1[i][j] == 0 or img2[i][j] == 0 :
            p.append(0)
        elif img1[i][j] == 128 or img2[i][j] == 128 :
            p.append(128)
        else :
            p.append(255)
    img3.append(p)
    
img3 = np.array(img3)

cv2.imwrite('Hasil/A Gabungan B.png', img3)

img3 = []
for i in range(img1.shape[0]) :
    p = []
    for j in range(img1.shape[1]) :
        if img1[i][j] == 0 or img2[i][j] == 0 :
            p.append(0)
        elif img1[i][j] == 128 and img2[i][j] == 128 :
            p.append(128)
        else :
            p.append(255)
    img3.append(p)
    
img3 = np.array(img3)

cv2.imwrite('Hasil/A Irisan B.png', img3)

img3 = []
for i in range(img1.shape[0]) :
    p = []
    for j in range(img1.shape[1]) :
        if img1[i][j] == 0 or img2[i][j] == 0 :
            p.append(0)
        elif img1[i][j] == 128 and img2[i][j] != 128 :
            p.append(128)
        else :
            p.append(255)
    img3.append(p)
    
img3 = np.array(img3)

cv2.imwrite('Hasil/A Irisan B Komplemen.png', img3)

img3 = []
for i in range(img1.shape[0]) :
    p = []
    for j in range(img1.shape[1]) :
        if img1[i][j] == 0 or img2[i][j] == 0 :
            p.append(0)
        elif img1[i][j] != 128 and img2[i][j] == 128 :
            p.append(128)
        else :
            p.append(255)
    img3.append(p)
    
img3 = np.array(img3)

cv2.imwrite('Hasil/A Komplemen Irisan B.png', img3)

img3 = []
for i in range(img1.shape[0]) :
    p = []
    for j in range(img1.shape[1]) :
        if img1[i][j] == 0 or img2[i][j] == 0 :
            p.append(0)
        elif not (img1[i][j] == 128 and img2[i][j] == 128) and (img1[i][j] == 128 or img2[i][j] == 128) :
            p.append(128)
        else :
            p.append(255)
    img3.append(p)
    
img3 = np.array(img3)

cv2.imwrite('Hasil/(A Irisan B) Komplemen Irisan (A Gabungan B).png', img3)

img3 = []
for i in range(img1.shape[0]) :
    p = []
    for j in range(img1.shape[1]) :
        if img1[i][j] == 0 or img2[i][j] == 0 :
            p.append(0)
        elif not (img1[i][j] == 128 or img2[i][j] == 128) or (img1[i][j] == 128 and img2[i][j] == 128) :
            p.append(128)
        else :
            p.append(255)
    img3.append(p)
    
img3 = np.array(img3)

cv2.imwrite('Hasil/(A Gabungan B) Komplemen Gabungan (A Irisan B).png', img3)

print("Rampung")