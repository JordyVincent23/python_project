import main
from services import db

def add():
    kode_barang = input('kode barang: ')
    nama_barang = input('nama barang: ')
    harga_barang = int(input('harga barang: '))
    stok_barang = input('stok barang: ')
    
    db.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)
    
def cek():
    items = db.fetch_item()
    for item in items:
        kode_barang = item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stok_barang = item[4]
        print(f'''
kode: {kode_barang}
{nama_barang} [{harga_barang}]
stok: {stok_barang}
''')

def start():
    while True:
        menu = int(input('Menu:\n1.Tambah barang\n2.Cek barang\n3.Kembali\nSilahkan dipilih: '))
        
        if menu == 1:
            add()
        elif menu == 2:
            cek()
        elif menu == 3:
            main.option()
        else:
            break
        
if __name__ == '__main__':
    print('ini warung')