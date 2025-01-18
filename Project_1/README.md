#Warung Sederhana & Game Tebak-Tebakan

#Proyek ini terdiri dari dua fitur utama:
-Warung Sederhana: Program untuk menambah dan mengecek barang dalam warung sederhana. Barang disimpan dalam database MySQL yang dikelola melalui XAMPP.
-Game Tebak-Tebakan: Sebuah permainan di mana pemain memilih salah satu dari empat kotak untuk menemukan hadiah.

#Prasyarat
Sebelum menjalankan aplikasi ini, Anda memerlukan beberapa hal:
-XAMPP: Untuk menjalankan server web Apache dan database MySQL secara lokal.
-Python 3.x: Untuk menjalankan skrip aplikasi.
-Library Python: Anda membutuhkan beberapa library Python untuk menjalankan proyek ini, seperti mysql-connector dan random.

#Instalasi
-Install XAMPP (Jika belum terinstal):
Unduh dan instal XAMPP dari situs resmi XAMPP.
Setelah terinstal, buka aplikasi XAMPP Control Panel.
Jalankan Apache dan MySQL dari XAMPP Control Panel.

-Install Python dan Library:
Pastikan Python 3.x sudah terinstal di komputer Anda.

-Install library mysql-connector dengan menjalankan perintah berikut di terminal/command prompt:
pip install mysql-connector

#Membuat Database di MySQL:
-Buka phpMyAdmin dengan mengakses http://localhost/phpmyadmin di browser.
-Buat database baru dengan nama warung.
-Buat tabel product di dalam database warung dengan query berikut:
CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kode_barang VARCHAR(50) NOT NULL,
    nama_barang VARCHAR(100) NOT NULL,
    harga_barang DECIMAL(10, 2) NOT NULL,
    stok_barang INT NOT NULL
);

#Menjalankan Program:
Pastikan sudah menginstal XAMPP dan sudah mengaktifkan APACHE dan MYSQL
Pertama buka folder ini di VS CODE dan buka terminal kemudian ketik py main.py untuk menjalankan program ini 

#Fitur Program
1. Warung Sederhana
Fitur ini memungkinkan Anda untuk:
Menambah barang ke dalam daftar barang dengan memasukkan kode, nama, harga, dan stok barang.
Mengecek barang yang ada di dalam daftar.
2. Game Tebak-Tebakan
Fitur ini adalah permainan di mana Anda harus memilih salah satu dari empat kotak. Salah satu kotak berisi hadiah, dan Anda harus menebak kotak mana yang benar. Pemain dapat memilih untuk bermain lagi setelah permainan selesai.

#Alur Program
-Menu Utama: Saat menjalankan program, Anda akan diberikan pilihan antara:
-Game Tebak-Tebakan: Memulai permainan di mana Anda memilih kotak untuk menemukan hadiah.
-Warung: Mengakses program warung untuk menambah atau mengecek barang.
-Hentikan Program: Menghentikan program dengan countdown.

#Fungsi dalam Program:
-libs.py: Fungsi untuk menyapa pengguna dengan nama komputer mereka dan untuk menghentikan program dengan countdown.
-games.py: Menangani permainan tebak-tebakan.
-market.py: Menangani fitur warung sederhana, termasuk menambah barang dan menampilkan barang yang ada.
-main.py: Mengatur alur program, memberikan pilihan kepada pengguna.

#Menjalankan program:
Setelah Anda menjalankan program, berikut adalah alur interaksi pengguna:
-Pilihan Menu: Program akan meminta Anda untuk memilih antara:
-Game Tebak-Tebakan: Anda akan diberikan empat kotak yang berisi simbol berbeda. Pilih salah satu kotak, dan sistem akan memberi tahu apakah pilihan Anda benar atau salah.
-Warung: Anda dapat menambah barang baru atau mengecek daftar barang yang ada dalam warung. Data barang disimpan dalam database MySQL yang dikelola melalui XAMPP.
-Hentikan Program: Menghentikan program.