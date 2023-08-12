"""
w - перезапись
r - чтение
a - дозапись
encodinf = "UTF-8"

справочник должен содержать данные:
имя, телефон, комментарий
хранится в файле phone.txt
пример записи - Кирилл; 899999999; Семинары

выводить все контакты на экран
добавить контакт
удалить контакт
изменить контакт
найти контакт конкретный
открыть сохранить файл целиком
выход из меню
можно сделать копию, поработать и сохранить
"""

"""
______________________________________________________
Данный телефонный справочник разработан группой студентов:
Коротеев Дмитрий
Иван Андронов
Арман Джамбулов
______________________________________________________
"""

file = 'Семинары Python\seminar8\phone.txt'

def add_contact(contact, file):
    with open(file, 'a', encoding='UTF-8') as add_c:
        add_c.write(f'\n{contact}')

def delete_contact(contact, file):
    with open(file, "r", encoding='UTF-8') as f:
        lines = f.readlines()
    with open(file, "w", encoding='UTF-8') as f:
        for line in lines:
            if line != contact:
                f.write(line)

def change_contact(file):
    with open(file, "r", encoding='UTF-8') as f:
        with open(file, "r", encoding='UTF-8') as f:
            lines = f.readlines()
            for i in range(1, len(lines)):
                print(f"{i}.", lines[i])
        number = int(input("Введите порядковый номер контакта который хотите изменить: "))
        changes = input("Введите изменение в формате <Имя; Номер; Комментарий> : ")
        lines[number] = (f"{changes}\n")
    with open(file, "w", encoding='UTF-8') as f:
        for line in lines:
            f.write(line)

def find_contact(file):
    with open(file, "r", encoding='UTF-8') as f:
        lines = f.readlines()
        name = input("Введите параметр поиска (имя, номер, комментарий): ")
        for line in lines:
            if name in line.split(';'):
                print(line)
        else:
            print("Такого контакта нет")

def all_contacts(file):
    with open(file, "r", encoding='UTF-8') as f:
            lines = f.readlines()
            print("Список контактов \n")
            for i in range(1, len(lines)):
                print(f"{i}.", lines[i])

action = 0
while action != 6:
    print(
        """
        _____Меню_____\n
    1. Добавить контакт
    2. Удалить контакт
    3. Изменить контакт
    4. Найти контакт
    5. Показать все контакты
    6. выход из меню
    """
    )
    action = int(input('Введите номер действия: '))
    if action == 1:
        name = input("Введите имя контакта: ")
        number = input("Введите номер контакта: ")
        comment = input("Введите комментакрий к контакту: ")
        contact = f"{name};{number};{comment}"
        add_contact(contact, file)
        print(f"\nКонтакт '{name};{number};{comment}' успешно добавлен.\n")

    if action == 2:
        with open(file, "r", encoding='UTF-8') as f:
            lines = f.readlines()
            data = {}
            for i in range(1, len(lines)):
                data[i] = lines[i]
                print(f"{i}.", lines[i])
        number = int(input("Введите порядковый номер контакта, который хотите удалить: "))
        delete_contact(data[number], file)
        print(f"\nКонтакт удален. \n")

    if action == 3:
        change_contact(file)

    if action == 4:
        find_contact(file)
    
    if action == 5:
        all_contacts(file)
