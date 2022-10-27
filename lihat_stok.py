
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


def stok_data():
    f = baca_file('stok.txt')
    root = Tk()
    root.geometry("380x900")
    root.title('Stok Barang')
    root.maxsize(380, 900)
    root.minsize(380, 900)
    myLabel = Label(root, text='STOK BARANG', font=('times', 13, 'bold'))
    myLabel.grid(row=0, column=0)
    for i in range(len(f)):
        for j in range(2):
            if i == 0:
                myLabel = Label(
                    root, text=f[i][j] + '   ', font=('times', 10, 'bold'))
                myLabel.grid(row=3, column=j)
                myLabel = Label(
                    root, text=20*'_', font=('times', 10, 'bold'))
                myLabel.grid(row=4, column=j)
            else:
                if j == 0:
                    myLabel = Label(
                        root, text=f[i][j] + '  ', font=('times', 10, 'bold'))
                    myLabel.grid(row=i+4, column=0)
                else:
                    myLabel = Label(
                        root, text=f[i][j], font=('times', 10, 'bold'))
                    myLabel.grid(row=i+4, column=1)

    root.mainloop()
