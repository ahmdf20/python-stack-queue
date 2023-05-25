def sequntial_seach_max(data):
  max_index = 0
  for i in range(1, len(data)):
    if data[i] > data[max_index]:
      max_index = i
  return max_index

mylist = [3,7,5,4,3,2]
max_index = sequntial_seach_max(mylist)
print(f"Index elemen maximum adalah {max_index}")