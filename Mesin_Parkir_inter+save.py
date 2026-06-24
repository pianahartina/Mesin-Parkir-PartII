from datetime import datetime
import locale

file_laporan = "laporan_keu_park_v2.txt"
TARIF_MOTOR = 3000 # per jam
TARIF_MOBIL = 5000 # per jam

print("==== MESIN PARKIR MINI V3 ====")
print("1. Motor")
print("2. Mobil")
print("3. Keluar & Liat Laporan")
print("-" * 30)

while True:
    pilihan = input("Pilih jenis kendaraan 1/2/3:").strip()

    if pilihan == "3":
        break

    if pilihan not in ["1", "2"]:
        print("Pilihan gak ada! Pilih 1 atau 2 atau 3")
        continue

    # Tentuin jenis + tarif
    jenis = "Motor" if pilihan == "1" else "Mobil"
    tarif_per_jam = TARIF_MOTOR if jenis == "Motor" else TARIF_MOBIL

    try:
        jam_masuk = float(input(f"Jam masuk {jenis} :")) #[contoh: 8.5]
        jam_keluar = float(input(f"Jam keluar {jenis} :")) # [contoh: 10.25]
    except ValueError:
        print("Error: Jam harus angka!") #Contoh 8.5 atau 10.25
        continue

    if jam_keluar <= jam_masuk:
        print("Error: Jam keluar harus lebih besar dari jam masuk!")
        continue

    # Hitung
    lama_parkir = jam_keluar - jam_masuk 
    total_tarif = int(lama_parkir * tarif_per_jam)
    waktu_sekarang = datetime.now().strftime("%A, %Y-%m-%d  %H:%M")

    # Format 1 baris: Jenis | Waktu | Masuk: x Keluar: y Rpz
    baris_laporan = f"{jenis} | {waktu_sekarang} | Masuk: {jam_masuk} Keluar: {jam_keluar}  Rp {total_tarif}\n"

    #simpen ke .txt mode "a" = append, biar gak numpuk data lama
    with open(file_laporan, "a") as f:
        f.write(baris_laporan)

    print(f"Data {jenis} tersimpan!")
    print(f" Lama parkir: {lama_parkir:.1f} jam | Tarif: Rp{total_tarif:,}\n")

print("\nSelesai input. Mau liat laporan?")
print(f"File laporan ada di: {file_laporan}")
    
