from tkinter import *


def update_data():
    root = Tk()
    root.geometry('520x540')
    root.title("Update Data Barang")
    root.configure(background='grey')

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

    def saveData(file, data):

        data = convert(data)

        f = open(file, "w")
        f.write(data)
        f.close()

    def convert(data):
        string = ""
        for tempData in data:
            tempDatas = [str(var) for var in tempData]
            string += ";".join(tempDatas)
            string += "\n"
        return string

    def msg():
        select = var.get()

    def save():
        g = var.get()

        data_stok = baca_file('stok.txt')
        condition = True
        index = 0
        try:
            cek_input_stok = int(e2.get())
            if int(e2.get()) >= 0:
                for i in range(len(data_stok)):
                    if str(e1.get().lower()) == data_stok[i][0]:
                        condition = False
                        index = i
                if condition == False:
                    data_stok[index][1] = str(e2.get())
                    saveData('stok.txt', data_stok)
                    mylabel = Label(root, text="Data Berhasil Diupdate!", width=25,
                                    font=("times", 20, "bold"), bg='blue', fg='white')
                    mylabel.place(x=70, y=240)
                    mylabel.after(1000, mylabel.master.destroy)
                else:
                    data_stok += [[e1.get().lower(), e2.get()]]

                    saveData('stok.txt', data_stok)
                    mylabel = Label(root, text="Data Berhasil Diupdate!", width=18,
                                    font=("times", 12, "bold"), bg='blue', fg='white')
                    mylabel.place(x=70, y=240)
                    mylabel.after(1000, mylabel.master.destroy)
            else:
                mylabel1 = Label(root, text="Jumlah harus lebih dari 0!", width=18,
                                 font=("times", 12, "bold"), bg='blue', fg='white')
                mylabel1.place(x=70, y=240)
                mylabel1.after(1000, mylabel1.master.destroy)
        except ValueError:
            mylabel1 = Label(root, text="Input tidak sesuai!", width=18,
                             font=("times", 12, "bold"), bg='blue', fg='white')
            mylabel1.place(x=70, y=240)
            mylabel1.after(1000, mylabel1.master.destroy)

    def saveinfo():
        save()

    l1 = Label(root, text="Data Pembelian Barang", width=25,
               font=("times", 20, "bold"), bg='blue', fg='white')
    l1.place(x=70, y=50)
    l2 = Label(root, text="Nama Barang", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l2.place(x=70, y=130)
    e1 = Entry(root, width=30, bd=2)
    e1.place(x=240, y=130)
    l3 = Label(root, text="Jumlah stok", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l3.place(x=70, y=180)
    e2 = Entry(root, width=30, bd=2)
    e2.place(x=240, y=180)

    var = IntVar()

    b1 = Button(root, text='Update', command=saveinfo, width=15,
                bg='green', fg='white', font=("times", 12, "bold"))
    b1.place(x=120, y=440)
    b2 = Button(root, text='Cancel', command=root.destroy, width=15,
                bg='maroon', fg='white', font=("times", 12, "bold"))
    b2.place(x=320, y=440)

    root.mainloop()
