def menu():
    print()
    print("Меню:")
    print("1. Вывод телефонной книги")
    print("2. Добавление контакта")
    print("3. Поиск по фамилии")
    print("4. Изменение контакта")
    print("5. Удаление контакта") 
    print("0. Выход из справочника")


def show_phonebook(data):
    for i in data:
        print(i)


def output(res):
    print(res)