list = ["Menu","setting","keluar"]
daftar =["Menu 1","Menu 2","Menu 3"]
setting_list = ["Setting 1","Setting 2","Setting 3"]
def menu(): 
    print("Anda memilih menu")
    for i ,item in enumerate(daftar,start=1):
        print(f"{i}. {item}")
    menu_pilihan = int(input("Masukkan pilihan menu (1-3): "))
    if menu_pilihan == 1:
        print("Anda memilih Menu 1")
    elif menu_pilihan == 2:
        print("Anda memilih Menu 2")
    elif menu_pilihan == 3:
        print("Anda memilih Menu 3")
    else:
        print("Pilihan tidak valid")

def setting(): 
    print("Anda memilih setting")
    for i ,item in enumerate(setting_list,start=1):
        print(f"{i}. {item}")
    setting_pilihan = int(input("Masukkan pilihan setting (1-3): "))
    if setting_pilihan == 1:
        print("Anda memilih Setting 1")
    elif setting_pilihan == 2:
        print("Anda memilih Setting 2")
    elif setting_pilihan == 3:
        print("Anda memilih Setting 3")
    else:
        print("Pilihan tidak valid")

def keluar(): 
    print("Anda memilih keluar")






while True :
    for i,item in enumerate(list,start=1):
        print(f"{i}. {item}")
    pilihan = int(input("Masukkan pilihan (1-3): "))
    if pilihan == 1:
        menu()
    elif pilihan == 2:
        setting()
    elif pilihan == 3:
        keluar()
        break
    else:
        print("Pilihan tidak valid")
