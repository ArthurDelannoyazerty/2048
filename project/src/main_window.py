from tkinter import *
import constants as c

class Main_Window():
    
    def __init__(self):
        self.window = Tk()
        self.window.title("2048")
        size = str(c.WIDTH_WINDOW_PX) + "x" + str(c.HEIGHT_WINDOW_PX)
        self.window.geometry(size)
        