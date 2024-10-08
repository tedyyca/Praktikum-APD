data_rumah = []
akun = [["tedy", "123", "admin"]]
    
    
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
        for cek_login in akun:
            if cek_login[0]==username and cek_login[1]==password:
                if cek_login[2]=="admin":
                    print(f"login berhasil admin, selamat datang, {username}")
                    
                    while True:
                        print( """
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
                            proses_tambah = [no_rumah, jenis_rumah, nama_pemilik_rumah, tahun_berdiri, alamat_rumah]
                            data_rumah.append(proses_tambah)
                            print("berhasil menambahkan data rumah")
                        elif pilih == "2":
                            if not data_rumah:
                                print("data rumah tidak ada")
                            else:
                                print("\n=== Data Rumah ===")
                                print(f"{'No':<4} {'No Rumah':<12} {'Jenis':<20} {'Pemilik':<15} {'Tahun':<6} {'Alamat'}")
                                print("-" * 90)
                                for i, data in enumerate(data_rumah, start=1):
                                    print(f"{i:<4} {data[0]:<12} {data[1]:<20} {data[2]:<15} {data[3]:<6} {data[4]}")
                        elif pilih == "3":
                            if not data_rumah:
                                print("data rumah tidak ada")
                            else:
                                print("\n=== Data Rumah ===")
                                print(f"{'No':<4} {'No Rumah':<12} {'Jenis':<20} {'Pemilik':<15} {'Tahun':<6} {'Alamat'}")
                                print("-" * 90)
                                for i, data in enumerate(data_rumah, start=1):
                                    print(f"{i:<4} {data[0]:<12} {data[1]:<20} {data[2]:<15} {data[3]:<6} {data[4]}")
                            pilih_rumah = int(input("Masukkan nomor rumah yang ingin diupdate: "))
                            if pilih_rumah in range(1, len(data_rumah) + 1):
                                akses_indeks = data_rumah[pilih_rumah-1]
                                akses_indeks[0] = int(input(f"Masukkan nomor rumah baru ({akses_indeks[0]}): "))
                                akses_indeks[1] = input(f"Masukkan jenis rumah baru ({akses_indeks[1]}): ")
                                akses_indeks[2] = input(f"Masukkan nama pemilik rumah baru ({akses_indeks[2]}): ")
                                akses_indeks[3] = input(f"Masukkan tahun berdiri rumah baru ({akses_indeks[3]}): ")
                                akses_indeks[4] = input(f"Masukkan alamat rumah baru ({akses_indeks[4]}): ")
                                print("data rumah berhasil diubah")
                            else:
                                print("pilihan tidak tersedia")
                        elif pilih == "4":
                            if not data_rumah:
                                print("data rumah tidak ada")
                            else:
                                print("\n=== Data Rumah ===")
                                print(f"{'No':<4} {'No Rumah':<12} {'Jenis':<20} {'Pemilik':<15} {'Tahun':<6} {'Alamat'}")
                                print("-" * 90)
                                for i, data in enumerate(data_rumah, start=1):
                                    print(f"{i:<4} {data[0]:<12} {data[1]:<20} {data[2]:<15} {data[3]:<6} {data[4]}")
                            pilih_rumah = int(input("Masukkan nomor rumah yang ingin dihapus: "))
                            if pilih_rumah in range(1, len(data_rumah) + 1):
                                yang_dihapus = data_rumah.pop(pilih_rumah - 1) 
                                print(f"Rumah dengan nomor '{yang_dihapus[0]}' berhasil dihapus.")
                            else:
                                print("Nomor rumah tidak valid.")
                        elif pilih == "5":
                            break
                        else:
                            print("pilihan tidak valid") 
                                                
                elif cek_login[2]=="user":
                    print(f"login berhasil user, selamat datang, {username}")
                    print( """
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
                            for i, data in enumerate(data_rumah, start=1):
                                print(f"{i:<4} {data[0]:<12} {data[1]:<20} {data[2]:<15} {data[3]:<6} {data[4]}")
                    elif pilih == "2":
                        break
            else:
                print("username atau password salah")
    elif pilih == 2:
        
        username = input("masukkan username : ")
        password = input("masukkan password : ")
        role = input("1 = admin, 2 user : ")
        if role == "1":
            role = "admin"
        elif role == "2":
            role = "user"
        else:
            print("invalid")
        proses_tambah = [username, password,role]
        akun.append(proses_tambah)
        print("register berhasil")
    elif pilih == 3:
        exit(0)

    
            
    

    
    
    


