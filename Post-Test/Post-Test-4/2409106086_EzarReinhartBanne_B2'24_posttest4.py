name = "ezar"
nim = "86"
counts = 0

while counts < 3:
    username = input("Masukkan username anda: ")
    password = input("Masukkan password anda: ")
    if username == name and password == nim:
        print("Anda berhasil login")
        break
    else:
        print("Username atau password salah")
        counts += 1

if counts < 3:
    while True:
        BB = int(input("Masukkan berat badan anda (dalam miligram)= "))
        TB =  float(input("Masukkan tinggi badan anda (dalam Kilometer)= "))

        BB_convert = BB / 1000000
        TB_convert = TB * 1000

        BMI = BB_convert / (TB_convert ** 2)

        if BMI < 18.5:
            print(f"BMI anda adalah {BMI:.2f} Berat badan anda kurang (underweight)")
        elif BMI < 24.9:
            print(f"BMI anda adalah {BMI:.2f} Berat badan anda normal")
        elif BMI <29.9:
            print(f"BMI anda adalah {BMI:.2f} Berat badan anda berlebihan (overweight)")
        elif BMI >= 30:
            print(f"BMI anda adalah {BMI:.2f}, Anda mengalami obesitas")
        
        print("Program telah berakhir, tentukan pilihan anda (1. Jika ingin mengulang program / 2. Jika ingin memberhentikan program): ")
        menu = int(input("PILIHAN (1/2): "))
        if menu == 1:
            pass
        elif menu == 2:
            print("Anda memilih untuk memberhentikan program")
            break