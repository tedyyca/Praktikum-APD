data_rumah = {}
akun = {"tedy": {"password": "123", "role": "admin"}}
is_logged_in = False

def tampilkan_menu_utama():
    print("""
\033[1;32m
███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔════╝████╗  ██║██║   ██║
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
•─────────────────⋅☾ ☽⋅────────────────•
\u2022 1. Login
\u2022 2. Register
\u2022 3. Keluar Program        
\033[0m""")

def login(username, password):
    global is_logged_in
    try:
        if username in akun and akun[username]["password"] == password:
            role = akun[username]["role"]
            is_logged_in = True
            print(f"Login berhasil sebagai {role}, selamat datang, {username}")
            if role == "admin":
                menu_admin()
            elif role == "user":
                menu_user()
        else:
            raise ValueError("Username atau password salah")
    except ValueError as e:
        print(e)

def input_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Input harus berupa angka.")
        return input_int(prompt)

def validasi_pilihan_menu(pilihan):
    try:
        if pilihan < 1 or pilihan > 5:
            raise ValueError("Pilihan tidak valid, coba lagi.")
        return pilihan
    except ValueError as e:
        print(e)
        return validasi_pilihan_menu(input_int("Masukkan pilihan: "))

def register():
    global akun  
    try:
        username = input("Masukkan username: ")
        if username in akun:
            raise ValueError("Username sudah terdaftar")
        password = input("Masukkan password: ")
        role = input("1 = admin, 2 = user: ")
        if role == "1":
            role = "admin"
        elif role == "2":
            role = "user"
        else:
            raise ValueError("Role tidak valid")
        akun[username] = {"password": password, "role": role}
        print("Registrasi berhasil")
    except ValueError as e:
        print(e)


def tampilkan_data_rumah():
    if not data_rumah:
        print("Data rumah tidak ada.")
    else:
        print("\n=== Data Rumah ===")
        print(f"{'No':<4} {'No Rumah':<12} {'Jenis':<20} {'Pemilik':<15} {'Tahun':<6} {'Alamat'}")
        print("-" * 90)
        for i, (no, info) in enumerate(data_rumah.items(), start=1):
            print(f"{i:<4} {no:<12} {info['jenis']:<20} {info['pemilik']:<15} {info['tahun']:<6} {info['alamat']}")


def menu_user():
     while True:
                    print("""
==================================
|          DATA RUMAH           |
==================================      
|    1. TAMPILKAN DATA RUMAH    |                                           
|    2. KELUAR                  |  
==================================
""")
                    pilih = input("masukkan pilihan menu: ") 
                    if pilih == "1":
                        if not data_rumah:
                            print("data rumah tidak ada")
                        else:
                            print("\n=== Data Rumah ===")
                            print(f"{'No':<4} {'No Rumah':<12} {'Jenis':<20} {'Pemilik':<15} {'Tahun':<6} {'Alamat'}")
                            print("-" * 90)
                            for i, (no, info) in enumerate(data_rumah.items(), start=1):
                                print(f"{i:<4} {no:<12} {info['jenis']:<20} {info['pemilik']:<15} {info['tahun']:<6} {info['alamat']}")
                    elif pilih == "2":
                        break


def ubah_data_rumah():
    if not data_rumah:
        print("data rumah tidak ada")
        return
    else:
        print("\n=== Data Rumah ===")
        print(f"{'No':<4} {'No Rumah':<12} {'Jenis':<20} {'Pemilik':<15} {'Tahun':<6} {'Alamat'}")
        print("-" * 90)
        for i, (no, info) in enumerate(data_rumah.items(), start=1):
            print(f"{i:<4} {no:<12} {info['jenis']:<20} {info['pemilik']:<15} {info['tahun']:<6} {info['alamat']}")
            
    pilih_rumah = int(input("Masukkan nomor rumah yang ingin diupdate: "))
    if pilih_rumah in data_rumah:
        no_rumah_baru = int(input(f"Masukkan nomor rumah baru ({pilih_rumah}): "))
        jenis_baru = input(f"Masukkan jenis rumah baru ({data_rumah[pilih_rumah]['jenis']}): ")
        pemilik_baru = input(f"Masukkan nama pemilik rumah baru ({data_rumah[pilih_rumah]['pemilik']}): ")
        tahun_baru = input(f"Masukkan tahun berdiri rumah baru ({data_rumah[pilih_rumah]['tahun']}): ")
        alamat_baru = input(f"Masukkan alamat rumah baru ({data_rumah[pilih_rumah]['alamat']}): ")
        
        
        data_rumah[no_rumah_baru] = {
            "jenis": jenis_baru,
            "pemilik": pemilik_baru,
            "tahun": tahun_baru,
            "alamat": alamat_baru
        }
        
        
        if no_rumah_baru != pilih_rumah:
            del data_rumah[pilih_rumah]
        
        print("data rumah berhasil diubah")
    else:
        print("nomor rumah tidak tersedia")


def hapus_data_rumah():
    if not data_rumah:
        print("data rumah tidak ada")
        return
    else:
        print("\n=== Data Rumah ===")
        print(f"{'No':<4} {'No Rumah':<12} {'Jenis':<20} {'Pemilik':<15} {'Tahun':<6} {'Alamat'}")
        print("-" * 90)
        for i, (no, info) in enumerate(data_rumah.items(), start=1):
            print(f"{i:<4} {no:<12} {info['jenis']:<20} {info['pemilik']:<15} {info['tahun']:<6} {info['alamat']}")
            
    pilih_rumah = int(input("Masukkan nomor rumah yang ingin dihapus: "))
    if pilih_rumah in data_rumah:
        del data_rumah[pilih_rumah]
        print(f"Rumah dengan nomor '{pilih_rumah}' berhasil dihapus.")
    else:
        print("Nomor rumah tidak valid.")

def menu_admin():
    while True:
        print("""
================================
|           DATA RUMAH          |
================================
|    1. TAMBAH DATA RUMAH       |           
|    2. TAMPILKAN DATA RUMAH    |          
|    3. UBAH DATA RUMAH         |     
|    4. HAPUS DATA RUMAH        |      
|    5. KELUAR                  |  
================================
""")
        pilihan = input_int("Masukkan pilihan menu: ")
        pilihan = validasi_pilihan_menu(pilihan)
        if pilihan == 1:
            tambah_data_rumah()
        elif pilihan == 2:
            tampilkan_data_rumah()
        elif pilihan == 3:
            ubah_data_rumah()
        elif pilihan == 4:
            hapus_data_rumah()
        elif pilihan == 5:
            break


def tambah_data_rumah():
    no_rumah = input_int("Masukkan nomor rumah: ")
    jenis_rumah = input("Masukkan jenis rumah: ")
    nama_pemilik_rumah = input("Masukkan nama pemilik rumah: ")
    tahun_berdiri = input("Masukkan tahun berdiri: ")
    alamat_rumah = input("Masukkan alamat rumah: ")

    
    rumah_baru = {
        "jenis": jenis_rumah,
        "pemilik": nama_pemilik_rumah,
        "tahun": tahun_berdiri,
        "alamat": alamat_rumah
    }

    data_rumah[no_rumah] = rumah_baru
    print("Berhasil menambahkan data rumah.")


def main():
    while True:
        tampilkan_menu_utama()
        try:
            pilihan = input_int("PILIH: ")
            if pilihan == 1:
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                login(username, password)
            elif pilihan == 2:
                register()
            elif pilihan == 3:
                print("Keluar dari program.")
                break
            else:
                raise ValueError("Pilihan tidak valid.")
        except ValueError as e:
            print(e)

main()
