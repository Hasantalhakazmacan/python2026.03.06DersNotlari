words =[]
while True:
    word = input("Enter a word :")
    if word not in words:
        words.append(word)
    else:
        print("You already entered this word")
        break
print(f"Yout typed in {len(words)} different words")
