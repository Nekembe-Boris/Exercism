def is_pangram(sentence:str):
    if (sen_letters := len([letter for letter in set(sentence.lower()) if letter.isalpha()])) == 26:
        return True
    return False
