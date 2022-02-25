my_list = [1, 2, 3]

res_list = [number ** 2 for number in my_list]
res_list2 = list(map(lambda number: number ** 2, my_list))
