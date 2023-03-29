## Имя Фамилия Телефон

# Каждая функция состоит из трех частей:
# 1я часть - ввод ответа от пользователя
# 2я часть - обработка ответа модулем model (чтение/запись из файла)
# 3я часть - вывод результата (res) модулем view

# Функции:
# 1. Вывод телефонной книги
# 2. Сохранение контакта
# 3. Поиск по фамилии
# 4. Изменение контакта
# 5. Удаление контакта

import view
import model

def run():
    ##view.greetings()
    while True:
        view.menu()
        answer = input("Ответ: ")

        if answer == "1":   ## вывести справочник
            data = model.read_phonebook()
            view.show_phonebook(data)

        elif answer == "2": ## Добавить контакт
            first_name = input("Введите Имя: ")
            last_name = input("Введите Фамилию: ")
            telephone_number = input("Введите номер телефона: ")
            res = model.add_contact(first_name, last_name, telephone_number)
            view.output(res)

        elif answer == "3": ## Найти контакт
            last_name = input("Введите Фамилию: ")
            data = model.find_contact(last_name)
            view.output(data)

        elif answer == "4": ## Изменение контакта
            last_name = input("Введите Фамилию: ")
            data = model.find_contact(last_name)
            if data != "Контакт не найден":
                changed_first_name = input("Введите новое Имя: ")
                changed_last_name = input("Введите новую Фамилию: ")
                changed_telephone_number = input("Введите новый номер телефона: ")
                res = model.change_contact(last_name, changed_first_name, changed_last_name, changed_telephone_number)
                view.output(res)
            else:
                view.output(data)

        elif answer == "5": ## Удаление контакта
            last_name = input("Введите Фамилию: ")
            data = model.find_contact(last_name)
            if data != "Контакт не найден":
                res = model.delete_contact(last_name)
                view.output(res)
            else:
                view.output(data)

        elif answer == "0": ## Выйти из программы
            return
        else:
            view.output("Неверный ответ")