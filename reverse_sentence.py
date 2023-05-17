def reverse(data):
  stack = []
  reversed_sentence = ""
  for word in data.split():
    stack.append(word)
  while len(stack) > 0:
    reversed_sentence += stack.pop() + " "
  return reversed_sentence.strip()
print(reverse("Ahmad Fadilah"))
