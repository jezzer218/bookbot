from stats import *
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = word_count(text)
    letters = letter_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(letters)
    print_report(book_path, words, chars_sorted_list)
    




def get_book_text(file_path):
    with open(file_path) as b:
        return b.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")




if __name__ == "__main__":
    main()
