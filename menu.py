import program


def button_click():
    workNotebook = 1
    while (workNotebook):
        print(
            f'МЕНЮ: \n\
                1 - Добавить заметку \n\
                2 - Посмотреть заметку \n\
                3 - Обновить заметку \n\
                4 - Посмотреть все заметки \n\
                5 - Удалить заметку \n\
                6 - Отсортировать заметки по дате \n\
                7 - Закрыть блокнот\n')
        answer = int(input("Введите номер пункта меню: "))
        if answer == 1:
            data = program.get_note()
            program.write_data(data)
        if answer == 2:
            program.showOne_data()
        if answer == 3:
            program.update_data()
        if answer == 4:
            program.show_data()
        if answer == 5:
            program.delete_data()
        if answer == 6:
            program.sorted_data()
        if answer == 7:
            workNotebook = 0
            print('Блокнот закрыт')