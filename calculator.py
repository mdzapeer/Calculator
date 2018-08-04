from tkinter import *
from tkinter import ttk

class GUI(object):

    def __init__ (self,window):
        self.window=window
        self.window.wm_title("Calculator")
        self.userin=IntVar()
        self.entry=ttk.Entry(self.window, textvariable=self.userin, width=50)
        self.entry.grid(row=0, column=0, columnspan=4, stick=N+W)

        self.button0=ttk.Button(self.window,text='0',width=10)
        self.button0.grid(row=5,column=1)

        self.button1=ttk.Button(self.window,text='1',width=10)
        self.button1.grid(row=4,column=0)

        self.button2=ttk.Button(self.window,text='2',width=10)
        self.button2.grid(row=4,column=1)
        
        self.button3=ttk.Button(self.window,text='3',width=10)
        self.button3.grid(row=4,column=2)

        self.button4=ttk.Button(self.window,text='4',width=10)
        self.button4.grid(row=3,column=0)

        self.button5=ttk.Button(self.window,text='5',width=10)
        self.button5.grid(row=3,column=1)

        self.button6=ttk.Button(self.window,text='6',width=10)
        self.button6.grid(row=3,column=2)   

        self.button7=ttk.Button(self.window,text='7',width=10)
        self.button7.grid(row=2,column=0)

        self.button8=ttk.Button(self.window,text='8',width=10)
        self.button8.grid(row=2,column=1)

        self.button9=ttk.Button(self.window,text='9',width=10)
        self.button9.grid(row=2,column=2)         

        self.buttonequal=ttk.Button(self.window,text='=',width=10)
        self.buttonequal.grid(row=5,column=3)

        self.buttondecimal=ttk.Button(self.window,text='.',width=10)
        self.buttondecimal.grid(row=5,column=2)

        self.buttonsign=ttk.Button(self.window,text='+/-',width=10)
        self.buttonsign.grid(row=5,column=0)

        self.buttonplus=ttk.Button(self.window,text='+',width=10)
        self.buttonplus.grid(row=4,column=3)

        self.buttonminus=ttk.Button(self.window,text='-',width=10)
        self.buttonminus.grid(row=3,column=3)

        self.buttonmultiply=ttk.Button(self.window,text='*',width=10)
        self.buttonmultiply.grid(row=2,column=3)

        self.buttondivide=ttk.Button(self.window,text='/',width=10)
        self.buttondivide.grid(row=1,column=3)        

window=Tk()

windowUI=GUI(window)

window.mainloop()