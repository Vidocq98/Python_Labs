from Library import Library
from Book import Book
from Taggable import Taggable
lib = Library(1, '51 Some str., NY')
lib += Book('Leo Tolstoi', 'War and Peace')
lib += Book('Charles Dickens', 'David Copperfield')
for book in lib:
    print(book)
    print(book.tag())
