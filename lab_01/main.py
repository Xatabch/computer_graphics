from tkinter import *
import math_part as mp

def get_points(points_array):
    '''Строит введенные точки и получившийся треугольник с окружностями'''
    
    lb = Label(root, text=points_array)
    lb.place(x=100,y=400)
    points_array = list(points_array.split(';'))
    
    k=200
    points_arr = [] #массив для введенных точек
    
    for i in range(len(points_array)):
        k += 20
        if points_array[i] != '':
            points_arr.append([float(points_array[i].split(',')[0]),
                               float(points_array[i].split(',')[1])])
            lb = Label(root, text=str(points_array[i]))
            lb.place(x=200,y=k)
        
    k = 450   
    for i in range(len(points_arr)):
        k += 20
        lbb = Label(root, text=str(points_arr[i]))
        lbb.place(x=200,y=k)

    points = mp.find_min_square(points_arr) #вычисленные точки

    print(points)

    triangle_x1 = 520 + points[0][0]
    triangle_y1 = 320 - points[0][1]
    triangle_x2 = 520 + points[1][0]
    triangle_y2 = 320 - points[1][1]
    triangle_x3 = 520 + points[2][0]
    triangle_y3 = 320 - points[2][1]

    print(triangle_x1,triangle_y1,triangle_x2,triangle_y2,
          triangle_x3,triangle_y3)

    canvas.create_polygon([triangle_x1,triangle_y1],[triangle_x2,triangle_y2],
                          [triangle_x3,triangle_y3],fill="red")

    #canvas.create_polygon([250.5,100],[200,150],[300,150],fill="yellow")

root = Tk()
root.title('My app')
root.geometry('1320x640')

canvas = Canvas(root, width=1040, height=640, bg='#002')
canvas.pack(side = 'right')

q = -500
for y in range(21):
    k = 50 * y
    canvas.create_line(20+k,620,20+k,20,width=1,fill = '#191938')
    if q != 0 and y != 20 and y != 0:
        canvas.create_text(20+k, 300,text = str(q),fill='white')
    if y != 20 and y != 0:
        canvas.create_line(20+k,310,20+k,315,width=1,fill='white')
    q += 50

q = -300
for x in range(13):
    k = 50 * x
    canvas.create_line(20,20+k,1020,20+k,width=1,fill = '#191938')
    if q != 0 and x != 12 and x != 0:
        canvas.create_text(495, 20+k,text = str(q),fill='white')
    if x != 12 and x != 0: 
        canvas.create_line(510,20+k,515,20+k,width=1,fill='white')
    q += 50

canvas.create_line(520,20,520,620,width=1,arrow=FIRST,fill='white') #ось У
canvas.create_line(20, 320, 1020, 320,width=1,arrow=LAST, fill='white') #ось X
canvas.create_text(500,300,text='0',fill='white')



label_entry = Label(root, text="Введите точки в предложенном формате,\nразделяя их ';'")
label_entry.place(x = 10, y = 10)
label_points = Label(root, text='Точки X,Y: ')
label_points.place(x = 0, y = 80)

entry_points = Entry(root)
entry_points.place(x=80, y=80)

btn_calc = Button(root, text='Рассчитать')
btn_calc.bind('<Button-1>',lambda event: get_points(str(entry_points.get())))
btn_calc.place(x = 70, y = 150)

btn_clean = Button(root, text='Удалить все точки')
btn_clean.bind('<Button-2>')
btn_clean.place(x = 50, y = 190)
root.mainloop()
