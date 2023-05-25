def binary_search(data, target):
  low = 0
  high = len(data) - 1
  while low <= high:
    mid = (low + high) // 2
    if data[mid] == target:
      return mid
    elif data[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1

names = ['Alice', 'Bob', 'Bona Parte', 'David', 'Joseph', 'Frank', 'George']
target_name = input("masukkan nama yang ingin dicari :")
index = binary_search(names, target_name)

print(f"Nama ditemukan pada index {index}") if index != -1 else print("Nama tidak ditemukan!")