from tkinter import *
from tkinter import ttk

#to do add a label showing full equation
#backspace delete button, keyboard shortcuts
#cleaner output for int no '.0 '

class GUI(object):
    
    def __init__ (self,window):
        global entry
        self.window=window
        self.window.wm_title("Calculator")        
        entry=ttk.Entry(self.window, width=50)
        entry.delete(0,END)
        entry.grid(row=0, column=0, columnspan=4, stick=N+W)

        self.button0=ttk.Button(self.window,text='0',width=10, command=lambda:self.buffer(0))
        self.button0.grid(row=5,column=1)

        self.button1=ttk.Button(self.window,text='1',width=10, command=lambda:self.buffer(1))
        self.button1.grid(row=4,column=0)

        self.button2=ttk.Button(self.window,text='2',width=10, command=lambda:self.buffer(2))
        self.button2.grid(row=4,column=1)
        
        self.button3=ttk.Button(self.window,text='3',width=10, command=lambda:self.buffer(3))
        self.button3.grid(row=4,column=2)

        self.button4=ttk.Button(self.window,text='4',width=10, command=lambda:self.buffer(4))
        self.button4.grid(row=3,column=0)

        self.button5=ttk.Button(self.window,text='5',width=10, command=lambda:self.buffer(5))
        self.button5.grid(row=3,column=1)

        self.button6=ttk.Button(self.window,text='6',width=10, command=lambda:self.buffer(6))
        self.button6.grid(row=3,column=2)   

        self.button7=ttk.Button(self.window,text='7',width=10, command=lambda:self.buffer(7))
        self.button7.grid(row=2,column=0)

        self.button8=ttk.Button(self.window,text='8',width=10, command=lambda:self.buffer(8))
        self.button8.grid(row=2,column=1)

        self.button9=ttk.Button(self.window,text='9',width=10, command=lambda:self.buffer(9))
        self.button9.grid(row=2,column=2)         

        self.buttonequal=ttk.Button(self.window,text='=',width=10, command=self.execute)
        self.buttonequal.grid(row=5,column=3)

        self.buttondecimal=ttk.Button(self.window,text='.',width=10, command=self.decimal)
        self.buttondecimal.grid(row=5,column=2)

        self.buttonsign=ttk.Button(self.window,text='+/-',width=10, command=lambda:entry.insert(0,'-'))
        self.buttonsign.grid(row=5,column=0)

        self.buttonplus=ttk.Button(self.window,text='+',width=10, command=lambda: self.ADD(entry.get()))
        self.buttonplus.grid(row=4,column=3)

        self.buttonminus=ttk.Button(self.window,text='-',width=10, command=lambda: self.SUBSTRACT(entry.get()))
        self.buttonminus.grid(row=3,column=3)

        self.buttonmultiply=ttk.Button(self.window,text='*',width=10, command=lambda: self.MULTIPLY(entry.get()))
        self.buttonmultiply.grid(row=2,column=3)

        self.buttondivide=ttk.Button(self.window,text='/',width=10, command=lambda: self.DIVIDE(entry.get()))
        self.buttondivide.grid(row=1,column=3)

        self.buttondelete=ttk.Button(self.window,text='Clear',width=10, command=lambda:entry.delete(0,END))
        self.buttondelete.grid(row=1,column=0)        

    def buffer(self,input1):
        global Input1
        entry.insert(END,input1)
        checkdec=entry.get()
        Input1=float(checkdec)
        #if '.' in checkdec:
            # if '+' in checkdec:
            #     Input1=float(checkdec.rsplit('+',1)[-1])
            # elif '/' in checkdec:
            #     Input1=float(checkdec.rsplit('/',1)[-1])
            # elif '*' in checkdec:
            #     Input1=float(checkdec.rsplit('*',1)[-1])
            # elif '-' in checkdec:
            #     Input1=float(checkdec.rsplit('-',1)[-1])
        #else:
            #Input1=float(checkdec)
            #print(Input1)

    def decimal(self):
        global Input1
        if '.' not in entry.get():
            Input1=.0
            entry.insert(END,'.')

    def ADD(self, input2):
        global Input2
        global signFlag
        entry.delete(0,END)   
        Input2=float(input2)         
        #entry.insert(END,input2+'+')
        signFlag='ADD'

    def SUBSTRACT(self, input2):
        global Input2
        global signFlag
        Input2=float(input2)
        entry.delete(0,END)    
        #entry.insert(END,input2)
        signFlag='MINUS'

    def DIVIDE(self, input2):
        global Input2
        global signFlag
        Input2=float(input2)
        entry.delete(0,END)    
        #entry.insert(END,input2)
        signFlag='DIVIDE'

    def MULTIPLY(self, input2):
        global Input2
        global signFlag
        Input2=float(input2)
        entry.delete(0,END)    
        #entry.insert(END,input2)
        signFlag='MULTIPLY'        

    def execute(self):
        if signFlag == 'ADD':
            result=Input1+Input2
            entry.delete(0,END)
            entry.insert(0,result)
        if signFlag == 'MINUS':
            result=Input1-Input2
            entry.delete(0,END)
            entry.insert(0,result)        
        if signFlag == 'DIVIDE':
            result=Input2/Input1
            entry.delete(0,END)
            entry.insert(0,result)        
        if signFlag == 'MULTIPLY':
            result=Input1*Input2
            entry.delete(0,END)
            entry.insert(0,result)

window=Tk()

windowUI=GUI(window)

window.mainloop()