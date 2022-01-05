input_range = input()
input_array = input().split()
new_array = []
check_boolean = True
counter = 0
for num in input_array:
    new_array.append(int(num))
while check_boolean:
    temp_array = []
    for num in new_array:
        check_diviable = num % 2
        tmp = num / 2
        temp_array.append(tmp)
        if check_diviable != 0:
            check_boolean = False
            break
    new_array = temp_array
    counter += 1
counter -= 1
print(counter)