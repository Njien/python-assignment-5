"""
ASSIGNMENT: Login and Registration Portal System

OBJECTIVE:
Create a simple command-line user management system that allows/prompts users to register new accounts, 
login to existing accounts, and optionally verify their accounts for a fee.

REQUIREMENTS:

1. SYSTEM SETUP:
   - Create a verification cost of 1500 (stored in a variable)
   - Initialize an empty variable "users_db" to store user data for all users
   - Display a welcome portal with clear instructions (provided in code below)

2. MAIN MENU:
   - Present users with a formatted welcome message showing available commands
   - Accept user input for either "login" or "register" (case-insensitive)
   - Handle invalid commands with appropriate error messages

3. REGISTRATION FUNCTIONALITY:
   - Prompt user for username, password, and initial balance
   - Check if username already exists in "users_db" (prevent duplicates)
   
   - Store new user with the following data structure:
     * username (string)
     * password (string)
     * balance (float)
     * is_verified (boolean, default: False)
   - Display success message and user information after creation

4. VERIFICATION SYSTEM (Post-Registration):
   - After successful registration, offer optional account verification
   - Show verification cost and prompt user for yes/no decision
   - If user chooses "yes":
     * Check if user has sufficient balance
     * If sufficient: deduct verification cost and set is_verified to True
     * If insufficient: display error message with current balance and required amount
   - Regardless of verification choice (whether the user wishes to verify or not), display "Login successful!" and user info

5. LOGIN FUNCTIONALITY:
   - Prompt user for username and password
   - Validate that username exists in the system
   - Verify password matches stored password
   - Display appropriate success or error messages:
     * Success: "login successful!" + user information
     * Username not found: f"user {username} does not exists"
     * Wrong password: f"password mismatch for {username}"

6. DATA STRUCTURE:
   Each user should have the following details:

    -> "username"
    -> "password"
    -> "balance"
    -> "is_verified"
   

7. OUTPUT FORMATTING:
   - Include clear command instructions
   - Display user information after successful operations

TECHNICAL REQUIREMENTS:
- Use appropriate data types (string, float, boolean, dict, list)
- Implement proper input validation
- Use preferred data type you think can handle storage of user details and users_db
- Handle case-insensitive input where appropriate
- Use conditional statements for flow control
- Implement proper error handling for edge cases

EXPECTED BEHAVIOR EXAMPLES:

Registration Flow:
1. User selects "register"
2. Creates username, password, enters balance
3. System confirms creation and shows user data
4. System offers verification option
5. User can accept/decline verification
6. System processes verification (if chosen) and shows final status

Login Flow:
1. User selects "login" 
2. Enters existing username and password
3. System validates credentials
4. Shows success message with user data OR appropriate error message

ERROR CASES TO HANDLE:
- Duplicate username registration
- Login with non-existent username
- Login with incorrect password  
- Insufficient balance for verification
- Invalid menu commands

STARTER CODE STRUCTURE:
- Initialize verification_amount variable
- Create empty users_db (use your preferred data type choice based on your thought)
- Build registration and login conditions
- Add verification system logic

This assignment tests your understanding of:
- Data types and data structures
- User input handling and validation
- Conditional logic and flow control
- String manipulation and formatting
- Basic error handling
- Program organization and user experience design
"""

# TODO: Implement the login and registration portal system based on the requirements above

verification_amount = 1500
#users_db = None            # Initialize user database with appropraite data-type
print('''

         Login and Register Portal        
      ________________________________    
    \t\tcommands:                            
      enter "login" to login              
      enter "register" to register        

''')

# Your implementation here..

#command = str(input("Enter command to login or register: ").lower())
Id = 1

user_db ={Id: {
	"username": "jessy",
	"password": "pass",
	"balance": 1500,
	"is_verified": False},
	Id+1: {
	"username": "tk",
	"password": "tanko",
	"balance": 1000,
	"is_verified": False}
	}

unavailable_pass = list(user_db[Id+1].values())
unavailable_username = list(user_db[Id].values())
general = unavailable_pass + unavailable_username

# Create or register account

command = str(input("Enter command to login or register:\n>>> ").lower())
if command == "register": 
	username = str(input("Create username:\n>>> ").lower())
	password = str(input("Create password:\n>>> ").lower())
	balance = float(input("Enter amount or balance:\n>>> "))
	is_verified = False

	if username in general:
		print(f"can not have duplicate username\n{username} already exist")
	else:
		if password in general:
			print("can not have duplicate password\nPlease change password")
		else:
			Id += 1
			user_db = {Id+1: {
			"username": username,
			"password": password,
			"balance": balance,
			"is_verified": False}
			}
			print("Account has been created successfully")
			print(f"Account details are: {user_db[3]}")

	# Get verified

			print("Would you like to get verified?yes/no\nVerification will cost you 1,500")
			yes_no = str(input("Do want to get verified?:\n>>> ").lower())
			if yes_no == "yes":
				if user_db[3]["balance"] >= verification_amount:
					print("verification for", user_db[3]["username"], "updated successful!")
					user_db[3]["balance"] = user_db[3]["balance"] - verification_amount
					user_db[3]["is_verified"] = True
					print(user_db[3])
					user_db.update(user_db[3])
				elif user_db[3]["balance"] < verification_amount:
					print("OOPS! Insufficient balance/amount")
					print("Verification will cost you 1,500")
					print(user_db[3])

			elif yes_no == "no":
				print("Registration successful!")
				print(user_db[3])
			else:
				print("Invalid command")
	
	# Login Logic

elif command == "login":
	username = str(input("Enter your username:\n>>> ").lower())
	if username in general:
		password = str(input("Enter your password: ").lower())
		if password in general:
			
			print("Login Successful!")
		else:
			print(f"Password mismatch! for {username}")
	else:
		print(f"Account for {username} Does not Exist\nPlease create account")
else:
	print("Invalid Command!")
