import string
def letters_count(text, letters= string.ascii_letters):
    letters = frozenset(letters)
    count = 0
    for chr in text:
        if chr in letters:
            count+=1
    return count
