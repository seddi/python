# -*- coding: utf-8 -*-
from __future__ import division
from Tkinter import *

class Uygulama(object):
    def __init__(self):
        self.ekran_duzenle()
        self.karakter_al()
        self.listem()
        
        
    def karakter_al(self):
        self.depola = ""
        
    def listem(self):
        self.listele = []
        self.yeni_islem = True
    def ekran_duzenle(self):
        self.ekran = Entry(width = 18)
        self.ekran.grid(row = 1, column = 4, columnspan = 2, ipady = 4)
        self.esit_ekrani = Entry(width = 8)
        self.esit_ekrani.grid(row = 1, column = 6)
        self.satir = 4
        self.sutun = 4

        self.liste=["1","2","3",
                "4","5","6",
                "7","8","9",
                "+","0","-",
                "*","%","/",
                "<","C","=",]
        for i in self.liste:

            self.komut = lambda tus=i : self.hesapla(tus)
            Button(text=i, width=5, relief=GROOVE,
                   command = self.komut).grid(row=self.satir,
                                             column=self.sutun)
            self.sutun += 1
            if self.sutun > 6:
                self.sutun = 4
                self.satir += 1
                
            
    def hesapla(self, tus):
        self.tus = tus
        if self.tus in "0123456789":
            if self.yeni_islem :
                self.esit_ekrani.delete(0, END)
                self.ekran.insert(END,self.tus)
                self.listele.insert(len(self.listele),self.tus)
                            
        if self.tus in "+-*/%":
            if (self.yeni_islem == False):
                self.listele.insert(len(self.listele),self.esit_ekrani.get())
                self.yeni_islem = True
            for i in range(0,len(self.listele)):
                self.depola = self.depola + self.listele[i]
                
            self.depola = self.depola + self.tus
            self.listele = []
            self.ekran.delete(0, END)

        if self.tus == "=":
            for i in range(0,len(self.listele)):
                self.depola = self.depola + self.listele[i]
                
            self.listele = []
            self.ekran.delete(0,END)
            self.esit_ekrani.delete(0,END)
            self.hesap = eval(self.depola,{"__builtins__":None},{})

            self.depola = str(self.hesap)
            self.esit_ekrani.insert(END,self.depola)
            
            self.yeni_islem = False
            self.depola = ""
            
        if self.tus == "<":
            if len(self.listele):
                N = len(self.ekran.get())
                self.ekran.delete(N-1,N)
                self.listele.remove(self.listele[N-1])
            
        if self.tus == "C":
            self.ekran.delete(0,END)
            self.esit_ekrani.delete(0,END)
            self.listele = []
            self.depola = ""
            self.yeni_islem = True

pencere = Tk()
baslik=pencere.title("hesap makinasi")
pencere.resizable(width=FALSE,height=FALSE)

uyg = Uygulama()
    
mainloop()
