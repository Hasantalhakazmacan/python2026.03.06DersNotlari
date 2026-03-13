def distinct_numbers(my_list):
    distinct =[]
    for item in my_list:
        if item not in distinct:
            distinct.append(item)
    return sorted(distinct)

my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list))

