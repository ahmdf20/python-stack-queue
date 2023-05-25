def sequntial_seach_most_frequent(data):
  count_dict = {}
  for item in data:
    if item in count_dict:
      count_dict[item] += 1
    else:
      count_dict[item] = 1
    most_frequent = None
    max_count = 0
  for key in count_dict:
    if count_dict[key] > max_count:
      most_frequent = key
      max_count = count_dict[key]
  return most_frequent

mylist = [1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 9, 9, 10]
frequent_elemen = sequntial_seach_most_frequent(mylist)
print(f"Elemen yang paling sering muncul adalah {frequent_elemen}")