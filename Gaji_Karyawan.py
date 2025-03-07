# Iputan Nama, Nik, Status (Pegawai Tetap/Honor), Golongan (A/B/C)
nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status Pegawai (Tetap/Honor): ").lower()
golongan = input("Masukkan Golongan (A/B/C): ").upper()

# Status Pegawai Tetap
if status == "tetap":
    if golongan == "A":
        gaji = 1000000
        bonus = 200000
    elif golongan == "B":
        gaji = 1000000
        bonus = 400000
    elif golongan == "C":
        gaji = 1000000
        bonus = 550000

# Status Pegawai Honor
elif status == "honor":
    if golongan == "A":
        gaji = 750000
        bonus = 150000
    elif golongan == "B":
        gaji = 750000
        bonus = 275000
    elif golongan == "C":
        gaji = 750000
        bonus = 480000
else:
    print("Status tidak valid")
    exit() # Keluar dari program

# Print Gaji, Bonus, dan Gaji Total
print("Nama: ", str(nama))
print("NIK: ", str(nik))
print("Status: ", str(status))
print("Golongan: ", str(golongan))
print("Gaji: ", int(gaji))
print("Bonus: ", int(bonus))
print("Gaji Total: ", int(gaji + bonus))