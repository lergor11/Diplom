import string

points = {}
edges = {}
writInFile = 0
array = {}
arraypoint = {}
pointsoutside = {}
kol = 0
def get_key(d, value): # функция для получения сколько у нас отрезков
    list = ""
    for k, v in d.items():
        if v == value:
            list += str(k)
            addarraypoint(k[0], k[1]) # этой функцией мы будем просматривать, от 1 точке сколько отходят отрезков
            addarraypoint(k[1], k[0])

    return list

def addline(a, b): # функция для просмтра если первый аргумент больше фторого то меняем местами (для читаемости)
    if a > b:
        a, b = b, a
    try:
        array[a, b] += 1
    except KeyError:
        array[a, b] = 1

def proc(line):
        line = [line[i:i + 8] for i in range(0, len(line), 8)] #разбиваем нашу сетку на элементов
        i = 0
        while i < 10:
            line[i] = int(line[i]) #превращаем наши точки из str в инт
            i += 1
        i = 0
        while i < 10: # перебираем наши точки

            if i > 0:
                list.append(line[i])
            if i > 1:
                if i == 2:
                    addline(line[2], line[3])
                    addline(line[2], line[6])
                if i == 3:
                    addline(line[3], line[4])
                    addline(line[3], line[7])
                if i == 4:
                    addline(line[4], line[8])
                    addline(line[4], line[5])
                if i == 5:
                    addline(line[5], line[9])
                    addline(line[5], line[2])
                if i == 6:
                    addline(line[6], line[7])
                    addline(line[6], line[9])
                if i == 7:
                    addline(line[7], line[8])
                if i == 8:
                    addline(line[8], line[9])
            i += 1

def addarraypoint(x,y):  # этой функцией мы будем просматривать, от 1 точке сколько отходят отрезков
    list = (arraypoint.setdefault(x))
    if(arraypoint.get(x)==None):
        list = [y]
    else:
        if(list.count(y)==0):
            list.append(y)
    arraypoint.update({x: list})


def valdotter(): # этой функцией мы будем перебирать массив , и отдавать  отрезки
    for a in arraypoint:
        list = (arraypoint.setdefault(a))
        #print(list)
        while len(list)>0:
            b = list.pop()
            a = str(a)
            b = str(b)
            lineab(a, b)
            #print(a,b)

def lineab(a, b): # вычисляем следующую точку.
    a = float(a)
    b = float(b)
    xyz1 = (points.setdefault(a))
    xyz2 = (points.setdefault(b))
    #print(xyz1,xyz2) #[0.0, 0.0, 0.0] [0.08333334, 0.0, 0.0]
    x1 = round(xyz1[0],8)
    y1 = round(xyz1[1],8)
    z1 = round(xyz1[2],8)
    x2 = round(xyz2[0],8)
    y2 = round(xyz2[1],8)
    z2 = round(xyz2[2],8)
    #print(x1,y1,z1,x2,y2,z2) #0.0 0.0 0.0 0.08333334 0.0 0.0
    if(x1 == x2)and (y1 == y2):
        x3 = x1
        y3 = y2
        z3 = 2*z2 - z1
    if (x1 == x2) and (z1 == z2):
        x3 = x1
        y3 = 2 * y2 - y1
        z3 = z1
    if (y1 == y2) and (z1 == z2):
        x3 = 2 * x2 - x1
        y3 = y2
        z3 = z2
    x3 = round(x3, 4)
    y3 = round(y3, 4)
    z3 = round(z3, 4)
    #print(x3,y3,z3) #0.1667 0.0 0.0
    testpoint(x3, y3, z3)



def testpoint(x, y, z, kol=None):
    flag = 0
    kol = 0
    for a in points:

        list = (points.setdefault(a))

        xd = round(list[0],4)
        yd = round(list[1],4)
        zd = round(list[2],4)
        #print(x,y,z,xd,yd,zd) #0.1667 0.0 0.0 0.1667 0.0 0.0
        if(x==xd and y==yd and z==zd):
            flag = 1
            #print(x,y,z,xd,yd,zd)# 0.1667 0.0 0.0 0.1667 0.0 0.0
    if(flag==0):
        kol+=1
        list = (x,y,z)
        pointsoutside[kol] = list
        #print(x,y,z)#-0.0833 0.0 0.0

def eps(x,y,z):
    epselent = 0.833
    for a in points:
        list = (points.setdefault(a))

        xd = round(list[0], 4)
        yd = round(list[1], 4)
        zd = round(list[2], 4)
    ab = ((xd - x)^2 + (yd - y)^2 + (zd - z)^2)^(1/2)
    if(ab<epselent):
        print(x,y,z,"У НАС ОШИБКА, Хьюстон")

file_name = r"balka2.k"     # открываем фаил на чтение (временно для удобства берем Shar)
with open(file_name) as file:     # закрываем фаил как только будет конец
    for line in file.readlines():
        # читаем построчно
        list = []
        if "$#" in line:
            continue
        if "$" in line:     # не ечатаем, если есть разделители и после них
            writInFile = 0
        if writInFile == 1: # печатаем точки, если нашли начало файла
            line = "        " + line # временные костыли

            line = [line[i:i+16] for i in range(0, len(line), 16)] # разделяем строку
            i = 0
            while i < 4:
                line[i] = float(line[i])
                if i > 0:
                    list.append(line[i])
                i += 1
            points[line[0]] = list
        if writInFile == 2:  # печатаем сетку, если нашли начало файла
            proc(line)       # функция подсчета сетки
            edges[line[0]] = list




        if "*NODE" in line:  # печатаем узлы если нашли слово NODE
            writInFile = 1
        if "*ELEMENT_SOLID" in line:  # печатаем грани если нашли слово ELEMENT_SOLID
            writInFile = 2

(edges)
print(points)
print(get_key(array, 4))
print(get_key(array, 2))
get_key(array, 1)
print(arraypoint)
valdotter()
