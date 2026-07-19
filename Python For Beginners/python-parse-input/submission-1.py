from typing import List

def read_integers() -> List[int]:
    u_input = input()
    r = u_input.split(",")
    res = []
    for e in r:
        res.append(int(e))
    return res

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
