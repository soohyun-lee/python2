a = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]
new_list = []
for num in a:
    if num not in new_list:
        new_list.append(num)
print(new_list)
 # [1,2,3,4,5] 중복없이