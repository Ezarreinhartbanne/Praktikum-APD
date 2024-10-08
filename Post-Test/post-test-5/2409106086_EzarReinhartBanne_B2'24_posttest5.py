pengguna = [
    [1, 'adminganteng', 'ezarr', 'admin'],
    [2, 'nasgor', 'batagor', 'pengguna']
]

menu = [
    [1, 'Tahu Tek', 15000],
]

while True:
    print("||==============================||")
    print("Selamat Datang di Manajemen Toko Tahu Tek \n1. Login \n2. Register \n3. Keluar")
    print("||==============================||")
    pilihan = input("Pilih Menu: ")

    if pilihan == '1':
        print("ANDA MEMILIH FITUR LOGIN \nSILAHKAN MASUKKAN USERNAME DAN PASSWORD ANDA ")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        user = None
        for u in pengguna:
            if u[1] == username and u[2] == password:
                user = u
                break

        if user:
            print(f"\nLogin berhasil sebagai {user[1]} ({user[3]})\n")
            if user[3] == 'admin':
                while True:
                    print("Menu Admin:")
                    print("1. Tambah Menu")
                    print("2. Lihat Menu")
                    print("3. Edit Harga Menu")
                    print("4. Logout")
                    pilihan_admin = input("Pilih Menu: ")

                    if pilihan_admin == '1':
                        id_baru = len(menu) + 1
                        nama_baru = input("Masukkan nama menu: ")
                        harga_baru = input("Masukkan harga menu: ")

                        if harga_baru.isdigit():
                            menu.append([id_baru, nama_baru, int(harga_baru)])
                            print(f"Menu '{nama_baru}' berhasil ditambahkan!\n")
                        else:
                            print("Input harga harus berupa angka!\n")

                    elif pilihan_admin == '2':
                        print("\nDaftar Menu:")
                        for m in menu:
                            print(f"ID: {m[0]}, Nama: {m[1]}, Harga: {m[2]}")
                        print()

                    elif pilihan_admin == '3':
                        id_edit = input("Masukkan ID menu yang akan diedit: ")

                        if id_edit.isdigit():
                            id_edit = int(id_edit)
                            for m in menu:
                                if m[0] == id_edit:
                                    harga_edit = input(f"Masukkan harga baru untuk {m[1]}: ")

                                    if harga_edit.isdigit():
                                        m[2] = int(harga_edit)
                                        print(f"Harga {m[1]} berhasil diupdate!\n")
                                    else:
                                        print("Input harga harus berupa angka!\n")
                                    break
                            else:
                                print("Menu tidak ditemukan!\n")
                        else:
                            print("ID harus berupa angka!\n")

                    elif pilihan_admin == '4':
                        print("Logout berhasil!\n")
                        break

                    else:
                        print("Pilihan tidak valid!\n")

            elif user[3] == 'pengguna':
                while True:
                    print("Menu Pengguna:")
                    print("1. Lihat Menu")
                    print("2. Beli Tahu Tek")
                    print("3. Logout")
                    pilihan_pengguna = input("Pilih Menu: ")

                    if pilihan_pengguna == '1':
                        print("\nDaftar Menu:")
                        for m in menu:
                            print(f"ID: {m[0]}, Nama: {m[1]}, Harga: {m[2]}")
                        print()

                    elif pilihan_pengguna == '2':
                        id_beli = input("Masukkan ID menu yang ingin dibeli: ")

                        if id_beli.isdigit():
                            id_beli = int(id_beli)
                            for m in menu:
                                if m[0] == id_beli:
                                    print(f"Anda telah membeli {m[1]} seharga {m[2]}\n")
                                    break
                            else:
                                print("Menu tidak ditemukan!\n")
                        else:
                            print("ID harus berupa angka!\n")

                    elif pilihan_pengguna == '3':
                        print("Logout berhasil!\n")
                        break

                    else:
                        print("Pilihan tidak valid!\n")
        else:
            print("Login gagal! Username atau password salah.\n")

    elif pilihan == '2':
        id_baru = len(pengguna) + 1
        username_baru = input("Masukkan username baru: ")

        username_terpakai = False
        for u in pengguna:
            if u[1] == username_baru:
                username_terpakai = True
                break

        if username_terpakai:
            print("Username telah digunakan, silahkan login atau pilih username lain!\n")
        else:
            password_baru = input("Masukkan password baru: ")
            pilihanakun = input("Pilih akun\n1. Pengguna\n2. Admin: ")
            if pilihanakun == '1':
                pengguna.append([id_baru, username_baru, password_baru, 'pengguna'])
                print("Registrasi pengguna berhasil!\n")
            elif pilihanakun == '2':
                pengguna.append([id_baru, username_baru, password_baru, 'admin'])
                print("Registrasi admin berhasil!\n")
            else:
                print("Pilihan tidak valid!\n")

    elif pilihan == '3':
        print("Terima kasih telah mengunjungi Toko Tahu Tek! Sampai jumpa!\n")
        break

    else:
        print("Pilihan tidak valid!\n")