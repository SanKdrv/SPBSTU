import math

free_space = 1.44 * 1024 * 1024
num_pages = 100
num_rows_on_page = 50
chars_on_row = 25
char_weight = 4
book_space = num_pages * num_rows_on_page * chars_on_row * char_weight
num_of_books = math.floor(free_space / book_space)
print("Количество книг, помещающихся на дискету:", num_of_books)
