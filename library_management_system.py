class Library:
    # constructor to open the books.txt file
    def __init__(self):
        self.file = open("books.txt", "a+")

    # destructor to close the books.txt file
    def __del__(self):
        self.file.close()

    # display menu and return user choice
    def menu(self):
        print("*** MENU ***\n1. List Books\n2. Add Books\n3. Remove Books")
        while True:
            try:
                choice = int(input("\nEnter your choice: "))
                if choice < 1 or choice > 3:
                    print("Choice should be between 1-3.")
                else:
                    return choice
            except ValueError:
                print("Choice should be a number.")


# main function
def main():
    lib = Library()
    choice = lib.menu()

    if choice == 1:
        lib.list_books()
    elif choice == 2:
        lib.add_book()
    else:
        lib.remove_book()


main()
