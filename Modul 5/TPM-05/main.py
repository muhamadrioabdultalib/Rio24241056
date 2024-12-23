# Input data
member = input("Apakah Member? (ya/tidak): ").strip().lower()
total_belanja = float(input("Masukkan total belanja Rp: "))

# Variabel untuk menyimpan diskon
diskon_persen = 0

# Logika diskon
if member == "ya":
    if total_belanja > 500000:
        diskon_persen = 20
    else:
        diskon_persen = 10
else:  # Jika bukan member
    if total_belanja > 500000:
        diskon_persen = 5
    else:
        diskon_persen = 0

# Perhitungan
diskon_rp = total_belanja * (diskon_persen / 100)
total_bayar = total_belanja - diskon_rp

# Output hasil
print(f"\nTotal belanja: Rp. {total_belanja:,.0f}")
print(f"Diskon persen: {diskon_persen}%")
print(f"Diskon Rp: {diskon_rp:,.0f}")
print(f"Bayar Rp. {total_bayar:,.0f}")