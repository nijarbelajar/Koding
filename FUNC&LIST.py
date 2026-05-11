siswa = ["adi", "budi", "caca", "dedi", "erik"]
menu = ["Tambah  Siswa","Hapus Siswa","Tampilkan Siswa","Keluar"]
#Function
def tampilkan_siswa():
    print("Daftar Siswa:")
    for i, nama in enumerate(siswa, start=1):
        print(f"{i}. {nama}")
def tambah () :
    nama = input("Masukkan nama siswa: ")
    siswa.append(nama)
    print(f"{nama} berhasil ditambahkan.")
    pilihan_tambah = input("apakah anda ingin melihat daftar siswa? (y/n): ")
    if pilihan_tambah.lower() == "y":
        tampilkan_siswa()
    else :
        print("Kembali ke menu utama.")
def hapus() :
    nama = input("Masukkan nama siswa yang ingin dihapus: ")
    if nama in siswa:
        siswa.remove(nama)
        print(f"{nama} berhasil dihapus.")
        pilihan_hapus = input("apakah anda ingin melihat daftar siswa? (y/n): ")
        if pilihan_hapus.lower() == "y":
            tampilkan_siswa()
        else :
            print("Kembali ke menu utama.")
    else:
        print("Siswa tidak ditemukan.")
        
# Program utama
while True : 
    print("\n\n=== MENU ===")
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item}")
    choice = int(input("Pilih menu (1-4): "))
    if choice == 1:
        tambah()
    elif choice == 2:
        hapus()
    elif choice == 3:
        tampilkan_siswa()
    elif choice == 4:
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")