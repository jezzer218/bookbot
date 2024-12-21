def main ():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    words_in_book = word_count(text)
    
    char_counted = count_char(text)
    sorted_list_chars = dict_to_list(char_counted)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_in_book} words found in the document")
    print()
    
    for i in sorted_list_chars:
        if not i["Character"].isalpha():
            continue
        print(f"The '{i['Character']}' character was found {i["Count"]} times")
    
    print("--- End report ---")
    
        
def get_book_text(path):
    
    with open(path) as f:
        return f.read()
    
def word_count(book):
    
    words = book.split()

    book_size = len(words)
    return book_size
def count_char(book):
    char_dict = {}
    for char in book:
        lower_case = char.lower()
        if lower_case in char_dict:
            char_dict[lower_case] += 1
        else:
            char_dict[lower_case] = 1
    return char_dict

def sort_on(key):
    return key["Count"]
    
def dict_to_list(char_dict):
    char_list = []
    for key in char_dict:
        char_list.append({"Character": key, "Count": char_dict[key]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
        
    
        
main()