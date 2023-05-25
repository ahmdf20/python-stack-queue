def sequential_seach_two_sum(data, target):
  for i in range(len(data)):
    for j in range(i+1, len(data)):
      if data[i] + data[j] == target:
        return data[i], data[j]
  return None

mylist = [1, 2, 3, 4, 5, 6, 7]
target_sum = 12
result = sequential_seach_two_sum(mylist, target_sum)
print(f"Tidak ada dua elemen yang jumlahnya sama dengan target.") if not result else print(f"Dua elemen yang jumlahnya sama dengan {target_sum} adalah {result[0]} dan {result[1]}")