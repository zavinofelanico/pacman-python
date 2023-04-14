#!/usr/bin/env python
# coding: utf-8

# In[1]:


from modul import Transaction


# In[2]:


def menu(opt):
    ''' 
    Fungsi untuk menampilkan daftar menu
        
    parameters
    opt : hasil instance class  
    '''

    print("<-----------------Selamat Datang di Aplikasi Super Kasir----------------->")
    while (True):
          try:
              id_transaksi = int(input("Masukkan ID Transaksi anda: "))
              print("ID Transaksi anda {}".format(id_transaksi))
              print("\n")
              break
          except ValueError:
              print("ID Transaksi tidak valid!")
              continue
    
    print("<-----------------------Super Kasir--------------->")
    print("Selamat datang, ID Transaksi Anda {}".format(id_transaksi))
    print("<------------------------------------------------->")   
    print("\n Menu: ")
    print("1. Menambahkan Item")
    print("2. Mengubah Nama Item")
    print("3. Mengubah Jumlah Item")
    print("4. Mengubah Harga Item")
    print("5. Menghapus Item")
    print("6. Reset Pesanan")
    print("7. Memeriksa Pesanan")
    print("8. Total Harga")
    print("9. Keluar")
    print("")
    print("<------------------------------------------------->")    
    # Input menu yang dipilih
    option = int(input("Masukkan Pilihan Anda: "))
        
    if option == 1:
        # Input nama item yang dipesan
        nama_item = input("Masukkan Nama Item yang Ingin Dipesan: ")
        
        # Looping sampai jumlah item yang diinput berupa angka
        while(True):
            try:
                # Input jumlah dari item yang dipesan
                jumlah_item = int(input("Masukkan Jumlah Item yang Ingin Dipesan: "))
            except ValueError:
                print("Harus Berupa Angka!")
            else:
                break
                
        # Looping sampai harga item yang diinput berupa angka        
        while(True):
            try:
                # Input harga dari item yang dipesan
                harga_item = int(input("Masukkan Harga Item yang Ingin Dipesan: "))
            except ValueError:
                print("Harus Berupa Angka!")
            else:
                break
                
        # Memanggil method di class Transaction        
        opt.add_item(nama_item, jumlah_item, harga_item)
        
        # Kembali ke menu
        menu(opt)
            
    elif option == 2:
        # Input nama item yang akan diperbarui
        nama_item = input("Masukkan Nama Item yang Ingin Diubah: ")
        
        # Input nama item baru
        nama_baru = input("Masukkan Nama Baru: ")
        
        # Memanggil method di class Transaction      
        opt.update_item_name(nama_item, nama_baru)
        
        # Kembali ke menu
        menu(opt)
            
    elif option == 3:
        # Input nama item
        nama_item = input("Masukkan Nama Item: ")
        
        # Looping sampai jumlah item yang diinput berupa angka
        while(True):
            try:
                # Input jumlah baru
                jumlah_baru = int(input("Masukkan Jumlah Baru: "))
            except ValueError:
                    print("Harus Berupa Angka!")
            else:
                break
        
        # Memanggil method di class Transaction         
        opt.update_item_qty(nama_item, jumlah_baru)
        
        # Kembali ke menu
        menu(opt)
            
    elif option == 4:
        # Input nama item
        nama_item = input("Masukkan Nama Item: ")
        
        # Looping sampai harga item yang diinput berupa angka 
        while(True):
            try:
                # Input harga baru
                harga_baru = int(input("Masukkan Harga Baru: "))
            except ValueError:
                print("Harus Berupa Angka!")
            else:
                break
                
        # Memanggil method di class Transaction  
        opt.update_item_price(nama_item, harga_baru)
        
        # Kembali ke menu
        menu(opt)
            
    elif option == 5:
        # Input nama item yang akan dihapus
        nama_item = input("Masukkan Nama Item yang Ingin Dihapus: ")
        
        # Memanggil method di class Transaction
        opt.delete_item(nama_item)
        
        # Kembali ke menu
        menu(opt)
            
    elif option == 6:
        # Memanggil method di class Transaction
        opt.reset_transaction()
        
        # Kembali ke menu
        menu(opt)
            
    elif option == 7:
        # Memanggil method di class Transaction
        opt.check_order()
        
        # Kembali ke menu
        menu(opt)
            
    elif option == 8:
        # Memanggil method di class Transaction
        opt.total_price()
        
        # Kembali ke menu
        menu(opt)
            
    elif option == 9:
        print("")
        print("Terima Kasih")
        print("")
        pass
        
    else:
        print("Inputan Anda Salah!")
        menu(opt)


# In[3]:


trans = Transaction()


# In[ ]:

menu(trans)