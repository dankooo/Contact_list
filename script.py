import pickle

cont_list='cont_list.data'

class contact: 
	cont = {}
	contacts_count = 0
	def __init__(self,name,phone_number):
		self.name = name
		self.phone_number = phone_number
		print('создан контакт "{0}", номер телефона: {1}'.format(self.name, self.phone_number))
		contact.contacts_count +=1
		print('В записной книжке {0} контактов'.format(contact.contacts_count))
		contact.cont[self.name] = self.phone_number
		print(contact.cont)
		'''f = open(cont_list, 'wb')
		pickle.dump('Количество контактов: ',contact.contacts_count,'\nКонтакты:',contact.cont,'\n',f)
		f.close()
		f = open(cont_list, 'rb')   #тут у меня говно
		read_list = pickle.load(f)
		print(read_list)
		f.close()'''

	

def add_contact():
	s =[]
	s.append(input('Введите Имя контакта: '))
	s.append(input('Введите номер телефона: '))
	contact(s[0],s[1])

def edit_contact():
	pass

def find_contact():
	pass

def delete_contact():
	pass

s = int(input('input num'))
menu = {1:add_contact, 2:edit_contact, 3:find_contact, 4:delete_contact}
menu[s]()