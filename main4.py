def first_word(txt):
    return txt.split(" ")[0]

def second_word(txt):
    return txt.split(" ")[1]

def last_word(txt):
    return txt.split(" ")[len(txt.split(" "))-1]

sentence = "it was a dark and stormy python"

print(first_word(sentence)) 
print(second_word(sentence)) 
print(last_word(sentence))
