from tkinter import *
import math_part as mp
from pandas import DataFrame

def clear():
    '''Очищает экран'''

    if len(array_points) > 0:
        try:
            for i in range(len(array_points)):
                canvas.delete(array_points[i])
        except:
            error_window('ТОЧЕК НЕТ!')

        try:
            canvas.delete(circumscribed_circle1)
            canvas.delete(triangle1)
            canvas.delete(inscribed_circle1)
        except:
            print('') # подумай над текстом сообщения


def error_window(error_text):
    '''Выводит ошибки'''

    error = Tk()
    error.title("Ошибка выполнения")
    error.geometry('300x50')

    lb_error_no_points = Label(error, text=error_text, fg='red')
    lb_error_no_points.place(x=10,y=15)

    error.mainloop()


def table_t(all_points):
    '''Выводит таблицу со всеми точками'''

    global table

    if len(all_points) > 0:
        size = '150x' + str(len(all_points) * 50)

        table = Tk()
        table.title('Table')
        table.geometry(size)

        tb = DataFrame(all_points, columns=['x', 'y'])
        lb = Label(table, text=str(tb))
        lb.place(x=0, y=0)

        table.mainloop()
    else:
        error_window('ТАБЛИЦА ПУСТА!')


def create_points(K,all_points):
    '''Строит все имеющиеся точки'''

    #K = 1 # коэффициент масштабирования
    #for i in range(len(all_points)):
    #    for j in range(len(all_points[i])):
            #if(all_points[i][j] >= 50):
            #    K=1
            #if (all_points[i][j] >= 20 and all_points[i][j] <= 40):
            #    K = 3
            #if(all_points[i][j] >= 7 and all_points[i][j] < 15):
            #    K=30

    for i in range(len(all_points)):
        points_text = canvas.create_text((580 + all_points[i][0]*K), 310 - all_points[i][1]*K,
                                         text=(str(i) + '.' + '(' + str(all_points[i][0]) + ', ' +
                                               str(all_points[i][1]) + ')'), fill='white')

        points = canvas.create_oval((520 + all_points[i][0]*K - 5), (320 - all_points[i][1]*K - 5),
                                    (520 + all_points[i][0]*K + 5),
                                    (320 - all_points[i][1]*K + 5), outline='red',
                                    fill='red', width=1)
        array_points.append(points)
        array_points.append(points_text)


def get_points(all_points):
    '''Строит введенные точки и получившийся треугольник с окружностями'''

    global circumscribed_circle1
    global triangle1
    global inscribed_circle1
    global points
    global answer
    global K
    global text_x
    global text_y

    if len(all_points) > 2:
        calculated_points = mp.find_min_square(all_points) #вычисленные точки

        K = 50  # коэффициент масштабирования
        max = -1000
        if 0 not in calculated_points:
            for i in range(len(calculated_points)):
                for j in range(len(calculated_points[i])):
                    print(abs(calculated_points[i][j]))
                    if abs(calculated_points[i][j]) > max:
                        max = abs(calculated_points[i][j])

            if (max >= 50):
                K = 1
            elif (max >= 20 and max <= 40):
                K = 3
            elif (max >= 7):
                K = 30

            print(K,max)

        if 0 not in calculated_points:
            answer = Tk()
            answer.title('Results')
            answer.geometry('400x400')

            center_cc = mp.center_circumscribed_circle(calculated_points) #центр описанной окружности
            radius_cc = mp.radius_circumscribed_circle(calculated_points) #радиус описанной окружности

            x1 = 520 + (center_cc[0] - radius_cc)*K
            y1 = 320 - (center_cc[1] - radius_cc)*K
            x2 = 520 + (center_cc[0] + radius_cc)*K
            y2 = 320 - (center_cc[1] + radius_cc)*K

            center_ic = mp.center_inscribed_circle(calculated_points)  #центр вписанной окружности
            radius_ic = mp.radius_inscribed_circle(calculated_points)  #радиус вписанной окружности

            x3 = 520 + (center_ic[0] - radius_ic)*K
            y3 = 320 - (center_ic[1] - radius_ic)*K
            x4 = 520 + (center_ic[0] + radius_ic)*K
            y4 = 320 - (center_ic[1] + radius_ic)*K

            circumscribed_circle1 = canvas.create_oval(x1, y1, x2, y2, outline="green",
                fill="green", width=2)

            triangle_x1 = 520 + calculated_points[0][0]*K
            triangle_y1 = 320 - calculated_points[0][1]*K
            triangle_x2 = 520 + calculated_points[1][0]*K
            triangle_y2 = 320 - calculated_points[1][1]*K
            triangle_x3 = 520 + calculated_points[2][0]*K
            triangle_y3 = 320 - calculated_points[2][1]*K

            triangle1 = canvas.create_polygon([triangle_x1,triangle_y1],[triangle_x2,triangle_y2],
                                  [triangle_x3,triangle_y3],fill="red")

            inscribed_circle1 = canvas.create_oval(x3[0], y3[0], x4[0], y4[0], outline="blue",
                fill="blue", width=2)

            lb = Label(answer, text='РЕЗУЛЬТИРУЮЩИЕ ТОЧКИ')
            lb.place(x=110, y = 10)

            indexes = [0,0,0]
            for i in range(len(calculated_points)):
                indexes[i] = all_points.index(calculated_points[i])

            circumscribed_circle = mp.square_circumscribed_circle(calculated_points[0], calculated_points[1], calculated_points[2])
            inscribed_circle = mp.square_inscribed_circle(calculated_points[0], calculated_points[1], calculated_points[2])

            table_result_points = DataFrame(calculated_points,columns=['x','y'],index=indexes)
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

            create_points(K,all_points)

            answer.mainloop()
        else:
            create_points(K,all_points)
            error_window('ВЫРОЖДЕННЫЙ ТРЕУГОЛЬНИК!')
    elif len(all_points) > 0 and len(all_points) < 3:
        create_points(K,all_points)
        error_window('НЕДОСТАТОЧНОЕ КОЛИЧЕСТВО ТОЧЕК!')



def filtered_data(points_array):
    '''Преобразует информацию к нормальному виду для добавления'''

    entry_points.delete(0, 'end')

    points_array = list(points_array.split(';'))

    for i in range(len(points_array)):
        if points_array[i] != '':
            if len(points_array[i].split(' ')) <= 1 \
                    and len(points_array[i].split(',')) == 2:
                if points_array[i].split(',')[0] != '' and points_array[i].split(',')[1] != '' \
                        and [float(points_array[i].split(',')[0]), \
                                float(points_array[i].split(',')[1])] not in all_points:
                    all_points.append([float(points_array[i].split(',')[0]),
                                float(points_array[i].split(',')[1])])



def start(points_array):
    '''Обертка для функций фильтрации и вычисления треугольников'''

    filtered_data(points_array)
    get_points(all_points)


def delete_all_points():
    '''Удаляет все введенные ранее точки'''

    clear()
    all_points.clear()


def add_and_reset(points_array):
    '''Добавляет точки и перевычисляет'''


    if points_array != '':
        clear()
        start(points_array)
    else:
        error_window('ВЫ НИЧЕГО НЕ ВВЕЛИ!')


def delete_points(points_array):
    '''Удаляет заданные точки'''

    if points_array != '':
        entry_points.delete(0, 'end')
        points_array = list(points_array.split(';'))
        points_arr = []
        count = 0

        for i in range(len(points_array)):
            if points_array[i] != '':
                points_arr.append([float(points_array[i].split(',')[0]),
                                   float(points_array[i].split(',')[1])])

        for i in range(len(points_arr)):
            if points_arr[i] in all_points:
                all_points.remove(points_arr[i])
                count += 1

        if count > 0:
            clear()
            get_points(all_points)
        else:
            error_window('ТАКОЙ ТОЧКИ НЕТ!')
    else:
        error_window('ВЫ НИЧЕГО НЕ ВВЕЛИ!')


def edit_points(points_array):
    '''Редактирует координаты введенной точки'''

    if points_array != '':
        entry_points.delete(0, 'end')
        points_array = list(points_array.split(':'))

        delete_array = []

        for i in range(len(points_array)):
            if points_array[i] != '':
                delete_array.append([float(points_array[i].split(',')[0]),
                                   float(points_array[i].split(',')[1])])

        if delete_array[0] in all_points:
            all_points[all_points.index(delete_array[0])] = delete_array[1]
            clear()
            get_points(all_points)
        else:
            error_window('ТАКОЙ ТОЧКИ НЕТ!')
    else:
        error_window('ВЫ НИЧЕГО НЕ ВВЕЛИ!')



root = Tk()
root.title('My app')
root.geometry('1320x640')

global all_points
global array_points
all_points = []
array_points = []

canvas = Canvas(root, width=1040, height=640, bg='#002')
canvas.pack(side = 'right')

q = -500
for y in range(21):
    k = 50 * y
    canvas.create_line(20+k,620,20+k,20,width=1,fill = '#191938')
    if y != 20 and y != 0:
        canvas.create_line(20+k,310,20+k,315,width=1,fill='white')
    q += 50

q = -300
for x in range(13):
    k = 50 * x
    canvas.create_line(20,20+k,1020,20+k,width=1,fill = '#191938')
    if x != 12 and x != 0: 
        canvas.create_line(510,20+k,515,20+k,width=1,fill='white')
    q += 50

canvas.create_line(520,20,520,620,width=1,arrow=FIRST,fill='white') #ось У
canvas.create_line(20, 320, 1020, 320,width=1,arrow=LAST, fill='white') #ось X
canvas.create_text(500,300,text='0',fill='white')



label_entry = Label(root, text="Введите точки в \nпредложенном формате: X,Y\nразделяя их ';'")
label_entry.place(x = 30, y = 10)
label_points = Label(root, text='Точки X,Y: ')
label_points.place(x = 10, y = 100)

entry_points = Entry(root)
entry_points.place(x=10, y=120)

btn_calc = Button(root, text='Рассчитать')
btn_calc.bind('<Button-1>', lambda event: start(str(entry_points.get())))
btn_calc.place(x = 10, y = 150)

btn_tab = Button(root, text='Вывести таблицу значений')
btn_tab.bind('<Button-1>', lambda event: table_t(all_points))
btn_tab.place(x = 10, y = 210)

text_tab = Label(root,text="Выводит таблицу со \nзначениями всех точек",justify="left")
text_tab.place(x=21, y=240)

btn_clean = Button(root, text='Удалить все точки')
btn_clean.bind('<Button-1>', lambda event: delete_all_points())
btn_clean.place(x = 10, y = 290)

text_clean = Label(root,text="Удаляет все ранее \nзаданные точки",justify="left")
text_clean.place(x=21, y=320)

btn_add = Button(root, text='Добавить точки')
btn_add.bind('<Button-1>', lambda event: add_and_reset(str(entry_points.get())))
btn_add.place(x=10, y= 370)

text_add = Label(root,text="Добавляет точку или точки \nвведенные в поле выше\nпри вводе одной"
                           " точки \nзаканчивать ;",justify="left")
text_add.place(x=21, y=400)

btn_add = Button(root, text='Удалить точку(и)')
btn_add.bind('<Button-1>', lambda event: delete_points(str(entry_points.get())))
btn_add.place(x=10, y= 480)


text_add = Label(root,text="Удаляет заданную точку\n(введите координаты в \nполе выше)",justify="left")
text_add.place(x=21, y=510)

btn_add = Button(root, text='Редактировать точку')
btn_add.bind('<Button-1>', lambda event: edit_points(str(entry_points.get())))
btn_add.place(x=10, y= 580)

text_add = Label(root,text="Редактирует заданную точку\n(введите координаты в формате:\n "
                           "координаты точки которую \nхотите изменить:новые \nкоординаты заданной точки)",
                 justify="left")
text_add.place(x=21, y=610)


root.mainloop()
