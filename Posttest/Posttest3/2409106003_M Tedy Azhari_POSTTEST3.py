#input height, weight, age
weight = float(input("Masukkan berat badan (gram): "))
height = float(input("Masukkan tinggi badan (km): "))
age = int(input("Masukkan usia (tahun): "))

#rumus BMR
bmr_pria = (0.01 * weight) + (625000 * height) - (5 * age) + 5
bmr_wanita = (0.01 * weight) + (625000 * height) - (5 * age) - 161

minimal = 1.25
sedang = 1.36
tinggi = 1.72

#Menentukan gender
print ("Terdapat dua opsi gender yaitu \n1 = pria\n2 = wanita")
gender = str(input("Masukkan jenis kelamin dengan angka: "))

#menentukan gender dan level aktivitas
print ("Terdapat tiga opsi pada level aktivitas yaitu angka\n1 = minimal(jarang bergerak)\n2 = sedang(olahraga 1-3 kali seminggu)\n3 = tinggi(olahraga 4-7 kali seminggu)")
activity = str(input("Masukkan level aktivitas dengan angka: "))

if gender == "1":
    if activity == "1":
        hasil = bmr_pria * minimal
    elif activity == "2":
        hasil = bmr_pria * sedang
    elif activity == "3":
        hasil = bmr_pria * tinggi
    else:
        print ("invalid")

elif gender == "2":
    if activity == "1":
        hasil = bmr_wanita * minimal
    elif activity == "2":
        hasil = bmr_wanita * sedang
    elif activity == "3":
        hasil = bmr_wanita * tinggi
    else:
        print ("invalid")
else:
    print("invalid")

print(f"(Kebutuhan Kalori Harian) Anda: {hasil:.2f} kalori/hari")
