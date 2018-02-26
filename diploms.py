points = {}
edges = {}
writInFile = 0
array = {}

def get_key(d, value):
    list =""
    for k, v in d.items():
        if v == value:
            list+=k + "; "
    return list

file_name = r"balka2.k"     # открываем фаил на чтение (временно для удобства берем Shar)
with open(file_name) as file:     # закрываем фаил как только будет конец
    for line in file.readlines():
        # читаем построчно
        list = []
        if "$#" in line:
            continue
        if "$"  in line:     # не ечатаем, если есть разделители и после них
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
            line = [line[i:i + 8] for i in range(0, len(line), 8)]  # разделяем строку
            i = 0
            while i < 10:
                line[i] = int(line[i])
                if i > 0:
                    list.append(line[i])
                i += 1
            edges[line[0]] = list
            i = 2
            while i < 9:
                if array.get(str(line[i])+" " +str(line[i+1]))!= None or array.get(str(line[i+1])+" " +str(line[i]))!= None:
                    print(str(line[i])+" " +str(line[i+1]))

                    value = array.get(str(line[i]) + " " + str(line[i+1]))
                    if value == None:
                        value = array.get(str(line[i+1]) + " " + str(line[i]))
                    if line[i] <= line[i+1]:
                        array[str(str(line[i]) + " " + str(line[i + 1]))] = value + 1
                    else:
                        array[str(str(line[i+1]) + " " + str(line[i]))] = value + 1

                else:
                    array[str(str(line[i]) + " " + str(line[i + 1]))] = 1
                i += 1
            if array.get(str(9) + " " + str(line[2])) != None and array.get(str(line[2]) + " " + str(line[9])) != None:
                print(str(line[9]) + " " + str(line[2]))

                value = array.get(str(line[9]) + " " + str(line[2]))
                print(value)
                if value == None:
                    value = array.get(str(line[2]) + " " + str(line[9]))
                    print(value)
                if line[9] <= line[2]:
                    array[str(str(line[9]) + " " + str(line[2]))] = value + 1
                else:
                    print(value)
                    array[str(str(line[2]) + " " + str(line[9]))] = value + 1

            else:
                array[str(str(line[9]) + " " + str(line[2]))] = 1

        if "*NODE" in line:  # печатаем узлы если нашли слово NODE
            writInFile = 1
        if "*ELEMENT_SOLID" in line:  # печатаем грани если нашли слово ELEMENT_SOLID
            writInFile = 2
print(edges)
print(array)
print(get_key(array, 4))