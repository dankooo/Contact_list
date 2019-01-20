import pickle
import os

contacts = 'contacts.data'
db = {}
if os.path.getsize(contacts)>0:
	with open(contacts, 'rb') as f:
		db = pickle.load(f)
else: 
	with open (contacts, 'wb') as f:
			pickle.dump(db,f)


class contact:
    def __init__(self, name,phone):
        self.name = name
        self.phone = phone
    def vcb(self, db):
        db[self.name] = {'name':self.name,'phone number':self.phone}


class phonebook(contact):
    def __init__ (self, name, phone):
        contact.__init__(self, name, phone)
    def save(self, cont, db, file):
        with open(contacts, 'rb') as f:
            db = pickle.load(f)