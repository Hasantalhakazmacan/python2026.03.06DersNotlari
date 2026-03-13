numbers = [2]  # Liste döngüden önce oluşturuldu

while True:
    
    number = int(input("New item: ")) 
    
    if number != 0:
        numbers.append(number)
        print(f"The list now: {numbers}")
        print(f"The list is in order: {sorted(numbers)}")
    else:
        print("bye")
        break