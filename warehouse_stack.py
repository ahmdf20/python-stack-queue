stack = []
menus = ["Add Stack", "Delete Last Stack", "Get First Stack", "Close"]
def add(stack, data):
  stack.append(data)
  print(f"{data} success added to stack.")

def delete(stack):
  print("Cannot delete data from null stack") if len(stack) == 0 else print(f"Delete first stack : {stack[-1]}")
  stack.pop()

def get(stack):
  print("Cannot get data from null stack") if len(stack) == 0 else print(f"First Stack : {stack[-1]}")
while True:
  print(f"\n Warehouse : {stack}")
  print("Menu")
  i = 1
  for menu in menus:
    print(f"{i}. {menu}")
    i+=1
  input_menu = int(input("Select menu (1/2/3/4) : "))
  if input_menu == 1:
    data = input("Input new Data : ")
    add(stack, data)
  elif input_menu == 2:
    delete(stack)
  elif input_menu == 3:
    get(stack)
  elif input_menu == 4:
    print("Thx for using this program!")
    break
  else:
    print("Invalid menu! Pls input available menu")
