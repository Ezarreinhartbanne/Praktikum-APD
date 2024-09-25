print("""
||----------------------------------------------------------||
                        Kalkulator BMI
                Made by Ezar Reinhart Banne
                          2409106086
||----------------------------------------------------------||
""")

#input
BB = int(input("Masukkan berat badan anda (dalam miligram)= "))
TB =  float(input("Masukkan tinggi badan anda (dalam Kilometer)= "))

#convert satuan
BB_convert = BB / 1000000
TB_convert = TB * 1000

#perhitungan BMI
BMI = BB_convert / (TB_convert ** 2)

#percabangan
if BMI < 18.5:
    print(f"BMI anda adalah {BMI:.2f} Berat badan anda kurang (underweight)")
elif BMI < 24.9:
    print(f"BMI anda adalah {BMI:.2f} Berat badan anda normal")
elif BMI <29.9:
    print(f"BMI anda adalah {BMI:.2f} Berat badan anda berlebihan (overweight)")
elif BMI >= 30:
    print("Anda mengalami obesitas")