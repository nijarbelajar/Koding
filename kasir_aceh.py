#               LOGIKA
# mulai
# buka apk atau web 
# menentukan lokasi pembeli 
# memilih menu makan 
# (decicion) memilih menu tambahan atau tidak  
# pembayaran
# (decicion) sudah terbayar atau belum
# jika pembayaran berhasil makanan dimasak
# jika pembayaran gagal/ belum , maka menunggu pembayaran berhasil

#               DATA BASE
makanan = ['Mie Aceh Original','Mie Aceh Telur','Mie Aceh Udang','Mie Aceh Daging','Mie Aceh Special']
minuman = ['Es Teh','Teh Hangat','Es Sirup','Es Timun Serut','Teh Tarek Dingin','Teh Tarek Panas','Kopi aceh','Es Capucino','Es Nutrisari Jeruk','Es Jeruk']
jajan = ['10 Sosis Solo','Risol Mayo','Piscok','Tamalada']
Harga_makan = [10000,13000,15000,17000,20000]
Harga_minum = [3000,3000,4000,4000,7000,6000,5000,7000,4000,4000]
Harga_jajan = [10000,4000,2500,2500]
keranjang_belanja = []
harga_jarak =[5000, 10000, 15000, 20000, 25000]
nama_pembeli = ''
jarak_pembeli = 0
ongkir = 0

#               SYSTEM
def input_data_pelanggan():
    global nama_pembeli, jarak_pembeli, ongkir
    nama_pembeli = input("Masukkan nama pembeli: ").strip()
    while not nama_pembeli:
        print("Nama tidak boleh kosong.")
        nama_pembeli = input("Masukkan nama pembeli: ").strip()

    while True:
        jarak = input("Masukkan jarak lokasi dari penjual (km): ")
        if not jarak.isdigit():
            print("Masukkan angka km yang valid.")
            continue
        jarak = int(jarak)
        if jarak < 0:
            print("Jarak tidak boleh negatif.")
            continue
        jarak_pembeli = jarak
        break

    if jarak_pembeli <= 3:
        ongkir = harga_jarak[0]
    elif jarak_pembeli <= 5:
        ongkir = harga_jarak[1]
    elif jarak_pembeli <= 10:
        ongkir = harga_jarak[2]
    elif jarak_pembeli <= 15:
        ongkir = harga_jarak[3]
    else:
        ongkir = harga_jarak[4]

    print(f"Nama pembeli: {nama_pembeli}")
    print(f"Jarak: {jarak_pembeli} km")
    print(f"Ongkir: Rp{ongkir}")


def tampilkan_menu(nama_menu, daftar_menu, daftar_harga):
    print(f"\nMenu {nama_menu}")
    for i, item in enumerate(daftar_menu):
        print(f"[{i+1}] {item} - Rp{daftar_harga[i]}")
    print("[0] Kembali ke menu utama")


def pilih_dari_menu(nama_menu, daftar_menu, daftar_harga):
    while True:
        tampilkan_menu(nama_menu, daftar_menu, daftar_harga)
        pilihan = input("Masukkan nomor menu (0 untuk kembali): ")
        if not pilihan.isdigit():
            print("Masukkan angka yang valid.")
            continue

        nomor = int(pilihan)
        if nomor == 0:
            return
        if 1 <= nomor <= len(daftar_menu):
            nama = daftar_menu[nomor - 1]
            harga = daftar_harga[nomor - 1]
            keranjang_belanja.append((nama_menu, nama, harga))
            print(f"Ditambahkan ke keranjang: {nama} - Rp{harga}")
            print(f"Keranjang sekarang: {[item for _, item, _ in keranjang_belanja]}")
            continue

        print("Nomor tidak valid.")


def lihat_keranjang():
    if not keranjang_belanja:
        print("Keranjang belanja kosong.")
        return

    print("\nKeranjang Belanja:")
    kategori_items = {}
    subtotal = 0
    for kategori, nama, harga in keranjang_belanja:
        kategori_items.setdefault(kategori, []).append((nama, harga))
        subtotal += harga

    for kategori in ['Makanan', 'Minuman', 'Snack & Tambahan']:
        if kategori in kategori_items:
            print(f"\n{kategori}:")
            for nama, harga in kategori_items[kategori]:
                print(f"  - {nama} - Rp{harga}")

    print(f"\nSubtotal: Rp{subtotal}")
    print(f"Ongkir: Rp{ongkir}")
    print(f"Total Bayar: Rp{subtotal + ongkir}")


def total_keranjang():
    return sum(harga for _, _, harga in keranjang_belanja)


def pilih_metode_pembayaran():
    metode = {
        '1': 'COD',
        '2': 'QRIS',
        '3': 'ShopeePay',
        '4': 'Transfer Bank BRI'
    }
    while True:
        print("\nPilih Metode Pembayaran:")
        print("[1] COD")
        print("[2] QRIS")
        print("[3] ShopeePay")
        print("[4] Transfer Bank BRI")
        pilihan = input("Masukkan nomor metode pembayaran: ")
        if pilihan in metode:
            return metode[pilihan]
        print("Pilihan tidak valid. Silakan pilih 1-4.")


def pembayaran():
    if not keranjang_belanja:
        print("Keranjang belanja kosong. Tambahkan pesanan dulu sebelum bayar.")
        return

    lihat_keranjang()
    subtotal = total_keranjang()
    total = subtotal + ongkir
    metode = pilih_metode_pembayaran()

    if metode == 'COD':
        print(f"Metode: COD")
        print(f"Total yang harus dibayar saat diterima: Rp{total}")
        keranjang_belanja.clear()
        return

    print(f"Metode: {metode}")
    while True:
        uang = input(f"Masukkan jumlah uang pembeli (Total Rp{total}) atau 0 untuk batal: Rp")
        if not uang.isdigit():
            print("Masukkan angka yang valid.")
            continue

        uang = int(uang)
        if uang == 0:
            print("Pembayaran dibatalkan.")
            return
        if uang < total:
            kekurangan = total - uang
            print(f"Uang tidak cukup. Kurang Rp{kekurangan}.")
            continue

        kembalian = uang - total
        print(f"Pembayaran berhasil lewat {metode}. Kembalian: Rp{kembalian}")
        keranjang_belanja.clear()
        return


def tampilan_utama():
    print(f"\nPembeli: {nama_pembeli} | Jarak: {jarak_pembeli} km | Ongkir: Rp{ongkir}")
    print("[1] Menu Makanan")
    print("[2] Menu Minuman")
    print("[3] Menu Snack & Tambahan")
    print("[4] Lihat Keranjang")
    print("[5] Pembayaran")
    print("[6] Keluar")


input_data_pelanggan()
while True:
    tampilan_utama()
    pilihan = input("Mau masuk ke menu apa: ")
    if pilihan == '1':
        pilih_dari_menu('Makanan', makanan, Harga_makan)
    elif pilihan == '2':
        pilih_dari_menu('Minuman', minuman, Harga_minum)
    elif pilihan == '3':
        pilih_dari_menu('Snack & Tambahan', jajan, Harga_jajan)
    elif pilihan == '4':
        lihat_keranjang()
    elif pilihan == '5':
        pembayaran()
    elif pilihan == '6':
        print('Terima kasih. Sampai jumpa!')
        break
    else:
        print('Maaf, pilihan tidak tersedia. Tolong masukkan angka yang tersedia.')
