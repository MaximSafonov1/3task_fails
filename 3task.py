with open('1.txt', encoding='utf-8') as file_1:
    length_1 = 0
    list_1 = []
    for line in file_1:
        length_1 += 1
        list_1.append(line)


with open('2.txt', encoding='utf-8') as file_2:
    length_2 = 0
    list_2 = []
    for line in file_2:
        length_2 += 1
        list_2.append(line)


with open('3.txt', encoding='utf-8') as file_3:
    length_3 = 0
    list_3 = []
    for line in file_3:
        length_3 += 1
        list_3.append(line)

print(f' Длина 1 текста = {length_1}')
print(f' Длина 2 текста = {length_2}')
print(f' Длина 3 текста = {length_3}')


with open('4.txt', 'w', encoding='utf-8') as file_4:
    file_4.write('2.txt\n')
    file_4.write(str(length_2) + '\n')
    for line in list_2:
        file_4.write(line)
    file_4.write('\n\n1.txt\n')
    file_4.write(str(length_1) + '\n')
    for line in list_1:
        file_4.write(line)
    file_4.write('\n\n3.txt\n')
    file_4.write(str(length_3) + '\n')
    for line in list_3:
        file_4.write(line)