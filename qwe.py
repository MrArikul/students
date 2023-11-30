from tkinter import Tk, Canvas
from grid import Grid
from student import Student
from sword import Sword
from weapon import Weapon
from hero import Hero
import random

root= Tk()
canvas = Canvas(root,width=800,height=600)
canvas.pack()
grid = Grid(canvas)
grid.display()

fs=open('students.txt','r',encoding='utf-8')

students=[]
for student in fs:
    s=student.split(';')
    id=int(s[0])
    name=s[1]
    var=int(s[3])
    group='ИП-21'
    gender=s[2]
    students.append({'id':id,'full_name':name, 'variant':var, 'group':group, 'gender':gender })


fs.close()

wp1 = Sword(canvas, 'Меч тысячи истин', 12)
wp2 = Sword(canvas, 'Скалка Пирожка', 9)


s1 = random.choice(students)
p1=Hero(canvas, s1['full_name'], 100, 500, s1['gender'])
p1.setWeapon(wp1)
p1.display()

s1 = random.choice(students)
p2=Hero(canvas, s1['full_name'], 500, 500, s1['gender'])
p2.setWeapon(wp2)
p2.display()

p1.attack(p2)
root.mainloop()