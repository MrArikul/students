from human import Human
from tkinter import Tk, Canvas, CENTER

class Student(Human):

    def __init__(self, canvas, name, x, y, g, v):
        super().__init__(canvas, name, x, y, g)
        self.group = g
        self.var = v
        
   
        