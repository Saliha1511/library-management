print("---------Welcome To Library Mangement System-----------")
lst = [[101, "Ramayan", "Valmiki"], [102, "Mahabarat", "Ved Vyas"], [103, "Durga Saptshi",
                                                                     "Mahirshi Markenday"], [104, "Premchand Ke Phate Jute", "Munshi Premchand"]]
nameLst = []


class books:

    def addBooks(self):
        print("Adding a Book To library")
        bookId = int(input("Enter The id of Book:"))

        for book in lst:

            if (book[0] == bookId):
                print("Book Already Exist")
                break

            else:
                bookName = input("Enter The Name of Book:")
                bookAuthor = input("Enter The Book Author")
                bookLst = [bookId, bookName, bookAuthor]
                lst.append(bookLst)
                print("successfully added book")
                break

    def viewBooks(self):
        print("You are viewing the books listed Below are:")
        for book in lst:
            print(
                f"The given book Id is {book[0]} and Book Name is {book[1]} and book author is {book[2]}")

    def issueBook(self):
     print("You are issuing a book from this library")
     name = input("Enter your Name Please: ")
     for namelist in nameLst:
        if namelist[0] == name:
            print("You Have Already Issued a book")
            issueId = int(input("Please Enter The ID of the book: "))
            for book in lst:
                if int(book[0]) == issueId:
                    print(f"Issued: Book ID: {book[0]}, Book Name: {book[1]}, Book Author: {book[2]}\nSuccessfully issued to {name}")
                    nameIssueLst = [book]
                    nameLst.append(nameIssueLst)
                    lst.remove(book)
                    return
            print("Specified Book Is not in The Library")
            return

     print("Unique Name")
     issueId = int(input("Please Enter The ID of the book: "))
     for book in lst:
        if int(book[0]) == issueId:
            print(f"Issued: Book ID: {book[0]}, Book Name: {book[1]}, Book Author: {book[2]}\nSuccessfully issued to {name}")
            nameIssueLst = [name, book]
            nameLst.append(nameIssueLst)
            lst.remove(book)
            return
     print("Specified Book Is not in the Library")

    def returnBook(self):
        print("You are returning book to library")
        returnName = input("Enter your Name Please: ")

        for nameBook in nameLst:

            namebooklist = nameBook[1]

            if (returnName == nameBook[0]):
                print("Name is Present in list")
                print(f"Current Issuing Books are:{namebooklist}")
                inputo = int(input("Please Enter The Id of Book: "))
                print(namebooklist[0])
                if (inputo == namebooklist[0]):
                    print(
                        f"You are returning Book Id:{namebooklist[0]} book Name:{namebooklist[1]} To Librarian")
                    lst.append(namebooklist)
                    nameLst.remove(nameBook)

                else:
                    print("Sepcific Book is not Issued to you")

            else:
                print("Please Enter a Valid Name ")

    def admin(self):
        print("Enter The id and Password please(Only for Admin)")
        username=input("Enter Your Username Please:")
        password=input("Enter Your password Please:")
        if (username == "admin" and password == "admin"):
            print("UserName and Password Matched")
            print(lst)
            print(nameLst)
                
        else:
            print("Username and password not matched")
            return


# actual working
a = books()

while True:
    print("Enter 0 to exit the Library")
    print("Enter 1 to add Books To Library")
    print("Enter 2 to Views Books From Library")
    print("Enter 3 to issue book from library {Only One}")
    print("Enter 4 to return book to library")
    print("Enter 5 to views issue and returns to library (Only for Admin)")
    case = int(input("Input Please:"))
    match case:
        case 0:
            exit()
        case 1:
            a.addBooks()
        case 2:
            a.viewBooks()
        case 3:
            a.issueBook()
        case 4:
            a.returnBook()
        case 5:
            a.admin()
        case _:
            exit()
