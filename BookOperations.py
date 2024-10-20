import re
library_dict = {}

class Book:
    def __init__(self, title, author, genre, ISBN):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.unique_id = ISBN
        self._availabilty = True

    def get_title(self):
        return self.__title
    def set_title(self,new_title):
        self.__title = new_title
    def get_author(self):
        return self.__author
    def set_author(self,new_author):
        self.__author = new_author
    def get_genre(self):
        return self.__genre
    def set_genre(self,new_genre):
        self.__genre = new_genre

    @staticmethod
    def BookOpsMenu():
        book_menu = ['1. Add a new book',
                '2. Borrow a book',
                '3. Return a book',
                '4. Search for a book',
                '5. Reserve a book',
                '6. Display all books',
                '7. Return to Main Menu'
    ]
        print("\nBook Operations\n")
        print("Menu:",*book_menu, sep='\n')
      
    def add_book(title,author,genre,ISBN):
        for pattern in ISBN:
            ISBN = input("Please enter the first four numbers of the ISBN of the book (format:xxx-x): ")
            pattern = (r"\d{3}-\d{1}")
            if re.search(pattern, ISBN):
                # library_dict = int(ISBN)
                print("ISBN succesfully added.")
                break
            else:
                print("\nISBN format is invalid. Try again...")
        title = input("Enter the title: ")
        Book.set_title
        author = input("Enter the author: ")
        Book.set_author
        genre = input("Enter the genre: ")
        Book.set_genre

        library_dict[ISBN] = {
                        'Title': title,
                        'Author': author,
                        'Genre': genre,
                        'Status': 'Available'
                    }
        print(f"\n{title} has been successfully added to the library!")
        print("\nBook Info:", library_dict[ISBN], sep="\n")

    @staticmethod
    def borrow_book(ISBN):
        ISBN = input("Please enter the first four numbers of the ISBN: ")
        if ISBN in library_dict:
            print("\nBook Info:", library_dict[ISBN], sep="\n")
            borrow_action = input("\nDo you want to borrow this book (y/n): ")
            if borrow_action == 'y':
                library_dict[ISBN]['Status'] = 'Unavailable'
                print(f"\n{library_dict[ISBN]['Title']} has been marked as {library_dict[ISBN]['Status']} ")
            else:
                print("\nReturning to menu...")
        else:
            print("\nISBN does not exist. Try again...")

    @staticmethod
    def return_book(ISBN):
        ISBN = input("Please enter the first four numbers of the ISBN: ")
        if library_dict[ISBN]['Status'] == 'Available':
            print("\nThis book is already in stock.")
        elif ISBN in library_dict:
            library_dict[ISBN]['Status'] = 'Available'
            print(f"\n{library_dict[ISBN]['Title']} has been marked as {library_dict[ISBN]['Status']}")
        else:
            print("\nISBN is invalid. Try again...")

    @staticmethod
    def search_for_book(ISBN):
        ISBN = input("Please enter the first four numbers of the ISBN: ")
        if ISBN in library_dict:
            print(f"\n{library_dict[ISBN]['Title']} is {library_dict[ISBN]['Status']}")
        else:
            print("\nISBN does not exist. Try again...")

    @staticmethod
    def reserve_book(ISBN, lib_id):
        ISBN = input("Please enter the first four numbers of the ISBN: ")
        # print(library_dict)
        if ISBN in library_dict.keys():
            # print("Hello")
            if library_dict[ISBN]['Status'] == 'Unavailable':
                print("\nThis book is not available at this time.")
                user_action = input("\nWould you like to reserve it once it is returned? (y/n): ")
                if user_action == 'y':
                    for pattern in lib_id:
                        lib_id = input("Please enter your library ID: ")
                        pattern = (r"\d{5}")
                        if re.search(pattern,lib_id):
                            library_dict[ISBN]['Status'] =  f'Reserved for Library ID: {lib_id}'
                            print(f"\n{library_dict[ISBN]['Title']} has been reserved for user with Library ID:{lib_id}")
                            break
                        else:
                            print("\nID format is incorrect. Try again...")
                else:
                    print("\nReturning to menu...")
            elif library_dict[ISBN]['Status'] == 'Available':
                print("\nThis book is available!")
                user_action = input("\nWould you like to reserve it? (y/n): ")
                if user_action == 'y':
                    for pattern in lib_id:
                        lib_id = input("Please enter your library ID: ")
                        pattern = (r"\d{5}")
                        if re.search(pattern,lib_id):
                            library_dict[ISBN]['Status'] = 'Reserved - [lib_id]'
                            print(f"\n{library_dict[ISBN]['Title']} has been reserved for Library ID:{lib_id}")
                            break
                        else:
                            print("\nID format is invalid. Try again...")
                else:
                    print("\nReturning to menu...")
        else:
            print("\nISBN is not present. Try again...")

    @staticmethod
    def display_book():
        if library_dict:
            print("\ndFetching book details...\n")
            print("\nLibrary Info:", library_dict, sep="\n")
        else:
            print("\nThere are no books to display.")
            print("\nReturning to menu...")

while True:
    Book.BookOpsMenu()
    try:
        book_menu_action = int(input("\nSelect an option: "))
        if book_menu_action == 1:
            Book.add_book('title','author','genre','ISBN')
        elif book_menu_action == 2:
            Book.borrow_book('ISBN')
        elif book_menu_action == 3:
            Book.return_book('ISBN')
        elif book_menu_action == 4:
            Book.search_for_book('ISBN')
        elif book_menu_action == 5:
            Book.reserve_book('ISBN','lib_id')
        elif book_menu_action == 6:
            Book.display_book()
        elif book_menu_action == 7:
            print("\nReturning to main menu...")
            break
    except ValueError:
        print("\nInput is invalid. Please try again...")