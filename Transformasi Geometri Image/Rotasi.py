import cv2
import numpy as np

def rotasi(img) :
    img_new = np.zeros((img.shape[1],img.shape[0],3))
    for i in range(img_new.shape[0]) :
        for j in range(img_new.shape[1]) :
            img_new[i,j,:] = img[j,img_new.shape[0]-1-i,:]
    return img_new

filename = "Dog.jpg"

img1 = cv2.imread(f'Dataset/Gambar Non Geometri/{filename}')

derajat = 270

if derajat % 90 != 0 :
    print("Sudut Perputaran Tidak Valid")

kuadran = int(derajat/90)

for i in range(kuadran%4) :
    img1 = rotasi(img1)

cv2.imwrite(f"Transformasi Geometri Image/Hasil/Rotasi {derajat} {filename}",img1)

print("Rampung")