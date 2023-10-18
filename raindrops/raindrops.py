def convert(number):
    drops = ["Pling", "Plang", "Plong"]
    divisor = [3,5,7]
    raindrop = ""

    for i, num in enumerate(divisor):
        if number % num == 0:
            raindrop += drops[i]
    if not raindrop:
        return f'{number}'
    return raindrop
