nama_guru = []
nomor_guru = []
log_absen = []
log_cuti = []
log_dinas = []
telat_status = []
log= ["cetak_log_absen","cetak_log_cuti","cetak_log_dinas"]
edit = ["Tambah Guru","Hapus Guru","Kembali ke menu utama"]
menu = ["Absensi","Ajukan cuti","Dinas Luar","Tampilkan Guru","Menu Edit","Cetak Log","Keluar"]
import datetime
import time
def waktu(n):
    waktu_sekarang = datetime.datetime.now()
    batas_waktu = waktu_sekarang.replace(hour=7, minute=0, second=0)
    if waktu_sekarang > batas_waktu :
        print (f"{nama_guru[n-1]} dengan nomor {nomor_guru[n-1]} telah masuk kerja pukul {waktu_sekarang.strftime('%H:%M:%S')}, terlambat {waktu_sekarang - batas_waktu}")
        return True
    else : 
        print (f"{nama_guru[n-1]} dengan nomor {nomor_guru[n-1]} telah absen tepat waktu pada pukul {waktu_sekarang.strftime('%H:%M:%S')}")
        return False
def telat () :       
    late = input ("apakah anda pernah terlambat sebelumnya? (y/n): ")
    if late.lower() == "y" :
        print ("anda belum dizinkan untuk cuti")
    elif late.lower() == "n" :
        print ("anda diizinkan untuk cuti")
    else :
        print("Pilihan tidak valid")
def tambah_guru () :
    nama = input("Masukkan nama guru: ")
    nomor = input("Masukkan nomor guru: ")
    if nama.strip() == "" or nomor.strip() == "":
        print("Nama dan nomor tidak boleh kosong.")
        return
    nama_guru.append(nama)
    nomor_guru.append(nomor)
    telat_status.append(False)
    print(f"{nama} dengan nomor {nomor} berhasil ditambahkan.")
def hapus_guru () :
    nama = input("Masukkan nama guru yang ingin dihapus: ")
    nomor = input("Masukkan nomor guru untuk menkonfirmasi penghapusan: ")
    if nama in nama_guru and nomor in nomor_guru:
        idx = nama_guru.index(nama)
        nama_guru.remove(nama)
        nomor_guru.remove(nomor)
        telat_status.pop(idx)
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
    if len(nama_guru) == 0:
        return
    n = input(f"Pilih nomor guru yang ingin absen (1-{len(nama_guru)}): ")
    if not n.isdigit():
        print("Pilihan tidak valid")
        return
    n = int(n)
    if 1 <= n <= len(nama_guru):
        terlambat = waktu(n)
        if terlambat:
            telat_status[n-1] = True
        log_absen.append(f'{nama_guru[n-1]} dengan nomor {nomor_guru[n-1]} telah absen pada {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        print (f'{nama_guru[n-1]} dengan nomor {nomor_guru[n-1]} telah absen')
    else :
        print("Pilihan tidak valid")
  
def cuti () :
    if len(nama_guru) == 0:
        print("Belum ada guru dalam database.")
        return
    nama = input("Masukkan nama guru yang ingin mengajukan cuti: ").strip()
    if nama == "":
        print("Nama tidak boleh kosong.")
        return
    if nama not in nama_guru:
        print("Guru tidak ditemukan.")
        return
    idx = nama_guru.index(nama)
    if telat_status[idx]:
        print(f"{nama} pernah terlambat sebelumnya. Cuti tidak diberikan.")
        return
    if datetime.datetime.now() > datetime.datetime.now().replace(hour=7, minute=0, second=0):
        print("Anda tidak dapat mengajukan cuti karena sudah melewati batas waktu absensi.")
        return
    log_cuti.append(f'{nama_guru[idx]} dengan nomor {nomor_guru[idx]} telah mengajukan cuti pada {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print("Cuti telah diajukan, menunggu persetujuan.")
def dinas_luar () :
    tampilkan_guru()
    n = int(input("Pilih nomor guru yang ingin melakukan dinas luar (1-4): "))
    lokasi_dinas = input("Masukkan lokasi dinas luar: ")
    if n == 1 :
        log_dinas.append(f'{nama_guru[n-1]} dengan nomor {nomor_guru[n-1]} telah melakukan dinas luar di {lokasi_dinas} pada {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        print (f'{nama_guru[n-1]} dengan nomor {nomor_guru[n-1]} telah melakukan dinas luar di {lokasi_dinas}')
    elif n == 2 :
        log_dinas.append(f'{nama_guru[n-1]} dengan nomor {nomor_guru[n-1]} telah melakukan dinas luar di {lokasi_dinas} pada {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        print (f'{nama_guru[n-1]} dengan nomor {nomor_guru[n-1]} telah melakukan dinas luar di {lokasi_dinas}')
    else : 
        print("Pilihan tidak valid")
def cetak_log_absen () :
    print("\nLog Absensi:")
    for log in enumerate(log_absen, start=1):
        print(f"{log[0]}. {log[1]}")
def cetak_log_cuti () :
    print("\nLog Cuti:")
    for log in enumerate(log_cuti, start=1):
        print(f"{log[0]}. {log[1]}")
def cetak_log_dinas () :
    print("\nLog Dinas Luar:")
    for log in enumerate(log_dinas, start=1):
        print(f"{log[0]}. {log[1]}")
def menu_edit () :
    print("\n=== Menu Edit Guru ===")
    for i, item in enumerate(edit, start=1):
        print(f"{[i]} {item}")
    pilihan = input("Masukkan nomor menu (0 untuk kembali): ")
    if pilihan == "1":
        tambah_guru()
    elif pilihan == "2":
        hapus_guru()
    elif pilihan == "0":
        return
    else:
        print("Pilihan tidak valid.")
def menu_cetak_log () :
    print("\n=== Menu Cetak Log ===")
    for i, item in enumerate(log, start=1):
        print(f"{[i]} {item}")
    pilihan = input("Masukkan nomor menu (0 untuk kembali): ")
    if pilihan == "1":
        cetak_log_absen()
    elif pilihan == "2":
        cetak_log_cuti()
    elif pilihan == "3":
        cetak_log_dinas()
    elif pilihan == "0":
        return
    else:
        print("Pilihan tidak valid.")
while True :
    print ("\n\n=== MENU ===")
    for i,item in enumerate(menu, start=1):
        print(f"{[i]} {item}")
    n = int(input("pilih menu (1-7): "))
    if n == 1 :
        absen ()
    elif n == 2 : 
        cuti ()
    elif n == 3 :
        dinas_luar ()
    elif n == 4 :
        tampilkan_guru()
    elif n == 5 :
        menu_edit()
    elif n == 6 :
        menu_cetak_log()
    elif n == 7 :
        print("Kamu telah keluar dari program")
        break
    else :
        print("Pilihan tidak valid")
# Program ini dibuat oleh Nijar dengan NISN 0086344912 untuk memenuhi tugas mata pelajaran Pemrograman Dasar.
# Program ini bertujuan untuk mengelola absensi, cuti, dan dinas luar guru di sebuah sekolah.
# Dengan menggunakan def (function), program ini efektif dalam mengorganisir kode dan memudahkan pengguna dalam menjalankan berbagai fungsi yang tersedia.
# penyimpanan data akan hilang ketika terminal ditutup, karena data disimpan dalam list yang bersifat sementara.