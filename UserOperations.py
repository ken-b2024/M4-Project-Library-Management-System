import re
user_dict = {}


class User:
    def __init__(self,lib_id,birthdate):
        self.__id = lib_id
        self.__birth_date = birthdate

    
    def UserOpsMenu():
        user_menu = [
            '1. Add a new user',
            '2. View user details',
            '3. Display all users',
            '4. Return to Main Menu'
    ]
        print("\nUser Operations\n")
        print("Menu:", *user_menu, sep='\n')

    @staticmethod
    def new_user(lib_id,birth_date):
        first_name = input("Enter the first name of user: ").capitalize()
        last_name = input("Enter the last name of user: ").capitalize()
        for pattern in lib_id:
            lib_id = input("Enter the user's library ID number (format: xxxxx): ")
            pattern = (r"\d{5}")
            if re.match(pattern,lib_id):
                print("Library ID was successfully added")
                break
            else:
                print("\nID format is invalid. Try again...")
        for pattern in birth_date:
            birth_date = input("Enter the bithdate of user (format: xx/xx/xxxx): ")
            pattern = (r"\d{2}/\d{2}/\d{4}")
            if re.search(pattern, birth_date):
                print("Birthdate was successfully added.")
                break
            else:
                print("\nBirthdate format is invalid. Try again...")
        user_dict[lib_id] = {
            'Firstname': first_name, 
            'Lastname': last_name,
            'ID': lib_id,
            'Birthdate': birth_date
        }
        
        print("\nUser Details:", user_dict, sep='\n')
        print(f"\nThe account for {first_name} has been created successfully")

    @staticmethod
    def view_user():
        lib_id = input("Enter the user's Library ID number: ")
        if lib_id in user_dict.keys():
            print("\nFetching user details...")
            print("User Details:", user_dict[lib_id])
        else:
            print("\nID number is invalid. Try again...")

    def display_users(self):
        if user_dict:
            print("\nFetching users...")
            print("\nUsers:", user_dict, sep='\n')
        else:
            print("\nThere are no contacts to display. Returning to main menu...")

while True:
    User.UserOpsMenu()
    try:
        user_menu_action = int(input("\nSelect an option: "))
        if user_menu_action == 1:
            User.new_user('lib_id','birthdate')
        if user_menu_action == 2:
            User.view_user()
        if user_menu_action == 3:
            User.display_users('self')
        if user_menu_action == 4:
            print("\nReturning to main menu...")
            break
    except ValueError:
        print("\nInput is invalid. Please try again...")