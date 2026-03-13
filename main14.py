def longest_series_of_neighbours(my_list):
    current = 1
    longest = 1
    for i in range(len(my_list)-1):
        if abs(my_list[i]-my_list[i+1])==1 :
            current +=1
        else:
            current = 1
        if current>longest:
            longest = current

    return longest

my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))
