def word_count(text):
    words = text.split()
    return len(words)


def letter_count(text):
    letters = text.lower()
    letters_count = {}

    for char in letters:
        if char in letters_count:
            letters_count[char] += 1
        else:
            letters_count[char] = 1

    return letters_count

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
