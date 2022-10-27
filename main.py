import tkinter as tk
from tkinter import *
from catatan_bulanan import catatan_bulanan
from hapus_data import hapus_data
from lihat_stok import stok_data
from pembelian import main_beli
from penjualan import main_jual
from update_data import update_data


app = tk.Tk()

app.geometry("370x300")
app.title('Program Produksi Meja Pingpong')
app.maxsize(370, 300)
app.minsize(370, 300)


labelmenu = Label(app, text='\n\n',
                  font=('times', 18, 'bold'))
labelmenu.grid(row=0)
pembelian = Button(app, text="Data Pembelian", width=20, command=main_beli,
                   bg="green", fg="white", borderwidth=3, relief=RIDGE)
pembelian.grid(row=1, sticky="w", padx=15, pady=5)
penjualan = Button(app, text="Data Penjualan", width=20, command=main_jual,
                   bg="green", fg="white", borderwidth=3, relief=RIDGE)
penjualan.grid(row=1, column=2, sticky="w", padx=15, pady=5)
stok = Button(app, text="Stock Barang", width=20, command=stok_data,
              bg="green", fg="white", borderwidth=3, relief=RIDGE)
stok.grid(row=2, sticky="w", padx=15, pady=5)
update = Button(app, text="Update Data", width=20, command=update_data,
                bg="green", fg="white", borderwidth=3, relief=RIDGE)
update.grid(row=2, column=2, sticky="w", padx=15, pady=5)
hapus = Button(app, text="Hapus Data", width=20, command=hapus_data,
               bg="green", fg="white", borderwidth=3, relief=RIDGE)
hapus.grid(row=3, sticky="w", padx=15, pady=5)
catatan_perbulan = Button(app, text="Catatan Perbulan", width=20, command=catatan_bulanan,
                          bg="green", fg="white", borderwidth=3, relief=RIDGE)
catatan_perbulan.grid(row=3, column=2, sticky="w", padx=15, pady=5)


app.mainloop()
