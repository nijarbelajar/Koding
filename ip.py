import os
import time
# 1 tampilkan daftar server
# 2 Tambah server Baru
# 3 Hapus server
# 4 Jalankan Monitoring (ping semua server)
# 5 keluar progam
ip = ["8.8.4.4","8.8.8.8","1.1.1.1"]
while True :
    print("[1] Tampilkan daftar server")
    print("[2] Tambah server Baru")
    print("[3] Hapus server")
    print("[4] Jalankan Monitoring (ping semua server)")
    print("[0] keluar progam")
    gerbang = input (": ")

    def speed():
        print ("menampilkan daftar ip")
        time.sleep (1)
        print (ip)
        for i in ip:
             print ("menjalankan perintah")
             print ("       ")
             ping = os.system (f'ping {i}')
             if ping == 0:
                    print ("Ping Berhasil")
             else :
                    print ("Ping Gagal")
             
    if gerbang == "0":
        print('anda keluar dari system')
        break
    elif gerbang =='1':
        print ("menampilkan daftar ip")
        print (ip)
    elif gerbang == "2":
        ip_baru = input("Tambahkan server Baru: ")
        ip.append(ip_baru)
    elif gerbang == '3':
        ip_baru = input("Hapus server: ")
        ip.remove(ip_baru)
    elif gerbang =='4':
        speed()
    else :
        print ("pilih [0] untuk keluar dari system")
