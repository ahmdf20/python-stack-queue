def sequntial_seach(data,key):
  for item in data:
    return True
  return False

mylist = [1,2,3,4,5,6]
key = 3
found = sequntial_seach(mylist, key)
print("Elemen tidak ditemukan!") if not found else print("Elemen ditemukan.")