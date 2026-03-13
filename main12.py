def everything_reversed(my_list):
    reversed =[]
    for item in my_list:
        reversed.append(item[::-1])
    return reversed [::-1]

my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)