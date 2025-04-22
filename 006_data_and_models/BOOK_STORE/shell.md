## Shell
### Adding data to the database
Python 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from book_outlet.models import Book
>>> harry_potter = Book(title="Harry Potter 1 - The Philosopher's Stone",rating=5)
>>> harry_potter.save()
>>> lord_of_the_rings = Book(title="Lord of the Rings",rating=4)
>>> lord_of_the_rings.save()
### Querying data from the database
>>> Book.objects.all()
<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]>