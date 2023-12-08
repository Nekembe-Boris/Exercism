def cal_ord(or_word, copy):

    for char in copy.lower():
        if char not in or_word.lower():
            return False

    original_char_sum = [ord(char) for char in or_word.lower()]
    copy_char_sum = [ord(char) for char in copy.lower()]

    return sum(original_char_sum) == sum(copy_char_sum)


def find_anagrams(word, candidates):
    anagrams = []

    for can_words in candidates:
        if can_words.lower() != word.lower():
            if cal_ord(word, can_words):
                anagrams.append(can_words)

    return anagrams
