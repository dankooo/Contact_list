import pickle
import os

cont_list='cont_list.data'
db ={}
if os.path.getsize(cont_list)>0:
	with open(cont_list, 'rb') as f:
		db = pickle.load(f)
else: 
	with open (cont_list, 'wb') as f:
			pickle.dump(db,f)

class contact: 
	cont = {}
	def __init__(self,name,phone_number,email):
		if not name or name.isspace():
			self.name = phone_number
			self.phone_number = phone_number
		else:
			self.phone_number = phone_number
			self.name = name
		self.email = email
		print('создан контакт "{0}", номер телефона: {1}, E-mail: {2}'.format(self.name, self.phone_number, self.email), end = '\n')
		contact.cont = {'Имя':self.name, 'Номер телефона':self.phone_number, 'E-mail':self.email}

		if os.path.getsize(cont_list)>0:
			with open(cont_list, 'rb') as f: 
				global db    
				db = pickle.load(f)
		
		db[self.name] = contact.cont
		print('Записано {0} контактов'.format(len(db)), end = '\n')


		with open (cont_list, 'wb') as f:
			pickle.dump(db,f)

	def del_cont(self, name):
		wrn = input('Вы действительно хотите удалить контакт "{0}"? [Y/N]'.format(self.name))
		if wrn == 'N':
			return
		elif wrn == 'Y':
			if os.path.getsize(cont_list)>0:
				with open(cont_list, 'rb') as f: 
					global db    
					db = pickle.load(f)
		else: return
		
		del db[self.name] 
		print('Записано {0} контактов'.format(len(db)), end = '\n')

		with open (cont_list, 'wb') as f:
			pickle.dump(db,f)

	def edit_cont(self, name, names_key):

		if os.path.getsize(cont_list)>0:
			with open(cont_list, 'rb') as f: 
				global db    
				db = pickle.load(f)
		for keys in db:
			if self.name == keys:
				subkeys = db[keys]
				del db[self.name]
				key = input('Введите значение: ')
				subkeys[self.names_key] = key
				db[key] = subkeys
				break
		else:
			db[self.name][self.names_key] = input('Введите значение: ')
		print('Контакт изменен:',key, '=>', db[key], end = '\n')

		with open (cont_list, 'wb') as f:
			pickle.dump(db,f)	

	def find_cont(self, value):
		if os.path.getsize(cont_list)>0:
			with open(cont_list, 'rb') as f: 
				global db    
				db = pickle.load(f)
		for values in db:
			if values == self.value:
				print(self.value, '=>', db.get(self.value), end = '\n')
			else: print('Контакт не найден')


def show_contacts():
	if os.path.getsize(cont_list)>0:
		with open(cont_list, 'rb') as f:
			db = pickle.load(f)
			print('Записано {0} контактов'.format(len(db)), end='\n')
		for keys in db:
			print(keys, '=>', db[keys])
	else: print('Записано {0} контактов'.format(len(db)), end='\n')
	print('\n')
	input('Нажмите любую клавишу')
	print('\n')
	
def add_contact():
	s =[]
	s.append(input('Введите имя: '))
	inpt = input('Введите номер телефона: ')
	while not inpt.isdigit():
		print('Повторите ввод', end = '\n')
		inpt = input('Введите номер телефона: ')
	s.append(inpt)
	s.append(input('Введите E-mail: '))
	contact(s[0],s[1],s[2])
	print('\n')
	input('Нажмите любую клавишу')
	print('\n')

def edit_contact():
	s =[]
	s.append(input('Введите Имя контакта: '))
	s.append(input('Введите, какое значение нужно изменить (Имя, Номер телефона, E-mail): '))
	contact.edit_cont(s[0],s[1])
	print('\n')
	input('Нажмите любую клавишу')
	print('\n')


def find_contact():
	s = input('Введите значение: ')
	contact.find_cont(s)
	print('\n')
	input('Нажмите любую клавишу')
	print('\n')


def delete_contact():
	s = input('Введите Имя контакта: ')
	contact.del_cont(s)
	print('\n')
	input('Нажмите любую клавишу')
	print('\n')


s = 1
while s !=0:
	s = int(input('''Контакты
	
Меню:
1) Создать новый контакт
2) Изменить контакт
3) Найти контакт
4) Удалить контакт
5) Список контактов
0) Завершить работу

Введите номер пункта меню: '''
	))
	print('\n')
	if s == 0:
		break
	menu = {1:add_contact, 2:edit_contact, 3:find_contact, 4:delete_contact, 5:show_contacts}
	menu[s]()
