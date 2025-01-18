import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'warung'
)

def insert_item(kode_barang, nama_barang, harga_barang, stok_barang):
    cursor = db.cursor()
    cursor.execute("INSERT INTO product (kode_barang, nama_barang, harga_barang, stok_barang) VALUES (%s, %s, %s, %s)", (kode_barang, nama_barang, harga_barang, stok_barang))
    db.commit()
    if cursor.rowcount > 0:
        print('\ndata berhasil disimpan\n')
    else:
        print('\ndata gagal disimpan\n')
        
def fetch_item():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM product')
    return cursor.fetchall()