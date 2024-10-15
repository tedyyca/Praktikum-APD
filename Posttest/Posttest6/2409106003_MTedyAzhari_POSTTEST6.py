data_rumah = {}
akun = {
    "tedy": {"password": "123", "role": "admin"}
}

while True:
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
    pilih = int(input("PILIH: "))
    if pilih == 1:
        
        username = input("masukkan username : ")
        password = input("masukkan password : ")
        
        if username in akun and akun[username]["password"] == password:
            role = akun[username]["role"]
            print(f"login berhasil {role}, selamat datang, {username}")
            
            if role == "admin":
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
                    pilih = input("masukkan pilihan menu: ") 
                    if pilih == "1":
                        no_rumah = int(input("masukkan nomor rumah: "))
                        jenis_rumah = input("masukkan jenis rumah: ") 
                        nama_pemilik_rumah = input("masukkan nama pemilik rumah: ") 
                        tahun_berdiri = input("masukkan tahun berdiri: ") 
                        alamat_rumah = input("masukkan alamat rumah: ") 
                        
                        data_rumah[no_rumah] = {
                            "jenis": jenis_rumah,
                            "pemilik": nama_pemilik_rumah,
                            "tahun": tahun_berdiri,
                            "alamat": alamat_rumah
                        }
                        print("berhasil menambahkan data rumah")
                    elif pilih == "2":
                        if not data_rumah:
                            print("data rumah tidak ada")
                        else:
                            print("\n=== Data Rumah ===")
                            print(f"{'No':<4} {'No Rumah':<12} {'Jenis':<20} {'Pemilik':<15} {'Tahun':<6} {'Alamat'}")
                            print("-" * 90)
                            for i, (no, info) in enumerate(data_rumah.items(), start=1):
                                print(f"{i:<4} {no:<12} {info['jenis']:<20} {info['pemilik']:<15} {info['tahun']:<6} {info['alamat']}")
                    elif pilih == "3":
                        if not data_rumah:
                            print("data rumah tidak ada")
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
                    elif pilih == "4":
                        if not data_rumah:
                            print("data rumah tidak ada")
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
                    elif pilih == "5":
                        break
                    else:
                        print("pilihan tidak valid")
            
            elif role == "user":
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
        else:
            print("username atau password salah")
            
    elif pilih == 2:
        username = input("masukkan username : ")
        password = input("masukkan password : ")
        role = input("1 = admin, 2 = user: ")
        if role == "1":
            role = "admin"
        elif role == "2":
            role = "user"
        else:
            print("invalid role")
            continue
        akun[username] = {"password": password, "role": role}
        print("register berhasil")
    
    elif pilih == 3:
        exit(0)