def is_isogram(string:str):
    return len(set(string.lower().replace(" ", "").replace("-", ""))) == len(string.replace(" ", "").replace("-", ""))
