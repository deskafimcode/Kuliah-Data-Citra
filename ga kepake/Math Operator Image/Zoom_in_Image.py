import cv2
import numpy as np

def interpolasi_bilinear (x,y,x1,y1,x2,y2,q11,q12,q21,q22) :
    var1 = (x2-x)/(x2-x1)*q11 + (x-x1)/(x2-x1)*q21
    var2 = (x2-x)/(x2-x1)*q12 + (x-x1)/(x2-x1)*q22
    return (y2-y)/(y2-y1)*var1 + (y-y1)/(y2-y1)*var2

filename = "Pantai.jpg"
img1 = cv2.imread(f"Dataset/Gambar Non Geometri/{filename}")

perbesaran = 4
akar_skala = int(perbesaran**0.5)

img2 = np.zeros((img1.shape[0]*akar_skala-(akar_skala-1),img1.shape[1]*akar_skala-(akar_skala-1),3))

for i in range(img1.shape[0]) :
    for j in range(img1.shape[1]) :
        img2[i*akar_skala,j*akar_skala,:] = img1[i,j,:]

for i in range(0,img2.shape[0]-akar_skala,akar_skala) :
    for j in range(0,img2.shape[1]-akar_skala,akar_skala) :
        for k in range(akar_skala+1) :
            for l in range(akar_skala+1) :
                if (k == 0 or k == akar_skala) and (l == 0 or l == akar_skala) :
                    continue
                x2 = j+akar_skala
                x1 = j
                y2 = i+akar_skala
                y1 = i
                x  = j+l
                y  = i+k
                img2[y,x,0] = interpolasi_bilinear(x,y,x1,y1,x2,y2,img2[y1,x1,0],img2[y1,x2,0],img2[y2,x1,0],img2[y2,x2,0])
                img2[y,x,1] = interpolasi_bilinear(x,y,x1,y1,x2,y2,img2[y1,x1,1],img2[y1,x2,1],img2[y2,x1,1],img2[y2,x2,1])
                img2[y,x,2] = interpolasi_bilinear(x,y,x1,y1,x2,y2,img2[y1,x1,2],img2[y1,x2,2],img2[y2,x1,2],img2[y2,x2,2])
                
cv2.imwrite(f"Math Operator Image/Hasil/{perbesaran}x{filename}", img2)
print("Rampung")

"""
    Batasan Batasan Program :
    1. Input perbesaran wajib bilangan kuadrat dan positif
    2. Program tidak menyediakan perbesaran < 1 (Ukuran Diperkecil)
"""