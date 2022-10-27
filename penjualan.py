from tkinter import *


def main_jual():
    root = Tk()
    root.geometry('520x540')
    root.title("Input Data Penjualan Barang")
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
        i = 0
        string = ""
        for tempData in data:
            i += 1
            tempDatas = [str(var) for var in tempData]
            string += ";".join(tempDatas)
            if i != len(data):
                string += "\n"
        return string

    def msg():
        bulan = cvar.get()
        select = var.get()

    def save():
        g = var.get()
        bulan = cvar.get()

        s = '\n' + e1.get().lower()+';'+e2.get()+';'+e3.get()+';'+bulan
        f = open(('data_penjualan.txt'), 'a')
        x = baca_file('data_penjualan.txt')

        data_stok = baca_file('stok.txt')
        condition = True
        index = 0
        try:
            for i in range(len(data_stok)):
                if str(e1.get().lower()) == data_stok[i][0]:
                    condition = False
                    index = i
            cek_input_harga = int(e2.get())
            cek_input_stok = int(e3.get())
            if condition == False:
                if (int(data_stok[index][1]) - int(e3.get())) < 0:
                    l10 = Label(root, text="Stok tidak mencukupi", font=(
                        "times", 9, "bold"), anchor="w", bg='grey')
                    l10.place(x=70, y=280)
                else:
                    data_stok[index][1] = str(
                        int(data_stok[index][1]) - int(e3.get()))
                    saveData('stok.txt', data_stok)
                    if (len(x)) == 0:
                        f.write('Barang'+';'+'Harga'+';'+'Jumlah'+';'+'Bulan')
                    f.write(s)
            else:
                l11 = Label(root, text="Barang tidak tersedia", font=(
                    "times", 9, "bold"), anchor="w", bg='grey')
                l11.place(x=70, y=280)
            f.close()
            l8 = Label(root, text="Input telah sesuai", font=(
                "times", 9, "bold"), anchor="w", bg='grey')
            l8.place(x=70, y=370)
            l8.after(1000, l8.master.destroy)
        except ValueError:
            l8 = Label(root, text="Input tidak sesuai", font=(
                "times", 9, "bold"), anchor="w", bg='grey')
            l8.place(x=70, y=370)
            l8.after(1000, l8.master.destroy)

    def saveinfo():
        save()

    l1 = Label(root, text="Data penjualan Barang", width=25,
               font=("times", 20, "bold"), bg='blue', fg='white')
    l1.place(x=70, y=50)
    l2 = Label(root, text="Nama Barang", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l2.place(x=70, y=130)
    e1 = Entry(root, width=30, bd=2)
    e1.place(x=240, y=130)
    l3 = Label(root, text="Harga", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l3.place(x=70, y=180)
    e2 = Entry(root, width=30, bd=2)
    e2.place(x=240, y=180)

    var = IntVar()

    l6 = Label(root, text="Jumlah", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l6.place(x=70, y=230)
    e3 = Entry(root, width=30, bd=2)
    e3.place(x=240, y=230)
    l7 = Label(root, text="Bulan penjualan", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l7.place(x=70, y=280)

    cvar = StringVar()
    cvar.set("Bulan penjualan")
    option = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    o = OptionMenu(root, cvar, *option)
    o.config(font=("times", 11), bd=3)
    o.place(x=240, y=280, width=190)

    b1 = Button(root, text='Submit', command=saveinfo, width=15,
                bg='green', fg='white', font=("times", 12, "bold"))
    b1.place(x=120, y=330)
    b2 = Button(root, text='Cancel', command=root.destroy, width=15,
                bg='maroon', fg='white', font=("times", 12, "bold"))
    b2.place(x=320, y=330)
    l8 = Label(root, text="Jika sudah klik submit otomatis tercatat di file data_penjualan.txt", font=(
        "times", 9, "bold"), anchor="w", bg='grey')
    l8.place(x=100, y=420)

    root.mainloop()
