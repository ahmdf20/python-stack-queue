def binary_next_larger(data, target):
  low = 0
  high = len(data) - 1
  next_larger = None
  while low <= high:
    mid = (low + high) // 2
    if data[mid] > target:
      next_larger = data[mid]
      high = mid - 1
    else:
      low = mid + 1
  return next_larger

mylist = [1,2,3,4,5,6,7,8]
target = 6
res = binary_next_larger(mylist, target)
print(f"Elemen terkecil yang lebih besar dari {target} adalah {res}") if not res else print("Tidak ada element yang lebih besar dari target")