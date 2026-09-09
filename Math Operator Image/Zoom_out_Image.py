import cv2
import numpy as np

filename = "Macaw.jpg"
img1 = cv2.imread(f"Dataset/Gambar Non Geometri/{filename}")

perbesaran = 1/16
seper_akar_skala = int(1/perbesaran**0.5)

if img1.shape[0]%seper_akar_skala > 1 or img1.shape[1]%seper_akar_skala > 1 :
    print("Jumlah Pixel Gambar Tidak Sesuai")
    exit()

if img1.shape[0]%seper_akar_skala == 0 :
    a =  int(img1.shape[0]/seper_akar_skala)
else :
    a =  img1.shape[0]//seper_akar_skala + 1
    
if img1.shape[1]%seper_akar_skala == 0 :
    b =  int(img1.shape[1]/seper_akar_skala)
else :
    b =  img1.shape[1]//seper_akar_skala + 1
    
img2 = np.zeros((a,b,3))

for i in range(a) :
    for j in range(b) :
        img2[i,j,:] = img1[i*seper_akar_skala,j*seper_akar_skala,:]
        
cv2.imwrite(f"Math Operator Image/Hasil/{perbesaran:.3f}x{filename}", img2)
print("Rampung")

