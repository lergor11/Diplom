import string

points = {}
edges = {}
writInFile = 0
array = {}
arraypoint = {}
pointsoutside = {}
kol = 0
def get_key(d, value):
    list = ""
    for k, v in d.items():
        if v == value:
            list += str(k)
            addarraypoint(k[0], k[1])
            addarraypoint(k[1], k[0])

    return list

def addline(a, b):
    if a > b:
        a, b = b, a
    try:
        array[a, b] += 1
    except KeyError:
        array[a, b] = 1

def proc(line):
        line = [line[i:i + 8] for i in range(0, len(line), 8)]
        i = 0
        while i < 10:
            line[i] = int(line[i])
            i += 1
        i = 0
        while i < 10:

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

def addarraypoint(x,y):
    list = (arraypoint.setdefault(x))
    if(arraypoint.get(x)==None):
        list = [y]
    else:
        if(list.count(y)==0):
            list.append(y)
    arraypoint.update({x: list})


def valdotter():
    for a in arraypoint:
        list = (arraypoint.setdefault(a))
        while len(list)>0:
            b = list.pop()
            a = str(a)
            b = str(b)
            lineab(a, b)

def lineab(a, b):
    a = float(a)
    b = float(b)
    xyz1 = (points.setdefault(a))
    xyz2 = (points.setdefault(b))
    z1 = round(xyz1[0],8)
    y1 = round(xyz1[1],8)
    x1 = round(xyz1[2],8)
    z2 = round(xyz2[0],8)
    y2 = round(xyz2[1],8)
    x2 = round(xyz2[2],8)
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
    testpoint(x3, y3, z3)



def testpoint(x, y, z, kol=None):
    flag = 0
    for a in points:
        list = (points.setdefault(a))
        xd = round(list[0],4)
        yd = round(list[1],4)
        zd = round(list[2],4)
        if(x==xd and y==yd and z==zd):
            flag = 1
    if(flag==0):
        kol=len(pointsoutside)
        kol+=kol
        list = (x,y,z)
        pointsoutside[kol] = list

file_name = r"balka2.k"     # открываем фаил на чтение (временно для удобства берем Shar)
with open(file_name) as file:     # закрываем фаил как только будет конец
    for line in file.readlines():
        # читаем построчно
        list = []
        if "$#" in line:
            continue
        if "$" in line:     # не ечатаем, если есть разделители и после них
            writInFile = 0
        if writInFile == 1: # печатаем, если нашли начало файла
            line = "        " + line # временные костыли

            line = [line[i:i+16] for i in range(0, len(line), 16)] # разделяем строку
            i = 0
            while i < 4:
                line[i] = float(line[i])
                if i > 0:
                    list.append(line[i])
                i += 1
            points[line[0]] = list
        if writInFile == 2:  # печатаем, если нашли начало файла
            proc(line)
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
