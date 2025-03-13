import requests

# Prompt input IP Address dari user
ip_address = input("Masukkan IP Address: ")

# Gunakan API Free untuk mendapatkan lokasi berdasarkan IP
url = f"https://ipapi.co/{ip_address}/json/"
response = requests.get(url)

# Cek apakah request berhasil
if response.status_code == 200:
    data = response.json()
    print("\nHasil Pencarian:")
    print(f"IP Address: {data.get('ip', 'Tidak ditemukan')}")
    print(f"Kota: {data.get('city', 'Tidak ditemukan')}")
    print(f"Provinsi: {data.get('region', 'Tidak ditemukan')}")  # <- Kurung tutup sudah benar di sini
    print(f"Negara: {data.get('country_name', 'Tidak ditemukan')}")
else:
    print("Gagal mengambil data. Pastikan IP Address benar atau coba lagi nanti.")
