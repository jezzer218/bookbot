def main ():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    words_in_book = word_count(text)
    print(f"{words_in_book} words found in the document")
    count_char(text)
    
        
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
        print(char)
        #if char in char_dict:
            #char[count + 1]
    
        
main()