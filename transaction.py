"""
Modul yang memuat metode pemrosesan transaksi dan 
keranjang belanja berdasarkan data masukan dari Customer.
"""
import uuid
from tabulate import tabulate
from item import Item
    
        
class Transaction:
    def __init__(self):
        """
        Menginisialisasi ID transaksi dengan karakter unik dan acak yang memanfaatkan library uuid.
        Menginisialisasi keranjang belanja (cart) dalam bentuk list.
        """
        self.transaction_id = "TR-"+ str(uuid.uuid4())
        self.cart = []
    
    #ADD
    def add_item(self, name, qty, price):
        """
        Metode menambah item ke keranjang belanja.
        
        Parameter:
            name(str): nama item
            qty(int): jumlah item
            price(float): harga item
        
        Parameter nama item disimpan dalam format 'title case' 
        untuk keperluan tampilan daftar order serta validasi perintah update-delete. 
        
        Setelah selesai menambahkan item, akan menampilkan isi keranjang beserta subtotal masing-masing item. 
        """
        try:
            qty = int(qty)
            price = float(price)
            if qty < 1 or price < 0:
                raise ValueError
        except ValueError:
            print("------------------------------------------------")
            print("Jumlah atau harga yang Anda masukkan tidak valid")
            print("------------------------------------------------")
            return
        
        item = Item(name.title(), qty, price)
        self.cart.append(item)
        self.check_order()
      
    
    #UPDATE
    def update_item_name(self, name, name_update):
        """
        Metode memperbarui nama item di keranjang belanja.
        
        Parameter:
            name(str): nama item yang ingin diperbarui
            name_update(str): nama item yang baru
        
        Kondisi: 
            Jika nama item yang dimasukkan salah ketik atau tidak ada di keranjang belanja, 
            maka muncul pesan bahwa nama item tidak ditemukan di keranjang. 
        """
        for item in self.cart:
            if item.name == name.title():
                item.name = name_update.title()
                self.check_order()
                return
        print("------------------------------------------------")    
        print(f"{name} tidak ditemukan dalam keranjang belanja.") 
        print("------------------------------------------------")
        
    
   
    def update_item_qty(self, name, qty_update):
        """
        Metode memperbarui jumlah item di keranjang belanja.
        
        Parameter:
            name(str): nama item yang jumlahnya ingin diubah
            qty_update(int): jumlah item yang baru
        
        Kondisi: 
            Jika nama item yang dimasukkan salah ketik atau tidak ada di keranjang belanja, 
            maka muncul pesan bahwa nama item tidak ditemukan di keranjang.         
        """

        try:
            qty_update = int(qty_update)
            if qty_update < 1:
                raise ValueError
        except ValueError:
            print("-------------------------------------")    
            print("Jumlah yang Anda masukkan tidak valid")
            print("-------------------------------------") 
            return
        
        for item in self.cart:
            if item.name == name.title():
                item.qty = qty_update
                self.check_order() 
                return
        print("------------------------------------------------")
        print(f"{name} tidak ditemukan dalam keranjang belanja.") 
        print("------------------------------------------------")
        
    
    def update_item_price(self, name, price_update):
        """
        Metode memperbarui harga item di keranjang belanja.
        
        Parameter:
            name(str): nama item yang harganya ingin diperbarui
            price_update(float): harga item yang baru
        
        Kondisi: 
            Jika nama item yang dimasukkan salah ketik atau tidak ada di keranjang belanja, 
            maka muncul pesan bahwa nama item tidak ditemukan di keranjang. 
        """
        try:
            price_update = float(price_update)
            if price_update < 1:
                raise ValueError
        except ValueError:
            print("------------------------------------")    
            print("Harga yang Anda masukkan tidak valid")
            print("------------------------------------") 
            return
        
        for item in self.cart:
            if item.name == name.title():
                item.price = int(price_update)
                self.check_order() 
                return
                
        print("------------------------------------------------")
        print(f"{name} tidak ditemukan dalam keranjang belanja.")
        print("------------------------------------------------")


    
    #DELETE
    def delete_item(self, name):
        """
        Metode menghapus satu item dari keranjang belanja.
        
        Parameter:
            name(str): nama item yang ingin dikeluarkan dari keranjang belanja.
        
        Kondisi: 
            Jika nama item yang dimasukkan salah ketik atau tidak ada di keranjang belanja, 
            maka muncul pesan bahwa nama item tidak ditemukan di keranjang.  

        Memunculkan pesan ketika item berhasil dihapus.         
        """

        for item in self.cart:
            if item.name == name.title():
                self.cart.remove(item)
                
                print("------------------------------")
                print(f"{item.name} berhasil dihapus!")
                print("------------------------------")
                self.check_order()
                return
        
        print("------------------------------------------------")
        print(f"{name} tidak ditemukan dalam keranjang belanja.")
        print("------------------------------------------------")
    

    #RESET
    def reset_transaction(self):
        """
        Metode menghapus (reset) seluruh transaksi.
        Menampilkan pesan jika reset berhasil dilakukan.
        """
        self.cart = []
        self.total = 0
        print("-------------------------------------------")
        print("Semua item berhasil dihapus dari keranjang!")
        print("-------------------------------------------")

        

    #CALCULATE
    def total_price(self):
        """
        Metode menghitung besaran diskon yang diberikan dan total harga belanjaan setelah dikurangi diskon.
        
        Kondisi: 
            - Jika keranjang tidak kosong maka berlakukan ketentuan berikut: 
                - Jika total belanja lebih besar dari 500_000 maka diskon yang didapat 10%
                - Jika total belanja lebih besar dari 300_000 maka diskon yang didapat 8%
                - Jika total belanja lebih besar dari 200_000 maka diskon yang didapat 5%
                - Jika total belanja di bawah dari 200_000 maka tidak mendapat diskon  
        """

        if self.cart:
            self.total=0
            for item in self.cart:
                self.total += item.qty * item.price

            if self.total > 500_000:
                discount = 0.10*self.total
            elif self.total > 300_000:
                discount = 0.08*self.total
            elif self.total > 200_000:
                discount = 0.05*self.total
            else:
                discount = 0

            total_after_discount = self.total - discount

            print(f"Total belanja: Rp{self.total:.2f}")
            print(f"Diskon: Rp{discount:.2f}")
            print(f"Total setelah diskon: Rp{total_after_discount:.2f}")
            print(f"\nID transaksi: {self.transaction_id}")       

    
    
    #CHECK ALL ORDER           
    def check_order(self):
        """
        Metode untuk menampilkan seluruh daftar item yang ada di keranjang belanja dalam bentuk tabel.

        Library: Tabulate. 
        
        """
        
        if not self.cart:
            print("------------------------------")
            print("Keranjang belanja masih kosong")
            print("------------------------------")
        
        else:
            print("\n==============   Super-Cashier Service  ==============")
            cart_table = [[i+1, item.name, item.qty, item.price, item.qty * item.price] for i, item in enumerate(self.cart)]
            headers = ["No","Nama Item", "Jumlah", "Harga", "Subtotal"]
            table = tabulate(cart_table, headers, tablefmt="grid")
            print(table)
        
       
                   
    