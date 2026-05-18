bumbu = []
bahan = []
alat = []
menu = ["Mie ayam"]
utama = ["cek inventory",
         "masak",
         "menu"       ]
tas =   [   "tas bumbu",
            "tas bahan",
            "tas alat"]

def isi() :
    for i ,item in enumerate (tas,start=1):
        print (f"[{i}] {item}")
    kemana = input ("Mau buka tas apa: ")
    if kemana == 1 :
        for i ,item in enumerate (bumbu,start=1):
                print (f"[{i}] {item}")
                perbumbuan ()
    elif kemana == 2 :
        for i, item in enumerate (bahan,start=1) :
                print (f'[{i}] {item}')
                perbahanan ()
    elif kemana == 3 :
        for i, item in enumerate (alat,strat=1):
                print (f"[{i}] {item}")
                peralatan ()
def perbumbuan():
    if (len.bumbu) == 0 :
        bumbu_masuk = input ("Masukan bumbu yang ingin kamu tambahkan: ")
        bumbu.append(bumbu_masuk)
    else :
        for i in bumbu :
            print (i)    
def perbahanan():
    if (len.bahan)== 0 :
        bahan_masuk = input ("Masukan bahan yang ingin kamu tambahkan: ")
        bahan.append(bahan_masuk)
    else :
        for i in bahan :
            print (i)
def peralatan ():
    if len(alat) == 0 :
        alat_masuk= input ("Masukan alat yang ingin kamu tambahkan: ")
        alat.append(alat_masuk)
    else :
        for i in alat :
            print (i)
    
def progam_menu () :
    pilihan =input ("Mau masak apa hari ini ?\n atau belum ada ide memasak: ")
    if pilihan.lower == "ya":
        print ("Belum ada menu,silahkan buat menu baru")
        
    else : 
        menu.append(pilihan)
        print ("Menu Berhasil ditambahkan")
        for i ,item in enumerate (menu,start=1 ) :
            print (f"[{i}] {item}")
def progam_utama ():
    while True :
        for i,item in enumerate (utama,start= 1):
            print (f"[{i}] {item}") 
        print ("\n==PROGAM UTAMA ==")
        pilih_utama = int(input ("Mau ngapain nih hari ini: "))
        if pilih_utama == 1 :
            isi()
        elif pilih_utama == 2 :
            progam_menu()
        else : break

progam_utama ()
