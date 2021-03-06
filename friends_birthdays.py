def add_birthdays(user_birthdays):
	add_records = input('Add records?(yes/no): ')
	PICKS = ['YES','Yes','NO','No']
	if add_records.title() not in PICKS:
		print('Invalid input!')
	else:	
		while add_records.title() == 'Yes' or add_records == 'YES':
			name = input('Enter your name: ')
			name = name.title()
			if name not in user_birthdays:
				birthday_date = input('Enter your birthday(dd/mm/yyyy): ')
				user_birthdays[name] = birthday_date
			else:
				print('Name already exists')	
			add_records = input('\nAdd more records?(yes/no): ')

def lookup_birthdays(user_birthdays):
	print('You can either look up user\'s name or user\'s birthday')
	print('+ Enter 1 to look up user\'s birthday[using user\'s name]')
	print('+ Enter 2 to look up user\'s name[using user\'s birthday]')
	try:
		choice = int(input('Enter your choice: '))
	except ValueError:
		print('Invalid input!')	
	else:	
		if choice == 1:
			user_name = input('Enter user\'s name: ')
			if user_name.title() in user_birthdays:
				for user,date in user_birthdays.items():
					if user_name.title() == user:
						print(f'{user} : {date}')
			else:
				print('Name not found')
		elif choice == 2:
			user_bdate = input('Enter user\'s birthday(dd/mm/yyyy): ')
			if user_bdate in user_birthdays.values():	
				for user,date in user_birthdays.items():
					if user_bdate == date:
						print(f'{user} : {date}')
			else:
				print('Birthday not found')
		else:
			print('Invalid input!')		

def change_birthdays(user_birthdays):
	print('You can either modify a user\'s birthday or user\'s name')
	print('+ Enter 1 to modify a user\'s birthday[using user\'s name]')
	print('+ Enter 2 to modify the user\'s name[using user\'s birthday]')
	try:
		choice = int(input('Enter your choice: '))	
	except ValueError:
		print('Invalid input!')
	else:		
		if choice == 1:
			user_name = input('Enter user\'s name: ')
			if user_name.title() in user_birthdays:
				new_bdate = input('Enter the new birthday(dd/mm/yyyy): ')
				user_birthdays[user_name.title()] = new_bdate
				print('Birthday has been modified')
			else:
				print('Name not found')
		elif choice == 2:
			user_bdate = input('Enter user\'s birthday(dd/mm/yyyy): ')	
			if user_bdate in user_birthdays.values():
				for key in list(user_birthdays):
					if user_birthdays[key] == user_bdate:
						user_birthdays.pop(key)
				new_username = input('Enter new username: ')
				user_birthdays[new_username.title()] = user_bdate
				print('Name has been modified')
			else:
				print('Birthday not found')
		else:
			print('Invalid input!')		

def delete_birthdays(user_birthdays):
	name = input('Enter user\'s name: ')
	if name.title() in user_birthdays:
		del user_birthdays[name.title()]
		print(f'{name.title()}\'s record has been deleted!')
	else:
		print('Name not found')

def menu_choice():
	print('\n\t\tMenu')
	print('1. Look up a birthday')
	print('2. Add a new birthday')
	print('3. Change a birthday')
	print('4. Delete a birthday')
	print('5. Quit the program')
	print('Make a selection from the menu:')
	CHOICES = [1,2,3,4,5]
	try:
		choice = int(input('\nEnter a valid choice: '))
	except ValueError:
		print('Invalid input!')	
	else:	
		if choice not in CHOICES:
			print('Invalid input!')
		else:	
			return choice	

def main():
	user_birthdays = {}
	user_choice = ''	
	QUIT = 5
	while user_choice != QUIT:
		user_choice = menu_choice()		
		if user_choice == 1:
			lookup_birthdays(user_birthdays)
		elif user_choice == 2:
				add_birthdays(user_birthdays)
		elif user_choice == 3:
			change_birthdays(user_birthdays)
		elif user_choice == 4:
			delete_birthdays(user_birthdays)
		elif user_choice == 5:
			print('You just ended the program..')	

main()


































