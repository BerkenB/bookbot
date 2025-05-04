from stats import word_counter, character_counter, dict_to_sorted_list
import sys
if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
def main():
    file_path = sys.argv[1]
    words = get_book_text(file_path)
    num_words = word_counter(words)
    char_count = character_counter(words)
    sorted_list = dict_to_sorted_list(char_count)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for char in sorted_list:
        if char['char'].isalpha():
            print(f'{char['char']}: {char['num']}')
    
    print('============= END ===============')
    

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

main()
