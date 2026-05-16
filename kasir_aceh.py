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
makanan = ['Mie Aceh Original','Mie Aceh Telur','Mie Aceh Daging','Mie Aceh Udang','Mie Aceh Special']
minuman = ['Es Teh','Teh Hangat','Es Sirup','Es Timun Serut','Teh Tarek Dingin','Teh Tarek Panas','Kopi aceh','Es Capucino','Es Nutrisari Jeruk','Es Jeruk']
jajan = ['Sosis Solo','Risol Mayo','Piscok','Tamalada']
Harga_makan = ['10000',
Harga_minum = []
Harga_jajan = []
def tampilan_utama ():
    print ("[1] Menu makanan")
    print ("[2] Menu Minuman")
    print ("[3] Menu Snack & Tambahan")
def makan () :
    while True :
        print ()
        
def minum () :
def snack () :



while True :
    tampilan_utama()
    gerbang = int(input("Mau masuk ke Menu Apa ? (Pilih nomornya)"))
    if gerbang == 1 :
        makan()
    elif gerbang == 2 :
        minum()
    elif gerbang == 3 :
        snack ()
    else :
        print ('Maaf tidak pilihan tersebut , tolong masukan angka yang tersedia')
