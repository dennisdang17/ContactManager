
def menu():
	#loop flag
	running = True
	while running:
		print("=========================================")
		print("Welcome to the contacts book! ")
		print("1. Add new contact")
		print("2. View your address book")
		print("3. Search for a contact")
		print("4. Edit a contact's information")
		print("5. Delete a contact")
		print("6. Exit the program ")
		print("=========================================")
		try:
			choice = int(input("What would you like to do?: "))
			if choice > 6:
				print("ERROR: Invalid value please try again.")
			else:
				running = False
		except ValueError:
			print("ERROR: Invalid value please try again.")
	return choice

def addNew(book):
	contact = []
	name = input("Name: ")
	address = input("Address: ")
	number = input("Number: ")
	email = input("Email address: ")
	contact.append(name)
	contact.append(address)
	contact.append(number)
	contact.append(email)
	book.append(contact)

def display(book):
	#checks to see if list is empty
	if book == []:
		print("Your contacts are empty!")
	#displays each list by splitting them with a ","
	else:
		for contact in book:
			print(', '.join(contact))

def search(book):
	#bollean flag
	flag = False
	#checks to see if list is empty
	if book == []:
		print("Your contacts are empty!")
	else:
		name = input("What is their name?: ")
		#checks each value in each list of lists to check if the name matches. Once it does, it prints that whole contact out
		for i in book:
			for j in i:
				if j == name:
					#Changes boolean flag to true, meaning that the contact is the same.
					flag = True
					if flag == True:
						print(', '.join(i))
		#says the contact isnt there
		if flag == False:
			print("That contact does not exist.")

def modify(book):
	#boolean flag
	flag = False
	#checks to see if list is empty
	if book == []:
		print("Your contacts are empty!")
	else:
		name = input("What is their name?: ")
		choice = input("Enter 'n' to edit name, 'a' to edit address, 'p' to edit phone number, or 'e' to edit email address: ")
		if choice == 'n':
			change = input("What would you like to change it to?: ")
			#checks each value in the list of lists to see if it is the same. If it is, change that value to whatever the user inpit is
			for i in book:
				for j in i:
					if j == name:
						flag = True
						if flag == True:
							i[0] = change
		elif choice == 'a':
			change = input("What would you like to change it to?: ")
			#checks each value in the list of lists to see if it is the same. If it is, change that value to whatever the user input is
			for i in b00k:
				for j in i:
					if j == name:
						flag = True
						if flag == True:
							i[1] = change
		elif choice == 'p':
			change = input("What would you like to change it to?: ")
			#checks each value in the list of lists to see if it is the same. If it is, change that value to whatever the user input is
			for i in book:
				for j in i:
					if j == name:
						flag = True
						if flag == True:
							i[2] = change
		elif choice == 'e':
			change = input("What would you like to change it to?: ")
			#checks each value in the list of lists to see if it is the same. If it is, change that value to whatever the user input is
			for i in book:
				for j in i:
					if j == name:
						flag = True
						if flag:
							i[3] = change
		else:
			print("Invalid input")

def delete(book):
	flag = False
	if book == []:
		print("Your contacts are empty!")
	else:
		name = input("What is their name?: ")
		#checks to see if the list is the same
		for i in book:
			for j in i:
				if j == name:
					flag = True
					if flag:
						book.remove(i)
						print("Contact:",j,"has been deleted.")
	if flag == False:
		print("There is no contact with that name.")



def main():
	#opens file and changes all the lines into a list of list
	file = open("contacts.txt", "r")
	contacts = []
	for lines in file:
		#removes the \n
		line = lines.rstrip("\n")
		newLine = line.split(",")
		contacts.append(newLine)
	openFile = open("contacts.txt","w")
	#boolean flag

	flag = True
	while flag:	
		#returns menu choice as a variable
		choice = menu()
		if choice == 1:
			addNew(contacts)
		if choice == 2:
			display(contacts)
		if choice == 3:
			search(contacts)
		if choice ==4:
			modify(contacts)
		if choice == 5:
			delete(contacts)
		if choice == 6:
			flag = False
			print("Thank you for using me!")
	#appends the new contact sheet into the textfile
	for contact in contacts:
		stringContact = (", ".join(contact))
		if stringContact != "":				
			openFile.write(stringContact)	 #writes the new contacts to the address book	
			openFile.write("\n")				 #starts a new line													
	openFile.close()

main()