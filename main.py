def count_words(book):
    with open(book) as f:
        file_contents = f.read()
        
    word_list = file_contents.split()    
    
    return len(word_list)

def count_letters(book):
    letter_dict = {}
    
    with open(book) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
    
    word_list = file_contents.split()
    
    for word in word_list:
        for letter in word:
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    
    return letter_dict
    
def print_report(book):
    letter_dict = count_letters(book)
    letter_list = list(letter_dict)
    # letter_list = list(count_letters(book))
    letter_list.sort()
    
    words_count = count_words(book)
    
    print(f"--- Begin report of {book} ---")
    print(f"{words_count} words found in the document")
    print()
    for letter in letter_list:
        if letter.isalpha():
            print(f"The {letter} character was found {letter_dict[letter]} times")
    print(f"--- End report ---")

#test
book_path = "books/frankenstein.txt"
# print(count_words(book_path))
# print(count_letters(book_path))
print_report(book_path)