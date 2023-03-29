
def read_phonebook():
    file = open('phonebook.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    return lines


def add_contact(first_name, last_name, telephone_number):
    file = open('phonebook.txt', 'a', encoding='utf-8')
    file.write(f"\n{first_name}\t{last_name}\t{telephone_number}")
    file.close
    return "Успешно добавлено"


def find_contact(last_name):
    file = open('phonebook.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    for ln in lines:
        if last_name in ln:
            file.close()
            return ln
    file.close()
    return "Контакт не найден"


def change_contact(last_name, changed_first_name, changed_last_name, changed_telephone_number):
    file = open('phonebook.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()

    for ln in lines:
        if last_name in ln:
            ln = "/n" + changed_first_name + "/t" + changed_last_name + "/t" + changed_telephone_number

    file = open('phonebook.txt', 'w', encoding='utf-8')
    lines = file.writelines(lines)
    file.close()

    return "Контакт успешно изменен"

def delete_contact(last_name):
    file = open('phonebook.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()

    for ln in lines:
        if last_name in ln:
            ln = ""

    file = open('phonebook.txt', 'w', encoding='utf-8')
    lines = file.writelines(lines)
    file.close()

    return "Контакт успешно удален"