pengguna = {
    1: {'username': 'adminganteng', 'password': 'ezarr', 'role': 'admin'},
    2: {'username': 'nasgor', 'password': 'batagor', 'role': 'pengguna'}
}

menu = {
    1: {'nama': 'Tahu Tek', 'harga': 15000}
}

# Fungsi login
def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    for u, u_data in pengguna.items():
        if u_data['username'] == username and u_data['password'] == password:
            return {'id': u, **u_data}
    print("Login gagal! Username atau password salah.\n")
    return None

# Fungsi melihat menu
def lihat_menu():
    print("\nDaftar Menu:")
    for m, m_data in menu.items():
        print(f"ID: {m}, Nama: {m_data['nama']}, Harga: {m_data['harga']}")
    print()

# Fungsi menambah menu
def tambah_menu():
    id_baru = len(menu) + 1
    nama_baru = input("Masukkan nama menu: ")
    harga_baru = input("Masukkan harga menu: ")

    if harga_baru.isdigit():
        menu[id_baru] = {'nama': nama_baru, 'harga': int(harga_baru)}
        print(f"Menu '{nama_baru}' berhasil ditambahkan!\n")
    else:
        print("Input harga harus berupa angka!\n")

# Prosedur membeli menu
def beli_menu():
    id_beli = input("Masukkan ID menu yang ingin dibeli: ")

    if id_beli.isdigit():
        id_beli = int(id_beli)
        if id_beli in menu:
            print(f"Anda telah membeli {menu[id_beli]['nama']} seharga {menu[id_beli]['harga']}\n")
        else:
            print("Menu tidak ditemukan!\n")
    else:
        print("ID harus berupa angka!\n")


while True:
    print("||==============================||")
    print("Selamat Datang di Manajemen Toko Tahu Tek \n1. Login \n2. Register \n3. Keluar")
    print("||==============================||")
    pilihan = input("Pilih Menu: ")

    if pilihan == '1':
        user = login()
        if user:
            if user['role'] == 'admin':
                while True:
                    print("Menu Admin:")
                    print("1. Tambah Menu")
                    print("2. Lihat Menu")
                    print("3. Edit Harga Menu")
                    print("4. Logout")
                    pilihan_admin = input("Pilih Menu: ")

                    if pilihan_admin == '1':
                        tambah_menu()
                    elif pilihan_admin == '2':
                        lihat_menu()
                    elif pilihan_admin == '3':
                        id_edit = input("Masukkan ID menu yang akan diedit: ")
                        if id_edit.isdigit():
                            id_edit = int(id_edit)
                            if id_edit in menu:
                                harga_edit = input(f"Masukkan harga baru untuk {menu[id_edit]['nama']}: ")
                                if harga_edit.isdigit():
                                    menu[id_edit]['harga'] = int(harga_edit)
                                    print(f"Harga {menu[id_edit]['nama']} berhasil diupdate!\n")
                                else:
                                    print("Input harga harus berupa angka!\n")
                            else:
                                print("Menu tidak ditemukan!\n")
                        else:
                            print("ID harus berupa angka!\n")
                    elif pilihan_admin == '4':
                        print("Logout berhasil!\n")
                        break
                    else:
                        print("Pilihan tidak valid!\n")

            elif user['role'] == 'pengguna':
                while True:
                    print("Menu Pengguna:")
                    print("1. Lihat Menu")
                    print("2. Beli Tahu Tek")
                    print("3. Logout")
                    pilihan_pengguna = input("Pilih Menu: ")

                    if pilihan_pengguna == '1':
                        lihat_menu()
                    elif pilihan_pengguna == '2':
                        beli_menu()
                    elif pilihan_pengguna == '3':
                        print("Logout berhasil!\n")
                        break
                    else:
                        print("Pilihan tidak valid!\n")

    elif pilihan == '2':
        id_baru = len(pengguna) + 1
        username_baru = input("Masukkan username baru: ")
        password_baru = input("Masukkan password baru: ")
        pilihanakun = input("Pilih akun\n1. Pengguna\n2. Admin: ")
        if pilihanakun == '1':
            pengguna[id_baru] = {'username': username_baru, 'password': password_baru, 'role': 'pengguna'}
            print("Registrasi pengguna berhasil!\n")
        elif pilihanakun == '2':
            pengguna[id_baru] = {'username': username_baru, 'password': password_baru, 'role': 'admin'}
            print("Registrasi admin berhasil!\n")
        else:
            print("Pilihan tidak valid!\n")

    elif pilihan == '3':
        print("Terima kasih telah mengunjungi Toko Tahu Tek! Sampai jumpa!\n")
        break

    else:
        print("Pilihan tidak valid!\n")
