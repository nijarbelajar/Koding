def sapa (nama):
    print (f"Selamat Pagi {nama}. Jangan lupa ngopi sebelum koding!!")
sapa ('yoyok')

def sisa (full,pakai) :
    jumlah = full - pakai 
    return jumlah 
print (sisa(10,1.1))

def absen (masuk) :
    if masuk <= 7 :
        print ("Kamu Tepat Waktu")
    elif masuk > 7 :
        print ("Kamu Terlambat")
absen (7)