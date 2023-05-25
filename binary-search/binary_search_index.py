def binary_search_index(data, key):
  low = 0
  high = len(data) - 1
  while low <= high:
    mid = (low + high) // 2
    if data[mid] == key:
      return mid
    elif data[mid] < key:
      low = mid + 1
    else:
      high = mid - 1
  return -1

mylist = [1, 2, 3, 4, 5, 6, 7, 8]
key = 5
index = binary_search_index(mylist, key)
print(f"Index element {key} is {index}") if index != -1 else print(f"Elemen tidak ditemukan")