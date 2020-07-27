from random import shuffle

num_list = [x for x in range(45)]
num = []
for j in range(6):
    shuffle(num_list)
    new_list = num_list.pop()
    num.append(new_list)
print(num)