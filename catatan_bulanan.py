
from tkinter import *


def baca_file(file):
    f = open(file).readlines()
    data = []
    for line in f:
        data = data+[csvtoarray(line)]
    return data


def csvtoarray(Arr):
    arr_baru = []
    idx = 0
    temp = 0

    for i in range(1, len(Arr)):
        if(i == len(Arr)-1):
            arr_baru += [Arr[temp:i]]

            if(Arr[-1:] != "\n"):
                arr_baru[idx] = arr_baru[idx]+Arr[len(Arr)-1]

        else:
            if(Arr[i] == ';'):
                idx += 1
                string = Arr[temp:i]

                arr_baru = arr_baru+[string]
                temp = i+1
    return arr_baru


def catatan_bulanan():
    data_beli = baca_file('data_pembelian.txt')
    data_jual = baca_file('data_penjualan.txt')
    root = Tk()
    root.title('Stok Barang')
    myLabel = Label(root, text='Catatan Keuangan Bulanan',
                    font=('times', 13, 'bold'))
    myLabel.pack()
    list_pendapatan = [0 for i in range(12)]
    list_pengeluaran = [0 for i in range(12)]
    for i in range(1, len(data_beli)):
        bulan = int(data_beli[i][3])
        list_pengeluaran[bulan -
                         1] += (int(data_beli[i][2]))*(int(data_beli[i][1]))
    for i in range(1, len(data_jual)):
        bulan = int(data_jual[i][3])
        list_pendapatan[bulan-1] += int(data_jual[i][2])*int(data_jual[i][1])
    for i in range(12):
        label1 = Label(
            root, text=f'{i+1}. Pendapatan bulan ke-{i+1}: {list_pendapatan[i]} rupiah')
        label1.pack()
    label2 = Label(root, text='\n'+20*'='+'\n')
    label2.pack()
    for i in range(12):
        label3 = Label(
            root, text=f'{i+1}. Pengeluaran bulan ke-{i+1}: {list_pengeluaran[i]} rupiah')
        label3.pack()

    root.mainloop()
