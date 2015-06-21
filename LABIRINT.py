from tkinter import*

WIDTH = 500
HEIGHT = 500



class Labirint():
    def __init__(self, master):

        self.canvas = Canvas(master, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.nalozi_matriko()
        zac_x, zac_y = self.narisi()
        self.k = Krogla(zac_x, zac_y, self.canvas, self.matrika)
        self.canvas.bind("<Left>", self.k.levo)
        self.canvas.bind("<Right>", self.k.desno)
        self.canvas.bind("<Up>", self.k.gor)
        self.canvas.bind("<Down>", self.k.dol)
        self.canvas.focus_set()
        menu = Menu(master)
        master.config(menu=menu)
        file = Menu(menu)
        menu.add_cascade(label="Menu", menu = file)
        file.add_command(label="Shrani", command=self.shrani)
        file.add_command(label="Zapri", command=master.destroy)
        

            
    def nalozi_matriko(self, file="nacrt2.txt"):
        self.matrika = []
        with open(file) as beri:
            for vrstica in beri:
                podsez = []
                for znak in vrstica:
                    if znak != "\n":
                        podsez.append(znak)
                self.matrika.append(podsez)

    def narisi(self):
        for i in range(len(self.matrika)):
            for j in range(len(self.matrika[i])):
                if self.matrika[i][j] == "*":
                    self.canvas.create_rectangle(
                        50*j, 50*i, 50*j + 50, 50*i + 50, fill = "black")
                if self.matrika[i][j] == "M":
                    self.canvas.create_rectangle(
                        50*j, 50*i, 50*j + 50, 50*i + 50, fill = "yellow")
                if self.matrika[i][j] == "Z":
                    zac_x = int(j * 50)
                    zac_y = int(i * 50)
        return zac_x, zac_y

    def shrani(self):
        print ("SHRANJENO")
        x = self.k.x / 50
        y = self.k.y / 50
        with open ("nacrt2.txt", "wt") as pisi:
            for i in range (len(self.matrika)):
                for j in range(len(self.matrika[i])):
                    if self.matrika[i][j] == "Z":
                        print(" ",file=pisi,end="")
                    elif i == y and j == x:
                        print("Z", file=pisi,end="")
                    else:
                        print(self.matrika[i][j],file=pisi,end="")
                print("",file=pisi)


        

class Krogla():
    def __init__(self, x, y, canvas, zid):
        self.zid = zid
        self.canvas = canvas
        self.x = x
        self.y = y
        self.krogec = self.canvas.create_oval(
            self.x, self.y, self.x + 50, self.y + 50, fill="orange")

    def levo(self, event):
        new_x = int((self.x - 50) / 50)
        new_y = int(self.y / 50)
        index = True
            
        if index:
            if self.zid[new_y][new_x] != "*" and new_x >=0:
                self.x -= 50
                self.canvas.coords(self.krogec, self.x, self.y, self.x + 50, self.y + 50)
                self.preveri_ce_je_konec(new_x, new_y)
        

    def desno(self, event):
        new_x = int((self.x + 50) / 50)
        new_y = int(self.y / 50)
        index = True
        try:
            self.zid[new_y][new_x]
        except IndexError:
            index = False
            
        if index:
            if self.zid[new_y][new_x] != "*":
                self.x += 50
                self.canvas.coords(self.krogec, self.x, self.y, self.x + 50, self.y + 50)
                self.preveri_ce_je_konec(new_x, new_y)

    def gor(self, event):
        new_x = int(self.x  / 50)
        new_y = int((self.y - 50) / 50)
        index = True
            
        if index:
            if self.zid[new_y][new_x] != "*" and new_y >= 0:
                self.y -= 50
                self.canvas.coords(self.krogec, self.x, self.y, self.x + 50, self.y + 50)
                self.preveri_ce_je_konec(new_x, new_y)

    def dol(self, event):
        new_x = int(self.x  / 50)
        new_y = int((self.y + 50) / 50)
        index = True
        try:
            self.zid[new_y][new_x]
        except IndexError:
            index = False
            
        if index:
            if self.zid[new_y][new_x] != "*":
                self.y += 50
                self.canvas.coords(self.krogec, self.x, self.y, self.x + 50, self.y + 50)
                self.preveri_ce_je_konec(new_x, new_y)

    

    def preveri_ce_je_konec(self,x, y):
        if self.zid[y][x] == "M":
            print ("ZMAGA")
            

root = Tk()

aplikacija = Labirint(root)

root.mainloop()
