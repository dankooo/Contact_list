import pickle
import os
import pprint

cont_list = 'cont_list.data'
db = {}
if os.path.getsize(cont_list) > 0:
    with open(cont_list, 'rb') as f:
        db = pickle.load(f)
else:
    with open(cont_list, 'wb') as f:
        pickle.dump(db, f)


class Contacts:
    def __init__(self, name, phone_number):
        if not name or name.isspace():
            self.name = phone_number
            self.phone_number = phone_number
        else:
            self.phone_number = phone_number
            self.name = name
        print('создан контакт "{0}", номер телефона: {1}'.format(
            self.name, self.phone_number))


def add_contact():
    contact = Contacts(input('Введите имя: ').strip(),
                       input('Введите номер телефона: ').strip())
    db[contact.name] = {'Имя': contact.name,
                        'Номер телефона': contact.phone_number}
    with open(cont_list, 'wb') as f:
        pickle.dump(db, f)
    input('Нажмите любую клавишу')
    print('\n')


def edit_cont():
    with open(cont_list, 'rb') as f:
        db = pickle.load(f)
    contact = input('Введите имя контакта: ').strip()
    print(contact, '=>', db[contact])
    key = input(
        'Введите, какое значение нужно изменить/добавить \
		(Имя, Номер телефона и т.д.): ').strip()
    if key == 'Имя':
        subkeys = db[contact]
        del db[contact]
        value = input('Введите значение: ').strip()
        subkeys[key] = value
        db[value] = subkeys
        print(value, '=>', db[value])
    else:
        subkeys = db[contact]
        del db[contact]
        value = input('Введите значение: ')
        subkeys[key] = value
        db[contact] = subkeys
        print(contact, '=>', db[contact])
    with open(cont_list, 'wb') as f:
        pickle.dump(db, f)
    input('Нажмите любую клавишу')
    print('\n')


def show_contacts():
    if os.path.getsize(cont_list) > 0:
        with open(cont_list, 'rb') as f:
            db = pickle.load(f)
        print('Записано {0} контактов'.format(len(db)))
        pprint.pprint(db)
    else:
        print('Записано {0} контактов'.format(len(db)))
    input('Нажмите любую клавишу')
    print('\n')


def del_contact():
    contact = input('Введите имя контакта: ')
    wrn = input(
        'Вы действительно хотите удалить контакт "{0}"? [Y/N]'.format(contact))
    if wrn == 'N':
        return
    elif wrn == 'Y':
        with open(cont_list, 'rb') as f:
            db = pickle.load(f)
    else:
        return
    del db[contact]
    print('Записано {0} контактов'.format(len(db)), end='\n')

    with open(cont_list, 'wb') as f:
        pickle.dump(db, f)


s = 1
while s > 0:
    s = int(input('''Контакты
Меню:
1) Создать новый контакт
2) Изменить контакт
3) Список контактов
4) Удалить контакт
0) Завершить работу
Введите номер пункта меню: '''))
    if s == 0:
        break
    menu = {1: add_contact, 2: edit_cont, 3: show_contacts, 4: del_contact}
    menu[s]()
