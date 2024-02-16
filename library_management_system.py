class Library:
    # constructor to open the books.txt file
    def __init__(self):
        self.file = open("books.txt", "a+")

    # destructor to close the books.txt file
    def __del__(self):
        self.file.close()
     # function to list all books in the file   
    def list_books(self):
        with open("books.txt", "r") as file:
            books_list = file.readlines()
            # iterate each line on the list
            for book in books_list:
                book_info = book.strip().split(",")
                print(f"Book name: {book_info[0]} | Author: {book_info[1]}")
    #function to add book
    def add_book(self):
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        first_release_year = input("Enter first release year: ")
        num_of_pages = input("Enter number of pages: ")
        book_info = f"{book_title},{book_author},{first_release_year},{num_of_pages}\n"
        with open("books.txt", "a") as file:
            file.write(book_info)
    #function to remove book
    def remove_book(self):
        book_title_to_delete = input("Enter book title to delete: ")
        with open("books.txt", "r") as file:
            books_list = file.readlines()
        with open("books.txt", "w") as file:
            for book in books_list:
                book_info = book.strip().split(",")
                if book_info[0] != book_title_to_delete:
                    file.write(book)

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
