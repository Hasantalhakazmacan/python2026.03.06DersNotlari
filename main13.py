def most_common_character(txt:str):
    index = 0
    most_common =""
    for char in txt:
        if index<txt.count(char):
            index = txt.count(char)
            most_common = char 
    return most_common ,index

first_string = "abcdbde"
print(most_common_character(first_string))

second_string = "exemplaryelementary"
print(most_common_character(second_string))

