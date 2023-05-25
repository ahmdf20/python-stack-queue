def is_similar(title1, title2):
  title1 = title1.lower()
  title2 = title2.lower()
  return True if title1[0] == title2[0] else False

def sequential_search(books, book_title):
  for book in books:
    if is_similar(book['title'], book_title):
      return book['shelf']
  return "Buku tidak ditemukan"

books = [
  {'title': 'Python Programming', 'shelf': 'A1'},
  {'title': 'Data Structures and Algorithms', 'shelf': 'B2'},
  {'title': 'Introduction to Machine Learning', 'shelf': 'C3'},
  {'title': 'Database Management Systems', 'shelf': 'D4'},
]

book_title = input("Masukkan judul buku yang ingin dicari : ")
shelf_location = sequential_search(books, book_title)
print(shelf_location)
