# # # nama = ["kingfaiz", "kkkkk", "ajajaj", "jjjjj", "pepepep", "oaoaoaoa"]

# # # print("sebelum")
# # # print(nama[0])
# # # print("")
# # # print("sesudah")
# # # nama.insert(2, "kingfaiz")
# # # print(nama)

# # # nama[4]={"fufufafa"}
# # # print(nama)
# # # hapus = nama.pop(2)
# # # print(nama)
# # # print(hapus)

# # # print(nama[1:9:2])

# # #list mobil bahan bakar listrik
# # # bensin = ["avanza", "honda", "yamaha"]
# # # #list mobil listrik
# # # listrik = ["tesla", "SAIC"]
# # # #menggabungkan listrik dan bensin
# # # semua = bensin+listrik
# # # #menampilkan list semua
# # # print(bensin*3)

# # # data = ["farel", "celio", [["hai", 23,2.3]]]
# # # print(data[2][2][0][::-1])

# # # matkul = [1,2,3,4,[5,6,7,[8,9]]]
# # # print(matkul[4][4][::-1])
# # matkul = [1,2,3,[4,5,6][7,8,9]]

# # for i in matkul:
# #     for j in i:
# #         print(j)

# # nama = ('farrel', 'vito','shandy','rijal')
# # print(nama[1:])
# mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")

#CRUD
print( 
"""
===========================
|   DATA MAHASISWA A24    |
===========================
|    1. TAMBAH DATA       |           
|    2. TAMPILKAN DATA    |          
|    3. UBAH DATA         |     
|    4. HAPUS DATA        |      
|    5. KELUAR            |  
===========================
"""
)

data_mahasiswa = []
while True:
    pilih = int(input("PILIH : "))
    if pilih == 1:
        nama = input("NAMA : ")
        nim = input("NIM : ")
        kelas = input("KELAS : ")
        data_mahasiswa.append([nama,nim,kelas])
    elif pilih == 2:
        for i in range(len(data_mahasiswa)):
            print(f"\n Data Mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i][0]}\nNIM : {data_mahasiswa[i][1]}\nKELAS : {data_mahasiswa[i][2]}")
    elif pilih == 3:
        nama_lama = input("Nama Baru : ")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                nama_baru = input("NAMA : ")
                nim_baru = input("NIM : ")
                kelas_baru = input("KELAS : ")
                data_mahasiswa[i][0] = nama_baru
                data_mahasiswa[i][1] = nim_baru
                data_mahasiswa[i][2] = kelas_baru
    elif pilih == 4:
        nama_lama = input("Nama yang ingin dihapus")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                del data_mahasiswa[i]
    elif pilih == 5:
        print("Terima Kasih Telah Mengakses Data Mahasiswa")
        break
    else:
        print("Anda Salah Input")

