import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# ============================================================
# 1. PATH DATA
# ============================================================

path_chest = r"D:\Semester 5\Data Citra\Aritmatika\data\xray chest.png"
path_hand = r"D:\Semester 5\Data Citra\Aritmatika\data\xray tangan.png"
path_skull = r"D:\Semester 5\Data Citra\Aritmatika\data\xray skull.jpg"

# Folder untuk menyimpan hasil
output_dir = r"D:\Semester 5\Data Citra\Aritmatika\hasil"

# Membuat folder hasil jika belum ada
os.makedirs(output_dir, exist_ok=True)


# ============================================================
# 2. MEMBACA CITRA
# ============================================================

chest = cv2.imread(path_chest, cv2.IMREAD_GRAYSCALE)
hand = cv2.imread(path_hand, cv2.IMREAD_GRAYSCALE)
skull = cv2.imread(path_skull, cv2.IMREAD_GRAYSCALE)


# Cek apakah citra berhasil dibaca
if chest is None:
    raise FileNotFoundError("X-Ray Chest tidak ditemukan!")

if hand is None:
    raise FileNotFoundError("X-Ray Tangan tidak ditemukan!")

if skull is None:
    raise FileNotFoundError("X-Ray Skull tidak ditemukan!")


# ============================================================
# 3. FUNGSI OPERASI ARITMATIKA
# ============================================================

def penambahan(image, c):
    """
    g(x,y) = f(x,y) + c
    """
    result = image.astype(np.int16) + c
    return np.clip(result, 0, 255).astype(np.uint8)


def pengurangan(image, c):
    """
    g(x,y) = f(x,y) - c
    """
    result = image.astype(np.int16) - c
    return np.clip(result, 0, 255).astype(np.uint8)


def perkalian(image, c):
    """
    g(x,y) = f(x,y) × c
    """
    result = image.astype(np.float32) * c
    return np.clip(result, 0, 255).astype(np.uint8)


def pembagian(image, c):
    """
    g(x,y) = f(x,y) / c
    """
    result = image.astype(np.float32) / c
    return np.clip(result, 0, 255).astype(np.uint8)


# ============================================================
# 4. OPERASI ARITMATIKA
# ============================================================

# 1. Penambahan pada X-Ray Chest
chest_tambah = penambahan(chest, 150)

# 2. Pengurangan pada X-Ray Tangan
hand_kurang = pengurangan(hand, 150)

# 3. Perkalian pada X-Ray Skull
skull_kali = perkalian(skull, 2.0)

# 4. Pembagian pada X-Ray Skull
skull_bagi = pembagian(skull, 4.0)


# ============================================================
# 5. SIMPAN HASIL CITRA
# ============================================================

cv2.imwrite(
    os.path.join(output_dir, "chest_penambahan_150.png"),
    chest_tambah
)

cv2.imwrite(
    os.path.join(output_dir, "tangan_pengurangan_150.png"),
    hand_kurang
)

cv2.imwrite(
    os.path.join(output_dir, "skull_perkalian_2.png"),
    skull_kali
)

cv2.imwrite(
    os.path.join(output_dir, "skull_pembagian_4.png"),
    skull_bagi
)


# ============================================================
# 6. VISUALISASI HASIL
# ============================================================

plt.figure(figsize=(16, 9))

# -------------------------
# Chest +150
# -------------------------
plt.subplot(2, 4, 1)
plt.imshow(chest, cmap="gray")
plt.title("Chest - Original")
plt.axis("off")

plt.subplot(2, 4, 2)
plt.imshow(chest_tambah, cmap="gray")
plt.title("Penambahan +150")
plt.axis("off")


# -------------------------
# Tangan -150
# -------------------------
plt.subplot(2, 4, 3)
plt.imshow(hand, cmap="gray")
plt.title("Tangan - Original")
plt.axis("off")

plt.subplot(2, 4, 4)
plt.imshow(hand_kurang, cmap="gray")
plt.title("Pengurangan -150")
plt.axis("off")


# -------------------------
# Skull ×2
# -------------------------
plt.subplot(2, 4, 5)
plt.imshow(skull, cmap="gray")
plt.title("Skull - Original")
plt.axis("off")

plt.subplot(2, 4, 6)
plt.imshow(skull_kali, cmap="gray")
plt.title("Perkalian ×2")
plt.axis("off")


# -------------------------
# Chest ÷2
# -------------------------
plt.subplot(2, 4, 7)
plt.imshow(skull, cmap="gray")
plt.title("Skull - Original")
plt.axis("off")

plt.subplot(2, 4, 8)
plt.imshow(skull_bagi, cmap="gray")
plt.title("Pembagian ÷4")
plt.axis("off")


plt.tight_layout()

# Simpan visualisasi gabungan
plt.savefig(
    os.path.join(output_dir, "hasil_aritmatika.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# 7. INFORMASI HASIL
# ============================================================

print("=" * 60)
print("OPERASI ARITMATIKA CITRA SELESAI")
print("=" * 60)

print("\n1. Penambahan")
print("   Citra  : X-Ray Chest")
print("   Operasi: f(x,y) + 150")
print("   Hasil  : chest_penambahan_150.png")

print("\n2. Pengurangan")
print("   Citra  : X-Ray Tangan")
print("   Operasi: f(x,y) - 150")
print("   Hasil  : tangan_pengurangan_150.png")

print("\n3. Perkalian")
print("   Citra  : X-Ray Skull")
print("   Operasi: f(x,y) × 2")
print("   Hasil  : skull_perkalian_2.png")

print("\n4. Pembagian")
print("   Citra  : X-Ray Skull")
print("   Operasi: f(x,y) / 4")
print("   Hasil  : skull_pembagian_4.png")

print("\nSemua hasil tersimpan di:")
print(output_dir)