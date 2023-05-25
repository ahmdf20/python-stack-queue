class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

class BookStack:
  def __init__(self):
    self.stack = []
  
  def add(self, book):
    self.stack.append(book)
    print(f"Success insert book {book.title}")

  def is_empty(self):
    return len(self.stack) == 0

  def delete(self):
    if (self.is_empty()):
      return None
    return self.stack.pop()
  
  def get(self):
    if (self.is_empty()):
      return None
    return self.stack[-1]

if __name__ == "__main__":
  menus = ["Add", "Read", "Delete", "Close"]
  book_stack = BookStack()
  while True:
    i = 1
    for menu in menus:
      print(f"{i}. {menu}")
      i+=1
    input_menu = int(input("Select menu (1/2/3/4) :"))
    if input_menu == 1:
      title = input("Input title book : ")
      author = input("Input author of the book : ")
      book = Book(title, author)
      book_stack.add(book)
    elif input_menu == 2:
      data = book_stack.get()
      if (book_stack.is_empty()):
        print("Cannot find data from null stack!")
      else:
        print(f"First data stack : {data.title}")
    elif input_menu == 3:
      data = book_stack.delete()
      if (book_stack.is_empty()):
        print("Cannot delete data from null stack!")
      else:
        print(f"Delete data : {data.title}")
    elif input_menu == 4:
      print("Thx for using this program!")
      break
    else:
      print("Invalid menu selection!")