# # daftar_buku = {
# # #key        #value
# # "Buku1" : "Harry Potter",
# # "Buku2" : "Percy Jackson",
# # "Buku3" : "Twillight"
# # }
# # print(daftar_buku["Buku1"])
# # print(daftar_buku["Buku2"])
# # print(daftar_buku["Buku3"])
# # print(daftar_buku)


# Biodata = {
# "Nama" : "Aldy Ramadhan Syahputra",
# "NIM" : 2109106079, #int
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" :True, #bool
# "Social Media" : {
#     "Instagram" : "@aldyrmdhns_",
#     "Discord" : "\'Izanami#6848"
#     }
# }

# # print(Biodata.get("Nama"))
# # print(Biodata.get("Alamat", "kosongbangg"))
# for i, j in Biodata.items():
#     print(Biodata[i])


# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = "FPS")
# print(games)

Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}

# print(Film)
# # del Film["The Conjuring"]
# # hapus = Film.pop("The Conjuring")
# Film.clear()
# print(Film)
# print(f"key yang di hapus = {hapus}")


# print(Film)
# Film["ZombieLand"] = "Comedy"


Biodata = {
"Nama" : "Aldy Ramadhan Syahputra",
"NIM" : 2109106079, #int
"KRS" : ["Program Web", "Struktur Data", "Basis Data"],
"Mahasiswa_Aktif" :True, #bool
"Social Media" : {
    "Instagram" : "@aldyrmdhns_",
    "Discord" : "\'Izanami#6848"
    }
}

print("jumlah dataaaa, =", len(Biodata))
pinjamdict = Biodata.copy()
print(pinjamdict)

key = "apel", "jeruk", "melon"
value = 1

buah = dict.fromkeys(key, value)
print(buah)

Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}
# for i in Film.values():
#     print(i, end="")

# print("Film :", Film.setdefault{"Oldbook", "Horror"})
# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }

# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
# for song in j:
#     print(song)
# print("")

mahasiswa = {
101 : {"Nama" : "Aldy", "Umur" : 19},
111 : {"Nama" : "Abdul", "Umur" : 18}
}

# for i, j in mahasiswa.items():
#     print("ID Mahasiswa : ", i)
# for i_a, j_a in j.items():
#     print (i_a, " : ", j_a)
# print("")

# for i, j in mahasiswa.items():
#     print(f"ID : {i}")
#     for keynested, valuenested in j.items():
#         print (f"{keynested} : {valuenested}")

# print(f" sebelum : {mahasiswa}")
# del mahasiswa [111]["Umur"]
# # mahasiswa[101]["angkatan"]=2023
# print(f"sesudah : {mahasiswa}")

Biodata = {}

while True:
    print("1. Tambah")
    print("2. Tampilakan")
    print("3. Exit")
    pilihan =  int(input("(1/2/3) : "))

    if pilihan == 1:
        nama = input("Masukkan nama :")
        umur = input("Masukkan umur :")
        alamat = input("Masukkan alamat :")

        Biodata[nama] = { 
            'Umur' : umur,
            'Alamat' : alamat
        }

    elif pilihan == 2:
        for nama, info in Biodata.items():
            print(f"Nama : {nama}")
            print(f"Umur : {info['Umur']}")
            print(f"Alamat : {info['Alamat']}")

    elif pilihan == 3:
        print("exit ...")
        break

    else:
        print("Invalid ... ... ")