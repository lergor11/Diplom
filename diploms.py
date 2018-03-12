points = {}
edges = {}
writInFile = 0
array = {}

def get_key(d, value):
    list = ""
    for k, v in d.items():
        if v == value:
            list += str(k)
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
            while i < 3:
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
print(edges)
print(array)
print(get_key(array, 4))