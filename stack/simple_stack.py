stack = [1,2,3,4,5]
print(f"stack = {stack}")

for i in range (len(stack)+1, 8):
  stack.append(i)
  print(f"stack input : {i}")
  print(f"stack = {stack}")

out = stack.pop()
print(f"stack out : {out}")
print(f"stack = {stack}")