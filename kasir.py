import time
makanan = ["pizza", "burger", "nasi goreng", "sate"]
minuman = ["teh", "kopi", "jus", "soda"] 
snack = ["keripik", "coklat", "permen", "kue"]
harga_makanan = [10000, 15000, 20000, 25000]
harga_minuman = [10000, 15000, 20000, 25000]
harga_snack = [10000, 15000, 20000, 25000]
keranjang_belanja = []

def pilih_kategori():
    print("Pilih kategori:")
    print("[1] Makanan")
    print("[2] Minuman")
    print("[3] Snack")
    try:
        kat = int(input("Masukkan pilihan: "))
    except ValueError:
        print("Pilihan harus berupa angka.")
        return None, None, None
    if kat == 1:
        return makanan, harga_makanan, "Makanan"
    elif kat == 2:
        return minuman, harga_minuman, "Minuman"
    elif kat == 3:
        return snack, harga_snack, "Snack"
    else:
        print("Pilihan tidak valid")
        return None, None, None

def tambah_menu():
    list_kat, harga_kat, nama_kat = pilih_kategori()
    if list_kat is not None:
        nama_baru = input(f"Masukkan nama item baru untuk {nama_kat}: ")
        try:
            harga_baru = int(input("Masukkan harga: "))
        except ValueError:
            print("Harga harus berupa angka.")
            return
        list_kat.append(nama_baru)
        harga_kat.append(harga_baru)
        print(f"Item {nama_baru} dengan harga Rp{harga_baru} telah ditambahkan ke {nama_kat}.")

def hapus_menu():
    list_kat, harga_kat, nama_kat = pilih_kategori()
    if list_kat is not None:
        if not list_kat:
            print(f"{nama_kat} kosong.")
        else:
            print(f"Daftar {nama_kat}:")
            for i, item in enumerate(list_kat, start=1):
                print(f"[{i}] {item} - Rp{harga_kat[i-1]}")
            try:
                nomor = int(input("Masukkan nomor item yang ingin dihapus: ")) - 1
            except ValueError:
                print("Nomor harus berupa angka.")
                return
            if 0 <= nomor < len(list_kat):
                item_hapus = list_kat.pop(nomor)
                harga_kat.pop(nomor)
                print(f"Item {item_hapus} telah dihapus dari {nama_kat}.")
            else:
                print("Nomor tidak valid.")

def bayar():
    if not keranjang_belanja:
        print("Keranjang kosong, silakan tambah produk terlebih dahulu.")
        return
    total = sum(harga for _, harga in keranjang_belanja)
    print(f'Total Pembayaran: Rp{total}')
    print('Masukkan jumlah uang yang dibayarkan:')
    try:
        uang = int(input())
    except ValueError:
        print("Uang harus berupa angka.")
        return
    if uang >= total:
        kembalian = uang - total
        print(f'Kembalian: Rp{kembalian}')
        print('Terima kasih telah berbelanja!')
        keranjang_belanja.clear()
    else:
        print('Uang tidak cukup, silakan coba lagi.')

while True :
    print ("[1] Tambah Menu")
    print ("[2] Hapus Menu")
    print ("[3] Tampilkan Daftar Makanan")
    print ("[4] Tampilkan Daftar Minuman")
    print ("[5] Tampilkan Daftar Snack")
    print ("[6] Lanjut ke Pembayaran")
    print ("[0] Keluar Program")
    print ( )

    try:
        pilihan = int(input("Masukkan Pilihan Anda: "))
    except ValueError:
        print("Pilihan harus berupa angka.")
        continue

    if pilihan == 0:
        print("Anda Telah Keluar Dari Program")

    elif pilihan == 1:
        print("Anda memasuki Program Tambah Menu.")
        tambah_menu()

    elif pilihan == 2:
        print("Anda memasuki Program Hapus Menu.")
        hapus_menu()

    elif pilihan == 3:
        while True:
            print("Tampilkan Daftar Makanan")
            for i, item in enumerate(makanan, start=1):
                print(f"[{i}] {item} - Rp{harga_makanan[i-1]}")
            print ('pilih nomor menu yang ingin ditambahkan ke keranjang belanja')
            try:
                nomor = int(input("Masukkan nomor menu: ")) - 1
            except ValueError:
                print("Nomor harus berupa angka.")
                continue
            if 0 <= nomor < len(makanan):
                keranjang_belanja.append((makanan[nomor], harga_makanan[nomor]))
                print(f'Keranjang Belanja: {[nama for nama, _ in keranjang_belanja]}')
            else:
                print("Nomor tidak valid.")
            print('apakah anda ingin menambahkan makanan lain? (y/no)')
            choice = input().lower()
            if choice == 'no':
                break
            elif choice == 'y':
                pass
            else:
                print("Masukkan y atau no")
                pass
        # Kembali ke menu utama
    elif pilihan == 4:
       while True:
            print("Tampilkan Daftar Minuman")
            for i, item in enumerate(minuman, start=1):
                print(f"[{i}] {item} - Rp{harga_minuman[i-1]}")
            print ('pilih nomor menu yang ingin ditambahkan ke keranjang belanja')
            try:
                nomor = int(input("Masukkan nomor menu: ")) - 1
            except ValueError:
                print("Nomor harus berupa angka.")
                continue
            if 0 <= nomor < len(minuman):
                keranjang_belanja.append((minuman[nomor], harga_minuman[nomor]))
                print(f'Keranjang Belanja: {[nama for nama, _ in keranjang_belanja]}')
            else:
                print("Nomor tidak valid.")
            print('apakah anda ingin menambahkan minuman lain? (y/no)')
            choice = input().lower()
            if choice == 'no':
                break
            elif choice == 'y':
                pass
            else:
                print("Masukkan y atau no")
                pass
       # Kembali ke menu utama
    elif pilihan == 5:
        while True:
            print("Tampilkan Daftar Snack")
            for i, item in enumerate(snack, start=1):
                print(f"[{i}] {item} - Rp{harga_snack[i-1]}")
            print('pilih nomor menu yang ingin ditambahkan ke keranjang belanja')
            try:
                nomor = int(input("Masukkan nomor menu: ")) - 1
            except ValueError:
                print("Nomor harus berupa angka.")
                continue
            if 0 <= nomor < len(snack):
                keranjang_belanja.append((snack[nomor], harga_snack[nomor]))
                print(f'Keranjang Belanja: {[nama for nama, _ in keranjang_belanja]}')
            else:
                print("Nomor tidak valid.")
            print('apakah anda ingin menambahkan snack lain? (y/no)')
            choice = input().lower()
            if choice == 'no ':
                break
            elif choice == 'y':
                pass
            else:
                print("Masukkan y atau no")
                pass
        # Kembali ke menu utama
    elif pilihan == 6:
        bayar()
        lanjut = input('Apakah ingin tambah menu lain? (y/n): ').lower()
        if lanjut != 'y':
            break
        print("Anda Telah Keluar Dari Program")
        break

    else :
        print ("Pilihan apa sih, masukin yang benar lah")