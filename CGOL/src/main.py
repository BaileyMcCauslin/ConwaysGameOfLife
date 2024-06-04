from tkinter import *

from TkinterGUI import TkinterGUI
from ConwaysGameOfLife import ConwaysGameOfLife

tk_gui = TkinterGUI(25)
gol = ConwaysGameOfLife(25,tk_gui,500)
tk_gui.init_gui()