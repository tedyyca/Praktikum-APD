#posttest2
nama = str(input("Masukkan nama lengkap:"))
nm = str(input("Masukkan nama panggilan:"))
tl = str(input("Masukkan tempat lahir:"))
tgl = str(input("Masukkan tanggal lahir:"))
nim = int(input("Masukkan NIM:"))
prodi = str(input("Masukkan Program Studi:"))
umur = int(input("Masukkan umur:"))
bb = float(input("Masukkan berat badan:"))
tb = float(input("Masukkan tinggi badan:"))

modulus_nim = nim % 6

print("Nama lengkap: ",nama)
print("Nama panggilan: ",nm)
print("Tempat lahir: ", tl)
print("Tanggal lahir: ",(tgl))
print("NIM: ", (nim))
print("NIM yang sudah dimodulus 6: ",(modulus_nim))
print("Program studi:",prodi)
print("Umur: ",(umur))
print("berat badan: ",(bb))
print("tinggi badan: ",(tb))


print(f"Assalamualaikum warahmatullahi wabarakatuh, Perkenalkan nama saya {nama}, Saya biasanya dipanggil {nm}, Saya lahir di {tl} pada tanggal {tgl}, NIM saya adalah {nim}, dan ini NIM saya setelah dimodulus dengan 6 yaitu {modulus_nim}, Saya berasal dari Program Studi {prodi}, Umur saya saat ini {umur}tahun, Berat badan saya {bb} dan tinggi badan saya {tb}, sekian perkenalan dari saya Wassalamualaikum warahmatullahi wabarakatuh")