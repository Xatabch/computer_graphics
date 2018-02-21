from tkinter import *
from sympy import *
from math import *

def draw_circle(center,radius):
    '''Рисует окружность'''

    points_array = []
    start = center[0] - radius
    end = center[0] + radius
    y = Symbol('y')
    for i in range(start, end+1, 1):
        root = solve((i-center[0])**2 + (y-center[1])**2 - radius**2, y)
        #print(root)
        if len(root) == 2:
            points_array.append([580 + float(i), 310 - float(root[0])])
            points_array.append([580 + float(i), 310 - float(root[1])])
        else:
            points_array.append([580 + float(i), 310 - float(root[0])])

    canvas.create_polygon(points_array,outline="red")

root = Tk()
root.title('My app')
root.geometry('1320x640')

canvas = Canvas(root, width=1040, height=640, bg='white')
canvas.pack(side='right')

# смещение по x
x = 15
# смещение по y
y = 130

# Меню
btn_rep = Button(root, text='Переместить', width=25)
btn_rep.bind('<Button-1>')
btn_rep.place(x=x, y=y)

label_rep_dx = Label(root, text='dx:')
label_rep_dx.place(x=x, y=y+40)
entry_rep_dx = Entry(root, width=10)
entry_rep_dx.place(x=x+25, y=y+40)

label_rep_dy = Label(root, text='dy:')
label_rep_dy.place(x=x+115, y=y+40)
entry_rep_dy = Entry(root, width=10)
entry_rep_dy.place(x=x+140, y=y+40)


btn_sc = Button(root, text='Масштабировать', width=25)
btn_sc.bind('<Button-1>')
btn_sc.place(x=x, y=y+140)

label_sc_cent = Label(root, text='cent:')
label_sc_cent.place(x=x, y=y+180)
entry_sc_cent = Entry(root, width=5)
entry_sc_cent.place(x=x+35, y=y+180)

label_sc_dx = Label(root, text='dx:')
label_sc_dx.place(x=x+82, y=y+180)
entry_sc_dx = Entry(root, width=5)
entry_sc_dx.place(x=x+107, y=y+180)

label_sc_dy = Label(root, text='dy:')
label_sc_dy.place(x=x+155, y=y+180)
entry_sc_dy = Entry(root, width=5)
entry_sc_dy.place(x=x+180, y=y+180)


btn_sc = Button(root, text='Поворот', width=25)
btn_sc.bind('<Button-1>')
btn_sc.place(x=x, y=y+280)

label_sc_cent = Label(root, text='cent:')
label_sc_cent.place(x=x, y=y+320)
entry_sc_cent = Entry(root, width=5)
entry_sc_cent.place(x=x+35, y=y+320)

label_sc_dx = Label(root, text='dx:')
label_sc_dx.place(x=x+82, y=y+320)
entry_sc_dx = Entry(root, width=5)
entry_sc_dx.place(x=x+107, y=y+320)

label_sc_dy = Label(root, text='dy:')
label_sc_dy.place(x=x+155, y=y+320)
entry_sc_dy = Entry(root, width=5)
entry_sc_dy.place(x=x+180, y=y+320)

draw_circle([1,1],50)


root.mainloop()
