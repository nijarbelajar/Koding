nama_guru = []
nomor_guru = []
menu = ["Absensi","Ajukan cuti","Dinas Luar","Tambah Guru","Tampilkan Guru","Hapus Guru","Keluar"]
def waktu () :
    time = int (input("Masukkan waktu (dalam jam): "))
    selisih = 0
    if time <= 7 :
        print (f"anda telah masuk kerja pukul {time}, terimakasih sudah tepat waktu")
    elif time > 7 :
        menit = int(input("Masukkan menit keterlambatan: "))
        selisih_jam = time - 7
        selisih_menit = menit
        print (f"anda masuk kerja pukul {time} terlambat {selisih_jam} jam dan {selisih_menit} menit")
def telat () :
    late = input ("apakah anda pernah terlambat sebelumnya? (y/n): ")
    if late.lower() == "y" :
        print ("anda belum dizinkan untuk cuti")
    elif late.lower() == "n" :
        print (f"{nama_guru[n-1]} diizinkan untuk cuti")
def tambah_guru () :
    nama = input("Masukkan nama guru: ")
    nomor = input("Masukkan nomor guru: ")
    nama_guru.append(nama)
    nomor_guru.append(nomor)
    print(f"{nama} dengan nomor {nomor} berhasil ditambahkan.")
def hapus_guru () :
    nama = input("Masukkan nama guru yang ingin dihapus: ")
    nomor = input("Masukkan nomor guru untuk menkonfirmasi penghapusan: ")
    if nama in nama_guru and nomor in nomor_guru:
        nama_guru.remove(nama)
        nomor_guru.remove(nomor)
        print(f"{nama} dengan nomor {nomor} berhasil dihapus.")
    else:
        print("Guru tidak ditemukan.")
def tampilkan_guru () :
    if len(nama_guru) == 0 :
        print ("Belum ada guru")
        tambah_guru()
        for i, nama in enumerate(nama_guru, start=1):
            print(f"{[i]} {nama} nomor guru {nomor_guru[i-1]}")
    else :
        print("Daftar Guru:")
        for i, nama in enumerate(nama_guru, start=1):
            print(f"{i}. {nama} - Nomor: {nomor_guru[i-1]}")
def absen () :
    tampilkan_guru()
    n = int(input("Pilih nomor guru yang ingin absen (1-4): "))
    waktu()
    if n == 1 :
        print (f'{nama_guru[0]} dengan nomor {nomor_guru[0]} telah absen')
    elif n == 2 :
        print (f'{nama_guru[1]} dengan nomor {nomor_guru[1]} telah absen')
    elif n == 3 :
        print (f'{nama_guru[2]} dengan nomor {nomor_guru[2]} telah absen')
    elif n == 4 :
        print (f'{nama_guru[3]} dengan nomor {nomor_guru[3]} telah absen')
def cuti () :
    tampilkan_guru()
    n = int(input("Pilih nomor guru yang ingin mengajukan cuti (1-4): "))
    telat()
    print (nama_guru[n-1])
def dinas_luar () :
    tampilkan_guru()
    n = int(input("Pilih nomor guru yang ingin melakukan dinas luar (1-4): "))
    lokasi_dinas = input("Masukkan lokasi dinas luar: ")
    if n == 1 :
        print (f'{nama_guru[0]} dengan nomor {nomor_guru[0]} telah melakukan dinas luar di {lokasi_dinas}')
    elif n == 2 :
        print (f'{nama_guru[1]} dengan nomor {nomor_guru[1]} telah melakukan dinas luar di {lokasi_dinas}')
    elif n == 3 :
        print (f'{nama_guru[2]} dengan nomor {nomor_guru[2]} telah melakukan dinas luar di {lokasi_dinas}')
    elif n == 4 :
        print (f'{nama_guru[3]} dengan nomor {nomor_guru[3]} telah melakukan dinas luar di {lokasi_dinas}')
while True :
    print ("\n\n=== MENU ===")
    for i,item in enumerate(menu, start=1):
        print(f"{i}. {item}")
    n = int(input("pilih menu (1-7): "))
    if n == 1 :
        absen ()
    elif n == 2 : 
        cuti ()
    elif n == 3 :
        dinas_luar ()
    elif n == 4 :
        tambah_guru()
    elif n == 5 :
        tampilkan_guru()
    elif n == 6 :
        hapus_guru()
    elif n == 7 :
        print("Kamu telah keluar dari program")
        break
    else :
        print("Pilihan tidak valid")
