import psycopg2
import os
import random
import time
from stdiomask import getpass
from colorama import init, Fore
import pandas as pd
from tabulate import tabulate
from PIL import Image, ImageDraw, ImageFont


# Inisialisasi Colorama untuk dukungan warna pada terminal
init(autoreset=True)

# Fungsi untuk membersihkan layar terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk menghubungkan ke database
def connect():
    return psycopg2.connect(
        database="project",
        user="postgres",
        password="010603",
        host="localhost",
        port="5432"
    )

def register():
    clear_screen()
    print(Fore.BLUE + "=== Registrasi Pengguna Baru ===")
    conn = connect()
    cur = conn.cursor()
    nama_pelanggan = input("Masukkan nama: ")
    alamat_pelanggan = input("Masukkan alamat: ")
    no_telfon = input("Masukkan No.Telpon: ")
    # id_pesanan = random.randint(1000, 9999)  # Menghasilkan id pesanan acak
    
    try:
        # Mengecek apakah nomor telepon sudah ada dalam database
        cur.execute(
            "SELECT no_telfon FROM data_pelanggan WHERE no_telfon = %s",
            (no_telfon,)
        )
        result = cur.fetchone()

        if result:
            print(Fore.RED + "Nomor telepon sudah terdaftar. Silakan gunakan nomor lain.")
            time.sleep(2)
        else:
            cur.execute(
                "INSERT INTO data_pelanggan (nama_pelanggan, alamat_pelanggan, no_telfon) VALUES (%s, %s, %s)",
                (nama_pelanggan, alamat_pelanggan, no_telfon)
            )
            conn.commit()
            print(Fore.GREEN + "Registrasi berhasil!")
            time.sleep(2)

    except psycopg2.Error as e:
        print(Fore.RED + f"Error: {e}")

    finally:
        cur.close()
        conn.close()
    main()

# Fungsi untuk login sebagai user
def login_user():
    clear_screen()
    print(Fore.CYAN + "\n=== Login User ===")
    no_telfon = input("Masukkan No.Telpon: ")

    conn = connect()
    cur = conn.cursor()

    try:
        attempt = 0
        while attempt < 2:
            cur.execute("SELECT * FROM data_pelanggan WHERE no_telfon = %s", (no_telfon,))
            user = cur.fetchone()

            if user:
                print(Fore.GREEN + "Login berhasil!")
                time.sleep(2)
                menu_user(user)
                return
            else:
                attempt += 1
                print(Fore.RED + f"Login gagal, percobaan ke-{attempt}. Silakan coba lagi.")

            no_telfon = input("Masukkan No.Telpon: ")

        print(Fore.RED + "Anda telah melebihi batas percobaan. Kembali ke menu utama.")
        time.sleep(2)
        main() 

    except psycopg2.Error as e:
        print(Fore.RED + f"Error: {e}")
    finally:
        cur.close()
        conn.close()
    return user

def get_data_from_db(jenis):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id_barang, nama_barang, harga_barang FROM barang WHERE jenis = %s", (jenis,))
        hasil = cursor.fetchall()
        return [{"id_barang": row[0], "nama_barang": row[1], "harga_baranag": row[2]} for row in hasil]
    except Exception as e:
        print(Fore.RED + f"Terjadi kesalahan: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

# Fungsi untuk memilih jenis barang
def pilih_barang(jenis):
    while True:
        clear_screen()
        print(Fore.CYAN + f"\n=== Pilih {jenis} ===")
        
        if jenis == "Router":
            pilihan_perangkat = [
                {"id": 1, "nama": "ONT_NOKIA_G-2425G-A", "harga": 200000, "stok": get_stok_barang(1)},
                {"id": 2, "nama": "ONT_ZTE_F670L", "harga": 200000, "stok": get_stok_barang(2)},
                {"id": 3, "nama": "ONT_FIBERHOME_HG6145F", "harga": 200000, "stok": get_stok_barang(3)},
                {"id": 4, "nama": "ONT_NOKIA_G240WL", "harga": 200000, "stok": get_stok_barang(4)}
            ]
        elif jenis == "Set Top Box":
            pilihan_perangkat = [
                {"id": 5, "nama": "ZTE_ZX10_B866F_V1.1", "harga": 150000, "stok": get_stok_barang(5)}
            ]
        else:
            print(Fore.RED + "Jenis barang tidak dikenal!")
            return None, 0

        for i, perangkat in enumerate(pilihan_perangkat, 1):
            print(f"{i}. {perangkat['nama']} - Harga: {perangkat['harga']} - Stok: {perangkat['stok']}")

        pilihan_barang = input(Fore.YELLOW + "Pilih barang: ")

        while True:
            try:
                pilihan_barang = int(pilihan_barang)
                if pilihan_barang <= len(pilihan_perangkat) and pilihan_barang > 0:
                    jumlah_barang = int(input(Fore.YELLOW + "Masukkan jumlah barang: "))
                    if jumlah_barang > 0 and jumlah_barang <= pilihan_perangkat[pilihan_barang - 1]['stok']:
                        return pilihan_perangkat[pilihan_barang - 1], jumlah_barang
                    elif jumlah_barang > pilihan_perangkat[pilihan_barang - 1]['stok']:
                        print(Fore.RED + f"Stok tidak cukup. Sisa stok: {pilihan_perangkat[pilihan_barang - 1]['stok']}")
                        input(Fore.YELLOW + "\nTekan Enter untuk kembali memilih jenis barang.")
                        break

                    else:
                        print(Fore.RED + "Jumlah barang harus lebih dari 0. Silakan masukkan lagi.")
                else:
                    print(Fore.RED + f"Pilihan barang tidak valid. Silakan masukkan angka di antara 1 dan {len(pilihan_perangkat)}")
                    time.sleep(2)
                    break  # Kembali ke loop luar untuk meminta pengguna memilih barang lagi
            except ValueError:
                print(Fore.RED + "Input tidak valid. Silakan masukkan angka.")

# Fungsi untuk mendapatkan stok barang berdasarkan id
def get_stok_barang(id_barang):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("SELECT stok_barang FROM barang WHERE id_barang = %s", (id_barang,))
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            return 0
    except psycopg2.Error as e:
        print(Fore.RED + f"Error: {e}")
        return 0
    finally:
        cur.close()
        conn.close()

# Fungsi untuk mengurangi stok barang setelah pembelian
def kurangi_stok_barang(id_barang, jumlah_barang):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("UPDATE barang SET stok_barang = stok_barang - %s WHERE id_barang = %s", (jumlah_barang, id_barang))
        conn.commit()
    except psycopg2.Error as e:
        print(Fore.RED + f"Error: {e}")
    finally:
        cur.close()
        conn.close()

# Fungsi untuk memilih metode pembayaran
def pilih_metode_pembayaran():
    clear_screen()
    print(Fore.CYAN + "\n=== Pilih Metode Pembayaran ===")
    metode_pembayaran = [
        {"nama": "Bank Mandiri", "id": 501},
        {"nama": "BRI", "id": 502},
        {"nama": "BNI", "id": 503},
        {"nama": "Dana", "id": 504}
    ]

    for i, metode in enumerate(metode_pembayaran, 1):
        print(f"{i}. {metode['nama']}")

    pilihan_metode = input(Fore.YELLOW + "Pilih metode pembayaran: ")
    return metode_pembayaran[int(pilihan_metode) - 1]

# Fungsi untuk menampilkan data dari tabel
def lihat_data():
    clear_screen()
    print(Fore.CYAN + "\n=== Lihat Data ===")
    print("1. Data Barang")
    print("2. Data Pelanggan")
    print("3. Detail Pesanan")
    pilihan = input(Fore.YELLOW + "Pilih opsi: ")

    conn = connect()
    cur = conn.cursor()

    try:
        if pilihan == "1":
            cur.execute("SELECT * FROM barang")
            rows = cur.fetchall()
            headers = [desc[0] for desc in cur.description]
            df = pd.DataFrame(rows, columns=headers)
            
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
        elif pilihan == "2":
            cur.execute("SELECT * FROM data_pelanggan")
            rows = cur.fetchall()
            headers = [desc[0] for desc in cur.description]
            df = pd.DataFrame(rows, columns=headers)
            
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
        elif pilihan == "3":
            cur.execute("SELECT * FROM detail_pesanan")
            rows = cur.fetchall()
            headers = [desc[0] for desc in cur.description]
            df = pd.DataFrame(rows, columns=headers)
            
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
        else:
            print(Fore.RED + "Pilihan tidak valid.")
            return

        input(Fore.YELLOW + "\nTekan Enter untuk kembali ke menu admin.")
        menu_admin()
    except psycopg2.Error as e:
        print(Fore.RED + f"Error: {e}")
    finally:
        cur.close()
        conn.close()
        
# Fungsi untuk mengupdate data
def update_data():
    clear_screen()
    print(Fore.CYAN + "\n=== Update Data ===")
    print("1. Update Data Barang")
    print("2. Update Data Pelanggan")
    print("3. Update Detail Pesanan")
    pilihan = input(Fore.YELLOW + "Pilih opsi: ")

    conn = connect()
    cur = conn.cursor()

    try:
        if pilihan == "1":
            id_barang = input(Fore.YELLOW + "Masukkan ID Barang: ")
            nama_barang = input(Fore.YELLOW + "Masukkan Nama Barang Baru: ")
            jenis_barang = input(Fore.YELLOW + "Masukkan Jenis Barang Baru: ")
            merk_barang = input(Fore.YELLOW + "Masukkan Merk Barang Baru: ")
            cur.execute("UPDATE barang SET nama_barang = %s, jenis_barang = %s, merk_barang = %s WHERE id_barang = %s",
                        (nama_barang, jenis_barang, merk_barang, id_barang))
            conn.commit()
            print(Fore.GREEN + "Data Barang berhasil diperbarui.")
        elif pilihan == "2":
            id_pelanggan = input(Fore.YELLOW + "Masukkan ID Pelanggan: ")
            nama_pelanggan = input(Fore.YELLOW + "Masukkan Nama Pelanggan Baru: ")
            alamat_pelanggan = input(Fore.YELLOW + "Masukkan Alamat Pelanggan Baru: ")
            no_telfon = input(Fore.YELLOW + "Masukkan No.Telfon Pelanggan Baru: ")
            cur.execute("UPDATE data_pelanggan SET nama_pelanggan = %s, alamat_pelanggan = %s , no_telfon = %s WHERE id_pelanggan = %s",
                        (nama_pelanggan, alamat_pelanggan, no_telfon, id_pelanggan))
            conn.commit()
            print(Fore.GREEN + "Data Pelanggan berhasil diperbarui.")
        elif pilihan == "3":
            id_pesanan = input(Fore.YELLOW + "Masukkan ID Pesanan: ")
            tanggal = input(Fore.YELLOW + "Masukkan Tanggal Transaksi Baru: ")
            jumlah_barang = input(Fore.YELLOW + "Masukkan Jumlah Barang Baru: ")
            id_barang = input(Fore.YELLOW + "Masukkan ID Barang Baru: ")
            id_pelanggan = input(Fore.YELLOW + "Masukkan ID Pelanggan Baru: ")
            id_metode = input(Fore.YELLOW + "Masukkan ID Metode Baru: ")
            cur.execute("UPDATE detail_pesanan SET tanggal = %s, jumlah_barang = %s, id_barang = %s, id_pelanggan = %s, id_metode = %s WHERE id_pesanan = %s",
                        (tanggal, jumlah_barang, id_barang, id_pelanggan, id_metode, id_pesanan))
            conn.commit()
            print(Fore.GREEN + "Detail Pesanan berhasil diperbarui.")
        else:
            print(Fore.RED + "Pilihan tidak valid.")
    except psycopg2.Error as e:
        print(Fore.RED + f"Error: {e}")
    finally:
        cur.close()
        conn.close()

    input(Fore.YELLOW + "\nTekan Enter untuk kembali ke menu admin.")
    menu_admin()

# Fungsi untuk menghapus data
def delete_data():
    clear_screen()
    print(Fore.CYAN + "\n=== Hapus Data ===")
    print("1. Hapus Stok Barang")
    print("2. Hapus Data Pelanggan")
    print("3. Hapus Detail Pesanan")
    pilihan = input(Fore.YELLOW + "Pilih opsi: ")

    conn = connect()
    cur = conn.cursor()

    try:
        if pilihan == "1":
            id_barang = input(Fore.YELLOW + "Masukkan ID Barang: ")
            cur.execute("UPDATE barang SET stok_barang = 0 WHERE id_barang = %s", (id_barang,))
            conn.commit()
            print(Fore.GREEN + "Stok Barang berhasil dihapus menjadi 0.")
        elif pilihan == "2":
            id_pelanggan = input(Fore.YELLOW + "Masukkan ID Pelanggan: ")
            cur.execute("DELETE FROM data_pelanggan WHERE id_pelanggan = %s", (id_pelanggan,))
            conn.commit()
            print(Fore.GREEN + "Data Pelanggan berhasil dihapus.")
        elif pilihan == "3":
            id_pesanan = input(Fore.YELLOW + "Masukkan ID Pesanan: ")
            cur.execute("DELETE FROM detail_pesanan WHERE id_pesanan = %s", (id_pesanan,))
            conn.commit()
            print(Fore.GREEN + "Detail Pesanan berhasil dihapus.")
        else:
            print(Fore.RED + "Pilihan tidak valid.")
    except psycopg2.Error as e:
        print(Fore.RED + f"Error: {e}")
    finally:
        cur.close()
        conn.close()

    input(Fore.YELLOW + "\nTekan Enter untuk kembali ke menu admin.")
    menu_admin()

# Fungsi untuk memperbarui status pembayaran
def update_status_pembayaran():
    clear_screen()
    print(Fore.CYAN + "\n=== Update Status Pembayaran ===")
    id = input(Fore.YELLOW + "Masukkan ID Pelanggan: ")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute("UPDATE data_pelanggan SET status_pembayaran = 'LUNAS' WHERE id_pelanggan = %s", (id,))
        conn.commit()
        print(Fore.GREEN + "Status Pembayaran berhasil diperbarui menjadi 'LUNAS'.")
    except psycopg2.Error as e:
        print(Fore.RED + f"Error: {e}")
    finally:
        cur.close()
        conn.close()

    input(Fore.YELLOW + "\nTekan Enter untuk kembali ke menu admin.")
    menu_admin()

# Fungsi menambah stok barang
def tambah_stok_barang():
    clear_screen()
    print(Fore.CYAN + "\n=== Tambah Stok Barang ===")
    id_barang = input(Fore.YELLOW + "Masukkan ID Barang: ")
    tambahan_stok = input(Fore.YELLOW + "Masukkan Jumlah Stok Tambahan: ")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute("UPDATE barang SET stok_barang = stok_barang + %s WHERE id_barang = %s", (tambahan_stok, id_barang))
        conn.commit()
        print(Fore.GREEN + f"Stok Barang berhasil ditambahkan sebanyak {tambahan_stok}.")
    except psycopg2.Error as e:
        print(Fore.RED + f"Error: {e}")
    finally:
        cur.close()
        conn.close()

    input(Fore.YELLOW + "\nTekan Enter untuk kembali ke menu admin.")
    menu_admin()

# Fungsi untuk login sebagai admin
def login_admin():
    clear_screen()
    print(Fore.CYAN + "\n=== Login Admin ===")
    nama_admin = input("Masukkan Nama Admin: ")
    password_pegawai= getpass("Masukkan Password: ")

    conn = connect()
    cur = conn.cursor()

    try:
        attempt = 0
        while attempt < 2:
            cur.execute("SELECT * FROM admin WHERE nama_admin = %s AND password_pegawai = %s", (nama_admin, password_pegawai))
            admin = cur.fetchone()

            if admin:
                print(Fore.GREEN + "Login berhasil!")
                time.sleep(2) 
                menu_admin()
                return
            else:
                attempt += 1
                print(Fore.RED + f"Login gagal, percobaan ke-{attempt}. Silakan coba lagi.")

            nama_admin = input("Masukkan Nama Admin: ")
            password_pegawai = getpass("Masukkan Password: ")

        print(Fore.RED + "Anda telah melebihi batas percobaan. Kembali ke menu utama.")
        time.sleep(2) 
        main()

    except psycopg2.Error as e:
        print(Fore.RED + f"Error: {e}")
    finally:
        cur.close()
        conn.close()

# Fungsi untuk menyimpan detail pesanan ke database
def simpan_detail_pesanan(id_pesanan, tanggal, jumlah_barang, id_barang, id_pelanggan, id_metode):
    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO detail_pesanan (id_pesanan, tanggal, jumlah_barang, id_barang, id_pelanggan, id_metode) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (id_pesanan, tanggal, jumlah_barang, id_barang, id_pelanggan, id_metode)
        )
        conn.commit()
        print(Fore.GREEN + "Detail pesanan berhasil disimpan.")
    except psycopg2.Error as e:
        print(Fore.RED + f"Error: {e}")
    finally:
        cur.close()
        conn.close()

# Fungsi data_pelanggan
def get_pelanggan_details(id_pelanggan):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("SELECT nama_pelanggan, alamat_pelanggan FROM data_pelanggan WHERE id_pelanggan = %s", (id_pelanggan,))
        return cur.fetchone()
    except psycopg2.Error as e:
        print(Fore.RED + f"Error: {e}")
        return None
    finally:
        cur.close()
        conn.close()

# Fungsi menu user
def menu_user(getid):
    clear_screen()
    print(Fore.CYAN + "\n=== Menu User ===")
    print("1. Router")
    print("2. Set Top Box")
    pilihan_user = input(Fore.YELLOW + "Pilih opsi: ")

    if pilihan_user == "1":
        jenis_barang = "Router"
    elif pilihan_user == "2":
        jenis_barang = "Set Top Box"
    else:
        print(Fore.RED + "Pilihan tidak valid.")
        return

    barang, total_pesanan = pilih_barang(jenis_barang)
    if barang is None:
        return

    metode_pembayaran = pilih_metode_pembayaran()

    harga_barang = barang['harga']
    biaya_pemasangan = 200000
    total_harga = (harga_barang * total_pesanan) + biaya_pemasangan

    print(Fore.GREEN + f"\nAnda telah memilih {total_pesanan} {jenis_barang} {barang['nama']}")
    print(Fore.GREEN + f"Metode pembayaran: {metode_pembayaran['nama']}")
    print(Fore.GREEN + f"Total Harga: {total_harga}")

    id_pesanan = random.randint(1000, 9999)
    id_pelanggan = getid[0]

    pelanggan_details = get_pelanggan_details(id_pelanggan)
    if pelanggan_details:
        nama_pelanggan, alamat_pelanggan = pelanggan_details
        simpan_detail_pesanan(id_pesanan, tanggal, id_pelanggan, barang['id'], id_pelanggan, metode_pembayaran['id'])
        kurangi_stok_barang(barang['id'], total_pesanan)
        generate_receipt(tanggal, nama_pelanggan, alamat_pelanggan, barang['nama'], total_pesanan, harga_barang, total_harga)
    else:
        print(Fore.RED + "Gagal mendapatkan detail pelanggan.")

def get_random_technician():
    conn = connect()
    cur = conn.cursor()
    try :
        # Mengambil semua nama dan nomor telepon teknisi dari tabel teknisi
        cur.execute("SELECT nama_teknisi, no_telfon FROM teknisi")
        teknisi_list = cur.fetchall()
        
        teknisi = random.choice(teknisi_list)
        nama_teknisi = teknisi[0]
        no_telfon_teknisi = teknisi[1]
        
        return nama_teknisi, no_telfon_teknisi
    
    except (Exception, psycopg2.Error) as error:
        print("Gagal Memuat Data!", error)
    finally:
        if conn:
            cur.close()
            conn.close()

def generate_receipt(nama_pelanggan, alamat_pelanggan, nama_barang, total_pesanan, harga_per_item, total_harga):
    # Mendapatkan nama teknisi secara acak dari database sekaligus nomor teleponnya 
    nama_teknisi, no_telfon_teknisi = get_random_technician()
    
    width, height = 600, 400
    receipt_img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(receipt_img)

    font = ImageFont.load_default()

    text_lines = [
        "Telkom Kebonsari Jember",
        "Jl. Letjend Suprapto No.70, Kebonsari, Kec. Sumbersari, Jember, Jawa Timur 68122",
        "(0331) 337799", 
        "----------------------------",
        f"Nama Pelanggan    : {nama_pelanggan}",
        f"Alamat            : {alamat_pelanggan}",
        "----------------------------",
        f"Nama Barang       : {nama_barang}",
        f"Jumlah Barang     : {total_pesanan}",
        f"Harga Barang      : Rp.{harga_per_item}",
        "Biaya Pemasangan   : Rp.200000",
        f"Total Harga       : Rp.{total_harga}",
        "----------------------------",
        f"Teknisi           : {nama_teknisi}",
        f"No Telp           : {no_telfon_teknisi}"
    ]

    y_text = 10
    for line in text_lines:
        draw.text((10, y_text), line, font=font, fill=(0, 0, 0))
        y_text += 20

    receipt_img.show()

# Fungsi menu admin
def menu_admin():
    clear_screen()
    print(Fore.CYAN + "\n=== Menu Admin ===")
    print("1. Lihat Data")
    print("2. Update Data")
    print("3. Hapus Data")
    print("4. Update Status Pembayaran")
    print("5. Tambah Stok Barang")
    pilihan = input(Fore.YELLOW + "Pilih opsi: ")

    if pilihan == "1":
        lihat_data()
    elif pilihan == "2":
        update_data()
    elif pilihan == "3":
        delete_data()
    elif pilihan == "4":
        update_status_pembayaran()
    elif pilihan == "5":
        tambah_stok_barang()
    else:
        print(Fore.RED + "Pilihan tidak valid.")

# Fungsi utama setelah login
def after_login():
    clear_screen()
    print(Fore.CYAN + "\n=== Login ===")
    print("1. Admin")
    print("2. User")
    role_choice = input(Fore.YELLOW + "Pilih role: ")

    if role_choice == "1":
        login_admin()
    elif role_choice == "2":
        login_user()
    else:
        print(Fore.RED + "Pilihan tidak valid.")

# Main program
def main():
    clear_screen()
    print("Menu Utama:")
    print("1. " + Fore.GREEN + "Register")
    print("2. " + Fore.GREEN + "Login")
    choice = input(Fore.YELLOW + "Pilih opsi: ")

    if choice == "1":
        register()
    elif choice == "2":
        after_login()
    else:
        print(Fore.RED + "Pilihan tidak valid.")

if __name__ == "__main__":
    main()