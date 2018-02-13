writInFile =0;
file_name = r"SHAR_P.k"# открываем фаил на чтение (временно для удобства берем Shar)
with open(file_name) as file:#закрываем фаил как только будет конец
    for line in file.readlines():#читаем построчно
        if "$" in line:# не ечатаем, если есть разделители и после них
            writInFile = 0
        if writInFile == 1:# печатаем, если нашли начало файла
            line="        "+line #временные костыли
            print([line[i:i+16] for i in range(0, len(line), 16)]) #делим входной фаил на 16 равных частей
        if "*NODE" in line:#печатаем узлы если нашли слово NODE
            writInFile =1;


