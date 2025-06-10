array = [1, 2, 3, 5, 7, 8, -1, 0, 4, 5, 6, -1, 2, 4, 5, -2, 5, 6, 6, 7, 7, 7, -3, 2, 2, 2, 2, 2]

first_neg_found = False
cache = []
last_neg_index = -1
index = -1

for num in array:
    index += 1
    if num < 0:
        if not first_neg_found:
            first_neg_found = True
            first_neg_index = index
        else:
            last_neg_index = index  # обновляется каждый раз
    if first_neg_found:
        cache.append((index, num))

# После прохода считаем сумму между первым и последним отрицательными (не включая их)
sum_between = sum(num for i, num in cache if first_neg_index < i < last_neg_index)

print("Сумма между первым и последним отрицательными числами:", sum_between)
