def menu():
    print("1. Вывод телефонной книги")
    print("2. Сохранение контакта")
    print("3. Поиск по фамилии")
    print("4. Изменение контакта")
    print("5. Удаление контакта") 

def show_phonebook(data):
    for i in data:
        print(i)