def get_longer_word(word1: str, word2: str) -> str:
    a = len(word1)
    b = len(word2)

    if a == b:
        return word1
    elif a > b:
        return word1
    else:
        return word2


# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
