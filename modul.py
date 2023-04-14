#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[18]:


class Transaction:
    '''
    Sebuah class untuk aplikasi kasir self-service di supermarket
    ...
    Attributes
    ----------
    id_transaksi : int
        id_transaksi berjenis input untuk hasil transaksi customer
    data_all_item : dict
        data_all_item adalah tempat penyimpanan data order transaksi yang berhasil diinput oleh customer kedalam sistem
    '''

    def __init__(self):
        '''
        Fungsi inisialisasi untuk class Transaction
        Parameters
        ----------
        Tidak terdapat parameter pada fungsi Constructor
        Attributes
        ----------
        id_transaksi : int
            id_transaksi berjenis input untuk hasil transaksi customer
        '''
        
        self.data_order = dict()
    
        
    def add_item(self, nama_item, jumlah_item, harga_item):
        '''
        fungsi menambahkan item belanja
        
        parameters
        nama_item   : str   item yang ingin dipesan
        jumlah_item : int   jumlah dari item yang dipesan
        harga_item  : int   harga dari item yang dipesan
        
        return tabel pesanan
        '''     
        # Menambahkan data ke dalam dictionary
        self.data_order.update({nama_item: [jumlah_item, harga_item, (jumlah_item * harga_item)]})
        
        #Menampilkan list item yang dipesan
        return self.check_order()
        
    def update_item_name(self, nama_item, nama_baru):
        '''
        fungsi mengubah nama item yang sudah diinput
        
        parameters
        nama_item   : str   nama item yang ingin diubah
        nama_baru   : str   nama item yang baru
        
        return tabel pesanan
        '''
        # Update nama item yang ada di library (data_order)
        temp = self.data_order[nama_item]
        try:
            self.data_order.pop(nama_item)
            self.data_order.update({nama_baru: temp})
            
            # Menampilkan list item yang telah diperbarui
            return self.check_order()
        except:
            raise exception ("Nama Item Tidak Sesuai")
            
    def update_item_qty(self, nama_item, jumlah_baru):
        '''
        fungsi mengubah jumlah item yang sudah diinput
        
        
        parameters
        nama_item   : str   nama item dari jumlah yang ingin diperbarui
        jumlah_baru   : int   jumlah item yang baru
        
        return tabel pesanan
        '''
        # Update jumlah item yang ada di library (data_order)
        try:
            self.data_order[nama_item][0] = jumlah_baru
            
            # Update total harga yang ada di library (data_order)
            self.data_order[nama_item][2] = jumlah_baru * self.data_order[nama_item][1]
            
            # Menampilkan list item yang telah diperbarui
            return self.check_order()
        except:
            raise exception ("Nama Item Tidak Sesuai")
            
    def update_item_price(self, nama_item, harga_baru):
        '''
        fungsi mengubah harga item yang sudah diinput
        
        parameters
        nama_item   : str   nama item dari harga yang ingin diperbarui
        harga_baru   : int   harga item yang baru
        
        return tabel pesanan
        '''
        # Update harga item yang ada di library (data_order)
        try:
            self.data_order[nama_item][1] = harga_baru
            
            # Update total harga yang ada di library (data_order)
            self.data_order[nama_item][2] = harga_baru * self.data_order[nama_item][0]
            
            # Menampilkan list item yang telah diperbarui
            return self.check_order()
        except:
            raise exception ("Nama Item Tidak Sesuai")
            
    def delete_item(self, nama_item):
        '''
        fungsi menghapus item yang sudah diinput
        
        parameters
        nama_item   : str   nama item yang ingin dihapus
       
        return tabel pesanan
        '''
        # Menghapus item tertentu
        try:
            self.data_order.pop(nama_item)
            
            # Menampilkan list item yang telah diperbarui
            return self.check_order()
        except:
            raise exception ("Nama Item Tidak Sesuai")
            
    def reset_transaction(self):
        '''
        fungsi menghapus semua data transaksi
       
        return
        pesan : str Semua Item Berhasil Dihapus
        '''
        # Menghapus semua data transaksi
        self.data_order.clear()
        print("Semua Item Berhasil Dihapus!")
        
    def check_order(self):
        '''
        fungsi menampilkan data transaksi yang telah dibuat
        '''
        # Mengubah data ke dalam bentuk dataframe
        try:
            if len(self.data_order) == 0:
                print("Anda Belum Memesan Apapun")
            else:
                data_transac = pd.DataFrame(self.data_order).T
                data_transac.index.name = "Nama Item"
                data_transac.columns = ["Jumlah Item", "Harga", "Total Harga"]
            
                print("Pesanan Anda: ")
                print("")
                print(data_transac.to_markdown())
        except:
            raise exception ("Nama Item/Jumlah Item/Harga Item Tidak Boleh Kosong")
            
    def total_price(self):
        '''
        fungsi menampilkan total harga dari transaksi yang telah dibuat
        dan menampilkan diskon jika memenuhi persyaratan yang ada
        '''
        # Menampilkan list item
        self.check_order()
        print("")
        
        # Menghitung total harga
        total_harga = 0
        for item in self.data_order:
            total_harga += self.data_order[item][2]
        
        # Menghitung diskon
        if total_harga > 500_000:
            total = total_harga * 0.93
            print(f"Selamat! Anda Mendapatkan Diskon 7%\nTotal Belanja Anda Setelah Diskon Sebesar Rp. {total}")
        elif total_harga > 300_000:
            total = total_harga * 0.94
            print(f"Selamat! Anda Mendapatkan Diskon 6%\nTotal Belanja Anda Setelah Diskon Sebesar Rp. {total}")
        elif total_harga > 200_000:
            total = total_harga * 0.95
            print(f"Selamat! Anda Mendapatkan Diskon 5%\nTotal Belanja Anda Setelah Diskon Sebesar Rp. {total}")
        else:
            print(f"Total Belanja Anda Sebesar Rp. {total_harga}")