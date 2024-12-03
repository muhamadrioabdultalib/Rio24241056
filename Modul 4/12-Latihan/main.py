tinggi_badan = float(input("masukan tinggi badan :"))
berat_badan = float(input("masukan berat badan :"))

tinggi_badan = tinggi_badan / 100
BMI = berat_badan / (tinggi_badan **2)

print(f"skor bmi adalah : {BMI:.1f}")