from tkinter import *
import math_part as mp
from pandas import DataFrame


def get_points(all_points):
    '''Строит введенные точки и получившийся треугольник с окружностями'''

    global circumscribed_circle1
    global triangle1
    global inscribed_circle1
    global table
    global answer
    global K
    global text_x
    global text_y

    #entry_points.delete(0, 'end')

    #points_array = list(points_array.split(';'))

    #points_arr = [] #массив для введенных точек
    
    #for i in range(len(points_array)):
    #    if points_array[i] != '':
    #        points_arr.append([float(points_array[i].split(',')[0]),
    #                           float(points_array[i].split(',')[1])])
    #        all_points.append([float(points_array[i].split(',')[0]),
    #                           float(points_array[i].split(',')[1])])

    size = '150x'+str(len(all_points)*50)

    table = Tk()
    table.title('Table')
    table.geometry(size)

    tb = DataFrame(all_points,columns=['x','y'])
    lb = Label(table, text = str(tb))
    lb.place(x=0,y=0)

    answer = Tk()
    answer.title('Results')
    answer.geometry('400x400')

    points = mp.find_min_square(all_points) #вычисленные точки
    print(mp.size_length(points[0], points[1], points[2]))
    for i in range(len(points)):
        for j in range(len(points[i])):
            if(points[i][j] < 50):
                K = 50
            else:
                K = 1

    if 0 not in points:
        center_cc = mp.center_circumscribed_circle(points) #центр описанной окружности
        radius_cc = mp.radius_circumscribed_circle(points) #радиус описанной окружности
        print('center_cc: ',center_cc)
        print('radius_cc: ',radius_cc)

        x1 = 520 + (center_cc[0] - radius_cc)*K
        y1 = 320 - (center_cc[1] - radius_cc)*K
        x2 = 520 + (center_cc[0] + radius_cc)*K
        y2 = 320 - (center_cc[1] + radius_cc)*K

        print('x1 y1 x2 y2: ',x1,y1,x2,y2)

        center_ic = mp.center_inscribed_circle(points)  #центр вписанной окружности
        radius_ic = mp.radius_inscribed_circle(points)  #радиус вписанной окружности

        x3 = 520 + (center_ic[0] - radius_ic)*K
        y3 = 320 - (center_ic[1] - radius_ic)*K
        x4 = 520 + (center_ic[0] + radius_ic)*K
        y4 = 320 - (center_ic[1] + radius_ic)*K

        #print('center_cc', center_cc)
        #print('center_ic', center_ic)
        #print('x3,y3,x4,y4', x3, y3, x4, y4)

        circumscribed_circle1 = canvas.create_oval(x1, y1, x2, y2, outline="red",
            fill="green", width=2)

        triangle_x1 = 520 + points[0][0]*K
        triangle_y1 = 320 - points[0][1]*K
        triangle_x2 = 520 + points[1][0]*K
        triangle_y2 = 320 - points[1][1]*K
        triangle_x3 = 520 + points[2][0]*K
        triangle_y3 = 320 - points[2][1]*K

        triangle1 = canvas.create_polygon([triangle_x1,triangle_y1],[triangle_x2,triangle_y2],
                              [triangle_x3,triangle_y3],fill="red")

        inscribed_circle1 = canvas.create_oval(x3[0], y3[0], x4[0], y4[0], outline="yellow",
            fill="white", width=2)

        lb = Label(answer, text='РЕЗУЛЬТИРУЮЩИЕ ТОЧКИ')
        lb.place(x=110, y = 10)

        indexes = [0,0,0]
        for i in range(len(points)):
            indexes[i] = all_points.index(points[i])

        circumscribed_circle = mp.square_circumscribed_circle(points[0], points[1], points[2])
        inscribed_circle = mp.square_inscribed_circle(points[0], points[1], points[2])

        table_result_points = DataFrame(points,columns=['x','y'],index=indexes)
        res_points = Label(answer, text=str(table_result_points))
        res_points.place(x=140, y=30)

        lb_square_inc_circle = Label(answer, text='ПЛОЩАДЬ ВПИСАННОЙ ОКРУЖНОСТИ: ')
        lb_square_inc_circle.place(x=10, y = 130)
        square_inc_circle = Label(answer, text = str(round(inscribed_circle, 3)))
        square_inc_circle.place(x=270, y=130)

        lb_square_circ_circle = Label(answer, text='ПЛОЩАДЬ ОПИСАННОЙ ОКРУЖНОСТИ: ')
        lb_square_circ_circle.place(x=10, y=150)
        square_circ_circle = Label(answer, text=str(round(circumscribed_circle, 3)))
        square_circ_circle.place(x=270, y=150)

        lb_square_difference = Label(answer, text='РАЗНОСТЬ ПЛОЩАДЕЙ: ')
        lb_square_difference.place(x=10, y=170)
        square_circ_circle = Label(answer, text=str(round(abs(circumscribed_circle - inscribed_circle), 3)))
        square_circ_circle.place(x=270, y=170)


    table.mainloop()
    answer.mainloop()

def filtered_data(points_array):
    '''Преобразует информацию к нормальному виду для добавления'''


    entry_points.delete(0, 'end')

    points_array = list(points_array.split(';'))

    for i in range(len(points_array)):
        if points_array[i] != '':
            all_points.append([float(points_array[i].split(',')[0]),
                               float(points_array[i].split(',')[1])])


    print(all_points)

def start(points_array):
    filtered_data(points_array)
    get_points(all_points)

def delete_all_points():
    '''Удаляет все введенные ранее точки'''

    canvas.delete(circumscribed_circle1)
    canvas.delete(triangle1)
    canvas.delete(inscribed_circle1)
    table.destroy()
    answer.destroy()


def add_and_reset(points_array):
    '''Добавляет точки и перевычисляет'''

    delete_all_points()
    start(points_array)


def delete_points(points_array):
    '''Удаляет заданные точки'''

    delete_all_points()

    entry_points.delete(0, 'end')

    points_array = list(points_array.split(';'))

    points_arr = []

    for i in range(len(points_array)):
        if points_array[i] != '':
            points_arr.append([float(points_array[i].split(',')[0]),
                               float(points_array[i].split(',')[1])])

    for i in range(len(points_arr)):
        if points_arr[i] in all_points:
            all_points.remove(points_arr[i])

    get_points(all_points)


root = Tk()
root.title('My app')
root.geometry('1320x640')

global all_points
all_points = []

canvas = Canvas(root, width=1040, height=640, bg='#002')
canvas.pack(side = 'right')

q = -500
for y in range(21):
    k = 50 * y
    canvas.create_line(20+k,620,20+k,20,width=1,fill = '#191938')
    #if q != 0 and y != 20 and y != 0:
    #    canvas.create_text(20+k, 300,text = str(q),fill='white')
    if y != 20 and y != 0:
        canvas.create_line(20+k,310,20+k,315,width=1,fill='white')
    q += 50

q = -300
for x in range(13):
    k = 50 * x
    canvas.create_line(20,20+k,1020,20+k,width=1,fill = '#191938')
    #if q != 0 and x != 12 and x != 0:
    #    canvas.create_text(495, 20+k,text = str(q),fill='white')
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
btn_calc.bind('<Button-1>', lambda event: start(str(entry_points.get())))
btn_calc.place(x = 70, y = 150)

btn_clean = Button(root, text='Удалить все точки')
btn_clean.bind('<Button-1>', lambda event: delete_all_points())
btn_clean.place(x = 50, y = 190)

btn_add = Button(root, text='Добавить точки')
btn_add.bind('<Button-1>', lambda event: add_and_reset(str(entry_points.get())))
btn_add.place(x=50, y= 230)

btn_add = Button(root, text='Удалить точку(и))')
btn_add.bind('<Button-1>', lambda event: delete_points(str(entry_points.get())))
btn_add.place(x=50, y= 270)


root.mainloop()
