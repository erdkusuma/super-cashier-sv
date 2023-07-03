"""
Modul untuk menjalankan interface aplikasi "Super-Cashier berbasis self-service" 
dengan menampilkan fitur aplikasi dalam bentuk daftar menu.
"""

from tabulate import tabulate
from transaction import Transaction

def main():
    transaction = Transaction()
    while True:
        print("\n=== Super-Cashier Service ===")
        print("1. Tambah Item")
        print("2. Ubah Item")
        print("3. Hapus Item")
        print("4. Reset Transaksi")
        print("5. Cek Total Belanja & Diskon")
        print("6. Keluar")

        try:
            choice = int(input("Masukkan pilihan (1-6): "))
        except ValueError:
            print("--------------------------------------")
            print("Pilihan tidak valid. Masukkan angka 1-6.")
            print("--------------------------------------")
            continue

        if choice == 1:
            name = input("Nama Item: ")
            qty = input("Jumlah Item: ")
            price = input("Harga Item: ")
            transaction.add_item(name, qty, price)
        elif choice == 2:
            if not transaction.cart:
                print("-----------------------------")
                print("Keranjang belanja masih kosong")
                print("-----------------------------")
                continue

            else:
                while True:
                    print("\n=== Menu Ubah ===")
                    print("1. Ubah Nama Item")
                    print("2. Ubah Jumlah Item")
                    print("3. Ubah Harga Item")
                    print("4. Kembali")
                    try:
                        sub_choice = int(input("Masukkan pilihan (1-4): "))
                    except ValueError:
                        print("--------------------------------------")
                        print("Pilihan tidak valid. Masukkan angka 1-4.")
                        print("--------------------------------------")
                        continue
                    
                    if sub_choice == 1:
                        name = input("Nama item yang ingin diubah: ")
                        name_update = input("Nama baru item: ")
                        transaction.update_item_name(name, name_update)
                        break
                    elif sub_choice == 2:
                        name = input("Nama item yang ingin diubah jumlahnya: ")
                        qty_update = int(input("Jumlah baru item: "))
                        transaction.update_item_qty(name, qty_update)
                        break
                    elif sub_choice == 3:
                        name = input("Nama item yang ingin diubah harganya: ")
                        price_update = float(input("Harga baru item: "))
                        transaction.update_item_price(name, price_update)
                        break
                    elif sub_choice == 4:
                        break
                    else:
                        print("--------------------------------------")
                        print("Pilihan tidak valid. Masukkan angka 1-4.")
                        print("--------------------------------------")

        elif choice == 3:
            if not transaction.cart:
                print("-----------------------------")
                print("Keranjang belanja masih kosong")
                print("-----------------------------")
                continue
            else:
                name = input("Nama item yang ingin dihapus: ")
                transaction.delete_item(name)
        elif choice == 4:
            transaction.reset_transaction()             
        elif choice == 5:
            transaction.check_order()
            transaction.total_price()
        elif choice == 6:
            break
        else:
            print("--------------------------------------")
            print("Pilihan tidak valid. Masukkan angka 1-6.")
            print("--------------------------------------")

main()