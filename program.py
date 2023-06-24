import csv
from datetime import datetime
import pandas as pd
import uuid

# создание заметки


def get_note():
    id = uuid.uuid4()
    name = input('Заголовок: ')
    desc = input('Содержание: ')
    now = datetime.now()
    data = {"Идентификатор": id, "Заголовок": name,
            "Описание": desc, "Дата": now}
    return data

# запись в файл


def write_data(data):
    columns = ["Идентификатор", "Заголовок", "Описание", "Дата"]
    with open("note.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writerow(data)
        file.close()
    print('Заметка добавлена')

# чтение из файла


def show_data():
    with open("note.csv", "r", newline="") as file:
        reader = list(csv.reader(file))
        for row in reader:
            columns = ["Идентификатор", "Заголовок",
                       "Описание", "Дата"]
            i = 0
            while i < len(row):
                while i < len(columns):
                    data_str = f'{columns[i]}: {row[i]}'
                    print(data_str)
                    i += 1
            print()

# показать одну заметку


def showOne_data():
    dataName = input('Введите заголовок заметки: ')
    with open("note.csv", "r", newline="") as file:
        reader = list(csv.reader(file))
        for row in reader:
            columns = ["Идентификатор", "Заголовок",
                       "Описание", "Дата"]
            if dataName in row:
                i = 0
                while i < len(row):
                    while i < len(columns):
                        data_str = f'{columns[i]}: {row[i]}'
                        print(data_str)
                        i += 1
        print()

# проверка введенных пользователем данных


def check(num, reader):
    incorrect = (num.isdigit() == 0) or (int(num) not in range(
        1, len(reader) + 1))
    while incorrect:
        print('Такого номера нет')
        num = input('Введите другой номер заметки: ')
        return check(num, reader)
    return int(num)

# редактирование заметки


def update_data():
    with open("note.csv", "r", newline="") as file:
        reader = list(csv.reader(file))
        num = input('Введите номер заметки: ')
        num = check(num, reader)
    df = pd.read_csv("note.csv", header=None, encoding='cp1251')
    flag = int(input('Что хотите изменить? 1 - заголовок, 2 - описание: '))
    if flag == 1:
        df.loc[num - 1, 2-1] = input('Введите новый заголовок: ')
    if flag == 2:
        df.loc[num - 1, 3-1] = input('Введите новое описание: ')
    df.loc[num - 1, 4-1] = datetime.now()
    df.to_csv("note.csv", header=None, index=False, encoding='cp1251')
    print("Заметка отредактирована")

# удалить заметку


def delete_data():
    with open("note.csv", "r", newline="") as file:
        reader = list(csv.reader(file))
        num = input('Введите номер заметки: ')
        num = check(num, reader)
        del reader[num - 1]
        file.close()
    with open("note.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(reader)
        file.close()
    print("Заметка удалена")

# сортировка по дате


def sorted_data():
    with open("note.csv", "r", newline="") as file:
        reader = list(csv.reader(file))
        reader = sorted(reader, key=lambda data: data[3])
        for row in reader:
            columns = ["Идентификатор", "Заголовок",
                       "Описание", "Дата"]
            i = 0
            while i < len(row):
                while i < len(columns):
                    data_str = f'{columns[i]}: {row[i]}'
                    print(data_str)
                    i += 1
            print()