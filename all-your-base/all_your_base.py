def to_other_base(dec_num, out_base):
    """Converts from decimal to other bases"""

    new_base_int = []

    while (results := divmod(dec_num, out_base)):
        new_base_int.append(results[1])
        if results[0] == 0:
            break
        dec_num = results[0]

    return new_base_int


def rebase(input_base, digits, output_base):

    if input_base <= 1:
        raise ValueError("input base must be >= 2")
    if output_base <= 1:
        raise ValueError("output base must be >= 2")
    for num in digits:
        if num < 0 or num >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    convert_int = 0

    for num in digits:
        convert_int = (convert_int * input_base) + num

    new_base = to_other_base(convert_int, output_base)

    return new_base[::-1]
