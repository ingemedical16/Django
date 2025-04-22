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
<QuerySet [<Book: Book object (1)>, <Book: Book object (2>>

### Updating models & migrating
python manage.py shell
7 objects imported automatically (use -v 2 for details).

Python 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from book_outlet.models import Book
>>> Book.objects.all()
<QuerySet [<Book: Harry Potter 1 - The Philosopher's Stone (5.0)>, <Book: Lord of the Rings (4.0)>]>
>>> 
python manage.py makemigrations
It is impossible to add a non-nullable field 'author' to book without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 2
codeany ➜ /workspaces/python/006_data_and_models/BOOK_STORE (main) $ python manage.py makemigrations
Migrations for 'book_outlet':
  book_outlet/migrations/0002_book_author_book_is_bestselling_alter_book_rating.py
    + Add field author to book
    + Add field is_bestselling to book
    ~ Alter field rating on book
codeany ➜ /workspaces/python/006_data_and_models/BOOK_STORE (main) $ 
codeany ➜ /workspaces/python/006_data_and_models/BOOK_STORE (main) $ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, book_outlet, contenttypes, sessions
Running migrations:
  Applying book_outlet.0002_book_author_book_is_bestselling_alter_book_rating... OK
codeany ➜ /workspaces/python/006_data_and_models/BOOK_STORE (main) $ python manage.py shell
Python 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from book_outlet.models import Book
>>> Book.objects.all()
<QuerySet [<Book: Harry Potter 1 - The Philosopher's Stone (5.0)>, <Book: Lord of the Rings (4.0)>]>
>>> Book.objects.all()[1]
<Book: Lord of the Rings (4.0)>
>>> Book.objects.all()[1].author
>>> Book.objects.all()[1].is_bestselling
False