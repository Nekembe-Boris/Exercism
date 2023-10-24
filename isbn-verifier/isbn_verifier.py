def is_valid(isbn:str):
    total = 0
    n_len = 10


    for char in isbn:
        if char == "-":
            continue
        if char == "X" and n_len == 1:
            total += 10
            n_len -= 1
            continue
        if char.isnumeric():
            total += int(char) * n_len
            n_len -= 1
            continue
        return False

    return n_len == 0 and total % 11 == 0
