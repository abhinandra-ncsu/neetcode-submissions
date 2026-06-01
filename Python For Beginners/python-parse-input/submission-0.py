from typing import List

def read_integers() -> List[int]:
    user_input = input()
    string_list = []
    for i in user_input.split(","):
        string_list.append(int(i))
    return string_list
    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
