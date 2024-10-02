ulang = 10
for i in range (ulang):
    print("perulangan ke-15"+ str(i))

simpan = [12, "udin petot", 14,5, True, 'A']


for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
        print()

jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 2
    jawab = input("Ulang lagi tidak? ")
print(f"Total perulangan: {hitung}")

hitung = 0
while True:
    hitung += 1
    ulang = input("Masih Ingin Mengulang? ")
    if ulang == "tidak" or ulang =="Tidak":
        break
print(f"Total Perulangan: {hitung}")

bilangan = 0  
while True:
    angka = int(input("Masukkan angka positif (atau angka negatif untuk berhenti): "))
    if angka < 0:
        break  
    total += angka 
print("Jumlah total angka positif:", bilangan)

