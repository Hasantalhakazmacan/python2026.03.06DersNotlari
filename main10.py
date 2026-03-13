def polindromes(txt):
    if txt [:]== txt[::-1]:
        return True
    else:
        return False


while True :
    word = input("Please type in a palindrome:")
    if polindromes(word):
        print(f"{word} is a polindrome")
        break
    else:
        print(f"{word} is not a polindrome")