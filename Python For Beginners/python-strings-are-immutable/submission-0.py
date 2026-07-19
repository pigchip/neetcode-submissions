def remove_fourth_character(word: str) -> str:
    a = word[:4]
    b = word[5:]

    return a + b

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
