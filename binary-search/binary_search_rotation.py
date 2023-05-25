def binary_search_rotation(data):
  low = 0
  high = len(data) -1 
  while low < high:
    mid = (low + high) // 2
    if data[mid] > data[high]:
      low = mid + 1
    else:
      high = mid
  return low

mylist = [1,2,3,4,5,6,7,8]
rotation_index = binary_search_rotation(mylist)
print(f"Index lowest rotation is {rotation_index}")