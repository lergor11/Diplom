points = {}
edges = {}
writInFile = 0

file_name = r"SHAR_P.k" # открываем фаил на чтение (временно для удобства берем Shar)
with open(file_name) as file:#закрываем фаил как только будет конец
    for line in file.readlines():
        # читаем построчно
        list = []
        if "$" in line: # не ечатаем, если есть разделители и после них
            writInFile = 0
        if writInFile == 1: # печатаем, если нашли начало файла
            line = "        " + line # временные костыли

            line = [line[i:i+16] for i in range(0, len(line), 16)] #разделяем строку
            i = 0
            while i < 3:
                line[i] = float(line[i])
                if i > 0:
                    list.append(line[i])
                i += 1
            points[line[0]] = line[1:4]
        if writInFile == 2:  # печатаем, если нашли начало файла
            line = [line[i:i + 8] for i in range(0, len(line), 8)]  # разделяем строку
            i = 0
            while i < 10:
                line[i] = int(line[i])
                if i > 0:
                    list.append(line[i])
                i += 1
            edges[line[0]] = list
        if "*NODE" in line: #печатаем узлы если нашли слово NODE
            writInFile = 1
        if "*ELEMENT_SOLID" in line:  # печатаем грани если нашли слово ELEMENT_SOLID
            writInFile = 2
print(edges)

