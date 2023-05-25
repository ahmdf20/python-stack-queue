def binary_search(data, key):
  low = 0
  high = len(data) - 1

  while low <= high:
    mid = (low + high) // 2
    if data[mid] == key:
      return True
    elif data[mid] < key:
      low = mid+1
    else: 
      high = mid - 1
  return False

mylist = [1,2,3,4,5,6,7,8]
key = 6
found = binary_search(mylist, key)
print("Elemen ditemukan") if found else print("Elemen tidak ditemukan")