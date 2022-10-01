# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

def list_elem(N):
    listNum = []
    for i in range(N):
        listNum.append(randint(-1 * N, N))
    return listNum


def find_position(list_n):
    file = open('file.txt', 'r')
    Lines = file.readlines()
    mult = 1
    for line in Lines:
        mult *= list_n[int(line)]
    return mult


list1 = list_elem(10)
print(list1)

mult_list_el = find_position(list1)
print(f'произведение элементов на указанных позициях (file.txt) = {mult_list_el}')