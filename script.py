import pickle
import os

cont_list='cont_list.data'
db ={}

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
		print('создан контакт "{0}", номер телефона: {1}, E-mail: {2}'.format(self.name, self.phone_number, self.email))
		contact.cont = {'name':self.name, 'phone number':self.phone_number, 'E-mail':self.email}

		if os.path.getsize(cont_list)>0:
			with open(cont_list, 'rb') as f: 
				global db    
				db = pickle.load(f)
		
		db[self.name] = contact.cont
		print('Записано {0} контактов'.format(len(db)))


		with open (cont_list, 'wb') as f:
			pickle.dump(db,f)
			print(db)

	def del_cont(name):
		wrn = input('r u rly wanna del "{0}"? [Y/N]'.format(name))
		if wrn == 'N':
			return
		if os.path.getsize(cont_list)>0:
			with open(cont_list, 'rb') as f: 
				global db    
				db = pickle.load(f)
		
		del db[name] 
		print('Записано {0} контактов'.format(len(db)))

		with open (cont_list, 'wb') as f:
			pickle.dump(db,f)

	def edit_cont(name, names_key):

		if os.path.getsize(cont_list)>0:
			with open(cont_list, 'rb') as f: 
				global db    
				db = pickle.load(f)
				print(db)
			
		db[name][names_key] = input('Введите значение: ')
		print(db)

		with open (cont_list, 'wb') as f:
			pickle.dump(db,f)	

	def find_cont(value):
		if os.path.getsize(cont_list)>0:
			with open(cont_list, 'rb') as f: 
				global db    
				db = pickle.load(f)
		for values in db:
			if values == value:
				print(value, '=>', db.get(value))
		'''for key in db.keys():
			if key == value:'''
			#else: return

def add_contact():
	s =[]
	s.append(input('Введите имя: '))
	print (s)
	inpt = input('Введите номер телефона: ')
	while not inpt.isdigit():
		print('Повторите ввод')
		inpt = input('Введите номер телефона: ')
	s.append(inpt)
	print (s)
	s.append(input('Введите E-mail: '))
	print (s)
	contact(s[0],s[1],s[2])

def edit_contact():
	s =[]
	s.append(input('Введите Имя контакта: '))
	s.append(input('Введите, какое значение нужно изменить (name, phone number, E-mail): '))
	contact.edit_cont(s[0],s[1])


def find_contact():
	s = input('Введите значение: ')
	contact.find_cont(s)


def delete_contact():
	s = input('Введите Имя контакта: ')
	contact.del_cont(s)


s = 1
while s !=0:
	s = int(input('input num: '))
	if s == 0:
		break
	menu = {1:add_contact, 2:edit_contact, 3:find_contact, 4:delete_contact}
	menu[s]()
