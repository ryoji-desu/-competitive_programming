def decide_even_or_odd():
    array_input= input().split()
    result_of_product = int(array_input[0]) * int(array_input[1])
    if result_of_product % 2 == 0:
        print("Even")
    else:
        print("Odd")
