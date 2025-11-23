class Book:
    def _init_(self, isbn: str, title: str, author: str,
                 published_year: int, category: str, available_copies: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.published_year = published_year
        self.category = category
        self.available_copies = available_copies

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "published_year": self.published_year,
            "category": self.category,
            "available_copies": self.available_copies}
    import json
import os
from book import Book

class LibraryInventory:
    def _init_(self, json_file="books.json"):
        self.json_file = json_file
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, "r") as f:
                data = json.load(f)
                return [Book(**book) for book in data]
        return []

    def save_books(self):
        with open(self.json_file, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)

    def add_book(self, book: Book):
        self.books.append(book)
        self.save_books()

    def remove_book(self, isbn: str):
        self.books = [b for b in self.books if b.isbn != isbn]
        self.save_books()

    def list_books(self):
        return self.books

    def search_book(self, isbn: str):
        for book in self.books:
            from inventory import LibraryInventory
from book import Book

def menu():
    lib = LibraryInventory()

    while True:
        print("\n===== LIBRARY INVENTORY MANAGER =====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List All Books")
        print("4. Search Book")
        print("5. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            year = int(input("Enter Published Year: "))
            category = input("Enter Category: ")
            copies = int(input("Enter Available Copies: "))

            book = Book(isbn, title, author, year, category, copies)
            lib.add_book(book)
            print("Book Added Successfully!")

        elif ch == "2":
            isbn = input("Enter ISBN to Remove: ")
            lib.remove_book(isbn)
            print("Book Removed Successfully!")

        elif ch == "3":
            books = lib.list_books()
            print("\n--- BOOK LIST ---")
            for b in books:
                print(f"{b.isbn} | {b.title} | {b.author} | {b.category} | Copies: {b.available_copies}")

        elif ch == "4":
            isbn = input("Enter ISBN to Search: ")
            book = lib.search_book(isbn)
            if book:
                print("\nBook Found:")
                print(book.to_dict())
            else:
                print("Book not found.")

        elif ch == "5":
            print("Exiting...")
            break

        else:
            print("Invalid Choice!")
        
    
    

