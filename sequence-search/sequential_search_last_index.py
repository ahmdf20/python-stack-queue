def sequential_search_last_index(data, key):
  last_index = -1
  for i in range(len(data)):
    if data[i] == key:
      last_index = i
  return last_index

mylist = [1,2,3,4,5,6,7]
key = 3
last_index = sequential_search_last_index(mylist, key)
print(f"Elemen {key} tidak ditemukan") if last_index == -1 else print(f"Index terakhir elemen {key} adalah {last_index}")
