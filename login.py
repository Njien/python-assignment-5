verification_fee = 1500
print("""
		available coomands
		"Login" to login account
		"register" to create new account""")
users_db = [{"username": "jessy", "password": "pass", "balance": 2000, "is_verified": False}, {"username": "tk", "password": "tanko", "balance": 1500, "is_verified": False}]

command = str(input("Enter login or register to continue:\n>>> ").lower())

if command == "register":
	username = str(input("create username\n>>> ").lower())
	if username in users_db[0].values() or username in users_db[1].values():
		print(f"username '{username}' already exist\nEnter another username")
	else:
		password = str(input("Create password:\n>>> ").lower())
		if password in users_db[0].values() or password in users_db[1].values():
			print(f"password '{password}' already exist\ncan not duplicate password")
		else:
			balance = float(input("Enter balance:\n>>> "))
			is_verified = False

			yes_no = str(input("Do you want get verified? yes/no;\n>>> ").lower())
			if yes_no == "yes":
				if balance >= verification_fee:
					print("Verification update successful")
					balance = balance - verification_fee
					is_verified = True
					users_db.append({"username": username, "password": password, "balance": balance, "is_verified": is_verified})
					print(f" Registered Successful: {users_db[2]}")
				else:
					print(f"inssufficient fund: verification fee is: {verification_fee}, but your balance is {balance}")
					
					users_db.append({"username": username, "password": password, "balance": balance, "is_verified": is_verified})
					print(f" Registered Successful: {users_db[2]}")
			elif yes_no == "no":
				users_db.append({"username": username, "password": password, "balance": balance, "is_verified": is_verified})
				print(f" Registered Successful: {users_db[2]}")
			else:
				print(f"{yes_no} is an in valid command")
elif command == "login":
	username = str(input("Enter username\n>>> ").lower())
	if username in users_db[0].values() or username in users_db[1].values():
		password = str(input("Enter password:\n>>> ").lower())
		if password in users_db[0].values() or password in users_db[1].values():
			print(f"Login successful! Welcome back '{username}'")
			print(f" users details: {users_db[0]}")
		else:
			print(f"password{password} mismatch for {username}")

	else:
		print(f"'{username}' account does not exist\nRegister new account")

else:
	print(f"invalid command!: '{command}' command does not exist")
					
