# MANAJEMEN PENDATAAN RUMAH
import os #library standar
import json #file eksternal
from prettytable import PrettyTable #library eksternal


# Data utama untuk rumah dan akun
# Dictionary kosong untuk menyimpan data
data_rumah = {}
akun = {} 
sudah_login = False  #variabel boolean, menandakan apakah sudah login atau belum

# Fungsi pembersihan layar
# mengecek sistem apakah bernilai "nt"(windows) 
def bersihkan():
    os.system("cls" if os.name == "nt" else "clear") #"cls" untuk windows dan "clear" untuk (linux/macOS)
    print("\033c", end="") #membersihkan seluruh layar terminal

# Fungsi penyimpanan dan pemuatan data rumah dari file JSON
# menyimpan data dari variabel data rumah ke file JSON
def simpan_data(filename="data_rumah.json"):
    with open(filename, "w") as file:
        json.dump(data_rumah, file)
# memuat data dari file JSON ke variabel data rumah
def muat_data(filename="data_rumah.json"):
    global data_rumah
    if os.path.exists(filename): #jika file ada, baca data rumah dari file
        with open(filename, "r") as file:
            data_rumah = json.load(file)
    else:
        data_rumah = {} #jika file tidak ada, dictionary kong

# Fungsi penyimpanan dan pemuatan data akun dari file JSON
def simpan_akun(filename="data_akun.json"):
    with open(filename, "w") as file:
        json.dump(akun, file)

def muat_akun(filename="data_akun.json"):
    global akun
    if os.path.exists(filename): #jika file ada, baca data akun dari file
        with open(filename, "r") as file:
            akun = json.load(file)
    else:
        akun = {} #jika file tidak ada, dictionary kong
           
    return {"admin": {"password": "admin", "role": "admin"}} # 1 akun admin yang disiapkan

# Fungsi input integer dengan validasi (memastikan input hanya berupa angka)
def input_int(pesan):
    try:
        return int(input(pesan)) # mengembalikan input jika berupa angka.
    except ValueError:
        print("Input harus berupa angka.")
        return input_int(pesan) # rekursif jika input tidak valid.

# Fungsi validasi pilihan menu (memastikan pilihan menu berada dalam rentang valid.)
def validasi_pilihan_menu(pilihan, max_pilihan):
    try:
        if pilihan < 1 or pilihan > max_pilihan:
            raise ValueError("Pilihan tidak valid, coba lagi.")
        return pilihan
    except ValueError as e:
        print(e)
        return validasi_pilihan_menu(input_int("Masukkan pilihan: "), max_pilihan)

# Fungsi tampilan menu utama
def tampilkan_menu_utama():
    bersihkan() #membersihkan terminal ketika memilih menu keluar
    print("""\
    \033[1;32m
         MANAJEMEN PENDATAAN RUMAH
                
    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
    ████╗ ████║██╔════╝████╗  ██║██║   ██║
    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
    •─────────────────⋅☾ ☽⋅────────────────• 
    • 1. Login 
    • 2. Register 
    • 3. Keluar Program        
    \033[0m
    """)

# Fungsi login
def login(username, password):
    global sudah_login #mengakses variabel global
    try:
        if username in akun and akun[username]["password"] == password: #memeriksa apakah username dan password cocok
            role = akun[username]["role"]
            sudah_login = True # mengubah status menjadi sudah login
            print(f"Login berhasil sebagai {role}, selamat datang {username}!") #role sesuai inputan username dan passwordd
            if role == "admin":
                menu_admin() #panggil menu admin
            elif role == "user":
                menu_user() #panggil menu user
        else:  
            raise ValueError("Username atau password salah")
    except ValueError as e:
        print(e)
        os.system("pause")

# Fungsi registrasi pengguna
def register():
    global akun #mengecek variabel global akun
    try:
        username = input("Masukkan username: ")
        if username in akun: #memeriksa apakah username ada di dalam data akun
            raise ValueError("Username sudah terdaftar,buat username lebih unik! ") #errorhandling ketika ada username yang sama dg data akun
            
        password = input("Masukkan password: ")
        akun[username] = {"password": password, "role": "user"}  # Semua pengguna baru menjadi 'user'
        simpan_akun()  # Simpan data akun ke file
        print("Registrasi berhasil, akun berhasil didaftarkan")
        input("Silakan lanjut login. Tekan Enter untuk melanjutkan...")
    except ValueError as e:
        print(e)
        os.system("pause")

# Fungsi untuk menampilkan data rumah dalam format tabel
def tampilkan_data_rumah():
    muat_data()
    if not data_rumah:
        print("Data rumah tidak ada.")
    else:
        table = PrettyTable()
        table.field_names = ["No", "No Rumah", "Jenis", "Pemilik", "Tahun", "Alamat", "status"] #membuat kolom data 
        for i, (no, info) in enumerate(data_rumah.items(), start=1):
            table.add_row([i, no, info["jenis"], info["pemilik"], info["tahun"], info["alamat"], info["status"]])
        print(table)

# Fungsi tampilkan data registrasi untuk admin
def tampilkan_data_registrasi():
    if not akun: #memeriksa ada tidaknya data
        print("Data registrasi tidak ada.")
    else:
        table = PrettyTable()
        table.field_names = ["Username", "Role"] # membuat tabel dengan kolom username dan role
        for username, info in akun.items():
            table.add_row([username, info["role"]])
        print(table)

# Fungsi tambah data rumah dengan menu jenis dan status rumah
def tambah_data_rumah():
    muat_data()

    while True:
        no_rumah = str(input_int("Masukkan nomor rumah: "))
        if no_rumah in data_rumah: #memeriksa nomer rumah apakah ada dalam data rumah
            print("Nomor rumah sudah ada. Silakan coba dengan nomor lain.")
        else:
            break
 


    # Menampilkan menu jenis rumah
    print("""\
          \033[1;32m
===============    
| Jenis Rumah |    
===============     
|   1. beton  |                                           
|   2. kayu   |  
=============== 
          \033[0m 
        """)
    pilihan_jenis = validasi_pilihan_menu(input_int("Pilih jenis rumah: "), 2)
    jenis_rumah = "beton" if pilihan_jenis == 1 else "kayu"

    # Validasi nama pemilik hanya berisi huruf
    while True:
        nama_pemilik_rumah = input("Masukkan nama pemilik rumah: ").strip() #menghapus spasi di awal dan di akhir input
        if nama_pemilik_rumah.replace(" ", "").isalpha(): #nama harus huruf
            break
        print("Nama pemilik hanya boleh berisi huruf. Silakan coba lagi.")

    # Validasi tahun berdiri
    while True:
        tahun_berdiri = input_int("Masukkan tahun berdiri.\nJangka tahun antara 1980-2024: ")
        if 1980 <= tahun_berdiri <= 2024:
            break
        print("Tidak valid, Tahun harus berada dalam rentang 1980-2024.\nSilahkan input ulang dan coba lagi") #jika rentang tahun tidak valid

    alamat_rumah = input("Masukkan alamat rumah: ")

    # Menampilkan menu status rumah
    print("""\
          \033[1;32m
==================
|  Status Rumah |
==================    
|   1. kosong    |
|   2. dijual    |                                           
|   3. ditempati |  
==================
         \033[0m 
        """)
    pilihan_status = validasi_pilihan_menu(input_int("Pilih status rumah: "), 3)
    status_rumah = ["kosong", "dijual", "ditempati"][pilihan_status - 1]

    data_rumah[no_rumah] = {
        "jenis": jenis_rumah,
        "pemilik": nama_pemilik_rumah,
        "tahun": tahun_berdiri,
        "alamat": alamat_rumah,
        "status": status_rumah
    }
    simpan_data()
    print("Berhasil menambahkan data rumah.")


# Fungsi ubah data rumah
def ubah_data_rumah():
    muat_data() #memanggil fungsi muat data
    tampilkan_data_rumah() #memanggil fungsi tampilkan data rumah
    pilih_rumah = str(input("Masukkan nomor rumah yang ingin diupdate: ")).strip()
    
    if pilih_rumah in data_rumah:
        no_rumah_baru = str(input_int(f"Masukkan nomor rumah baru ({pilih_rumah}): "))

        # Pilih jenis rumah
        print("""\
               \033[1;32m
===============    
| Jenis Rumah |    
===============     
|   1. beton  |                                           
|   2. kayu   |  
=============== 
               \033[0m 
        """)
        pilihan_jenis = validasi_pilihan_menu(input_int(f"Masukkan jenis rumah baru ({data_rumah[pilih_rumah]['jenis']}): "), 2)
        jenis_baru = "beton" if pilihan_jenis == 1 else "kayu"

        # Validasi nama pemilik baru
        while True:
            pemilik_baru = input(f"Masukkan nama pemilik rumah baru ({data_rumah[pilih_rumah]['pemilik']}): ").strip()
            if pemilik_baru.replace(" ", "").isalpha():
                break
            print("Nama pemilik hanya boleh berisi huruf. Silakan coba lagi.")
        
        # Validasi tahun berdiri baru
        while True:
            tahun_baru = input_int(f"Masukkan tahun berdiri baru ({data_rumah[pilih_rumah]['tahun']}).\nJangka tahun antara 1980-2024: ")
            if 1980 <= tahun_baru <= 2024:
                break
            print("Tidak valid, Tahun harus berada dalam rentang 1980-2024.\nSilahkan inpat ulang dan coba lagi")

        alamat_baru = input(f"Masukkan alamat rumah baru ({data_rumah[pilih_rumah]['alamat']}): ")

        # Pilih status rumah
        print("""\
              \033[1;32m
==================
|  Status Rumah |
==================    
|   1. kosong    |
|   2. dijual    |                                           
|   3. ditempati |  
==================
           \033[0m   
        """)
        pilihan_status = validasi_pilihan_menu(input_int(f"Masukkan status rumah baru ({data_rumah[pilih_rumah]['status']}): "), 3)
        status_baru = ["kosong", "dijual", "ditempati"][pilihan_status - 1]

        # Update data rumah
        data_rumah[no_rumah_baru] = {
            "jenis": jenis_baru,
            "pemilik": pemilik_baru,
            "tahun": tahun_baru,
            "alamat": alamat_baru,
            "status": status_baru
        }
        if no_rumah_baru != pilih_rumah: 
            del data_rumah[pilih_rumah] #hapus data rumah berdasarkan nomer rumah
        simpan_data() #panggil fungsi simpan data
        print("Data rumah berhasil diubah.")
    else:
        print("Nomor rumah tidak tersedia.")


# Fungsi hapus data rumah
def hapus_data_rumah():
    muat_data()
    tampilkan_data_rumah()
    pilih_rumah = str(input("Masukkan nomor rumah yang ingin dihapus: "))
    if pilih_rumah in data_rumah:
        del data_rumah[pilih_rumah]
        simpan_data()
        print(f"Rumah dengan nomor '{pilih_rumah}' berhasil dihapus.")
    else:
        print("Nomor rumah tidak valid.")

# Menu admin
def menu_admin():
    while True:
        print("""\
              \033[1;32m
===================================
|           MENU ADMIN            |
===================================
|    1. TAMBAH DATA RUMAH         |           
|    2. TAMPILKAN DATA RUMAH      |          
|    3. UBAH DATA RUMAH           |     
|    4. HAPUS DATA RUMAH          |      
|    5. TAMPILKAN DATA REGISTRASI |
|    6. KELUAR                    |  
===================================
               \033[0m
        """)
        pilihan = validasi_pilihan_menu(input_int("Masukkan pilihan menu: "), 6)
        if pilihan == 1:
            tambah_data_rumah() # panggil fungsi tambah data rumah
        elif pilihan == 2:
            tampilkan_data_rumah() # panggil fungsi tampilkan data rumah
        elif pilihan == 3:
            ubah_data_rumah() # panggil fungsi ubah data rumah
        elif pilihan == 4:
            hapus_data_rumah() # panggil fungsi hapus data rumah
        elif pilihan == 5:
            tampilkan_data_registrasi() # panggil fungsi tampilkan data registrasi
        elif pilihan == 6:
            break

# Menu user
def menu_user():
    while True:
        print("""\
              \033[1;32m
===================================
|          MENU USER              |
===================================      
|    1. TAMPILKAN DATA RUMAH      |
|    2. TAMBAHKAN DATA  RUMAH     |
|    3. KELUAR                    |  
===================================
              \033[0m
        """)
        pilih = validasi_pilihan_menu(input_int("Masukkan pilihan menu: "), 4)
        if pilih == 1:
            tampilkan_data_rumah() # panggil fungsi tampilkan data rumah
        elif pilih == 2:
            tambah_data_rumah() # panggil fungsi tambah data rumah
        elif pilih == 3:
            break
        
# Fungsi utama program
def main():
    global data_rumah, akun
    muat_data() # panggil fungsi  muat data
    muat_akun() # panggil fungsi muat akun
    while True:
        tampilkan_menu_utama() # panggil fungsi  tampilkan menu utama
        pilihan = validasi_pilihan_menu(input_int("PILIH: "), 3)
        if pilihan == 1:
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            login(username, password) #memanggil fungsi login
        elif pilihan == 2:
            register()  # Memanggil fungsi register
        elif pilihan == 3:
            print("Keluar dari program.")
            break

if __name__ == "__main__":
    main()
