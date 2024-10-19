import re
author_dict = {}

class Author:
    def __init__(self,name,biography):
        self.__name = name
        self._biography = biography

    def set_name(self,author_name):
        self.__name = author_name
    def get_name(self):
        return self.__name

    def AuthorOpsMenu():
        author_menu = [
            '1. Add a new author',
            '2. View author details',
            '3. Display all authors',
            '4. Return to Main Menu'
        ]
        print("\nAuthor Operations\n")
        print("Menu", *author_menu, sep='\n')

    def add_author(self,ISNI):
        author_name = input("Enter the name of the author: ")
        for pattern in ISNI:
            ISNI = input("Enter the last four digits of the author's ISNI: ")
            pattern = (r"\d{4}")
            if re.search(pattern, ISNI):
                print("\n ISNI successfully added.")
                break
            else:
                print("\nISNI format is invalid. Try again...")
        author_bio = input("Enter the Author's biography: ")

        author_dict[ISNI] = {
            'Name': author_name,
            'Biography': author_bio
        }
        print("Author:", author_dict, sep='\n')
        print("\nAuthor has been succesfully added")


    def view_author(ISNI):
        for i in ISNI:
            ISNI = input("Enter the last four of the author's ISNI: ")
            if ISNI in author_dict:
                print("\nFetching author details...\n")
                print("\nAuthor Info:", author_dict, sep='\n')
                break
            else:
                print("\nInvalid ISNI. Try again...")

    def display_authors():
        print("\nFetching author database...\n")
        print("Authors:", author_dict, sep='\n')

while True:
    Author.AuthorOpsMenu()
    try:
        author_menu_action = int(input("\nSelect an option: "))
        if author_menu_action == 1:
            Author.add_author('self','ISNI')
        if author_menu_action == 2:
            Author.view_author('ISNI')
        if author_menu_action == 3:
            Author.display_authors()
        if author_menu_action == 4:
            print("\nReturning to Main Menu...")
            break
    except ValueError:
        print("\nInvalid input. Please try again...")