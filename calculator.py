from tkinter import *
from tkinter import ttk

class GUI(object):

    def __init__ (self,window):
        self.window=window
        self.userin=IntVar()
        self.entry=ttk.Entry(window, textvariable=self.userin)
        self.entry.grid()
