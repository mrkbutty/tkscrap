#!python
# -*- coding: utf-8 -*-
import sys
import tkinter as tk
#import tkMessageBox as tkmb
import tkinter.messagebox as tkmb

pyexe=sys.executable+' '+sys.version.split()[0]
args = '\n'.join(sys.argv)
print('Args', pyexe+args)

top = tk.Tk()
def hello():
   tkmb.showinfo("Args", pyexe+'\n'+args)

B1 = tk.Button(top, text = "Get Args", command = hello)
B1.pack()

top.mainloop()
