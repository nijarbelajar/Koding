bumbu = ["bawang", "jahe", "lengkuas"]
bahan = ["ayam", "mie"]
alat = ["wajan", "sendok"]
menu = ["Mie ayam"]
utama = ["cek inventory", "masak", "menu"]
tas = ["tas bumbu", "tas bahan", "tas alat"]


def tampil_daftar(items):
    for i, item in enumerate(items, start=1):
        print(f"[{i}] {item}")


def isi():
    print("Pilih tas:")
    tampil_daftar(tas)
    kemana = input("Mau buka tas apa (angka): ")
    k = int(kemana)
    if k == 1:
        show_bumbu()
    elif k == 2:
        show_bahan()
    elif k == 3:
        show_alat()
    else:
        print("Pilihan tas tidak tersedia.")


def show_bumbu():
    if len(bumbu) == 0:
        b = input("Masukan bumbu yang ingin kamu tambahkan: ")
        if b:
            bumbu.append(b)
            print("Bumbu ditambahkan.")
    else:
        print("Isi tas bumbu:")
        tampil_daftar(bumbu)


def show_bahan():
    if len(bahan) == 0:
        b = input("Masukan bahan yang ingin kamu tambahkan: ")
        if b:
            bahan.append(b)
            print("Bahan ditambahkan.")
    else:
        print("Isi tas bahan:")
        tampil_daftar(bahan)


def show_alat():
    if len(alat) == 0:
        a = input("Masukan alat yang ingin kamu tambahkan: ")
        if a:
            alat.append(a)
            print("Alat ditambahkan.")
    else:
        print("Isi tas alat:")
        tampil_daftar(alat)


def program_menu():
    while True:
        print("\n-- Menu Saat Ini --")
        tampil_daftar(menu)
        print("[0] Kembali ke menu utama")
        pilihan = input("Masukkan nama menu baru atau 0 untuk kembali: ")
        if pilihan.strip() == "0":
            break
        if pilihan.strip() == "":
            print("Input kosong — tidak ada perubahan.")
            continue
        menu.append(pilihan)
        print("Menu berhasil ditambahkan:")
        tampil_daftar(menu)


def main():
    while True:
        print("\n== PROGAM UTAMA ==")
        tampil_daftar(utama)
        pilih = input("Mau ngapain nih hari ini (angka, atau 0 untuk keluar): ")
        try:
            p = int(pilih)
        except ValueError:
            print("Masukkan angka yang valid.")
            continue

        if p == 1:
            isi()
        elif p == 2:
            print("Fitur 'masak' belum diimplementasikan.")
        elif p == 3:
            program_menu()
        elif p == 0:
            print("Keluar. Sampai jumpa.")
            break
        else:
            print("Pilihan tidak tersedia.")


if __name__ == "__main__":
    main()
