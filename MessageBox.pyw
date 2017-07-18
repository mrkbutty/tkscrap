#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import Tkinter as tk
import tkMessageBox as tkmb

args = ', '.join(sys.argv)
print 'Args', args

top = tk.Tk()
def hello():
   tkmb.showinfo("Args", args)

B1 = tk.Button(top, text = "Get Args", command = hello)
B1.pack()

top.mainloop()
