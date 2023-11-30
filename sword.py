from tkinter import Tk, Canvas
from weapon import Weapon


class Sword(Weapon):

    def __init__(self, c, n, d):
        self._canvas = c
        self._baseDamage = d
        self._name = n
        
    def display(self, x, y):
        self._canvas.create_line(x, y, x+100, y+100, width=1)
        self._canvas.create_line(x+100, y+75, x+75, y+100)

