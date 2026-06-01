def add_two_numbers() -> int:
    user_input = input()
    sum = []
    for i in user_input.split(","):
        sum.append(int(i))
    final_sum = 0
    for i in sum:
        final_sum += i
    return final_sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
