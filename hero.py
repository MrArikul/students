from tkinter import Tk, Canvas, ARC, W, CENTER
from human import Human


class Hero(Human):
    
    def __init__(self, canvas, name, x, y, gen):
        super().__init__(canvas, name, x, y, gen)
        self.health = 100
        self.wp = None
    
    def setWeapon(self, weapon):
        self._wp = weapon
        
    def attack(self, enemy):
        damage = self._wp.hit()
        print(f'{self._name} нанес(ла) {damage} урона  {enemy._name}!')
        print(f'у {enemy._name} осталось {enemy.health} здоровья!')
        
        
    def _drawName(self):
        name =f"{self._name.split()[0]} {self._name.split()[1][0]}. {self._name.split()[2][0]}."
        self.canvas.create_text(self.x+50, self.y-250,
        text=name,
        justify=CENTER, font="Verdana 14")
        self.canvas.create_line(self.x, self.y-284, self.x+100, self.y-284, width=10, fill="green")
        
    def _drawWeapon(self):
        self._wp.display(self.x-100, self.y-200)
        
    def display(self):
        super().display()
        self._drawWeapon()