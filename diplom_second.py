
points = {}
edges = {}
writInFile = 0
array = {}
setka = {}
side = {}


def proc(line):
    line = [line[i:i + 8] for i in range(0, len(line), 8)]
    i = 0
    while i < 10:
        line[i] = int(line[i])
        i += 1
    sides = {1: sorted([line[2], line[3], line[4], line[5]]),
             2: sorted([line[2], line[3], line[7], line[6]]),
             3: sorted([line[3], line[4], line[8], line[7]]),
             4: sorted([line[6], line[7], line[8], line[9]]),
             5: sorted([line[2], line[5], line[9], line[6]]),
             6: sorted([line[4], line[5], line[9], line[8]]),}


    setka.update({line[0]: sides})

def search(setka):
    for i in setka.values():
        for k in i.values():
            y = tuple(k)
            if array.get(y) is None:
                array.update({y: 1})
            else:
                count = array.get(y)
                array.update({y: count+1})




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

print(setka)
search(setka)
print(array)