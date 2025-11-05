from stats import get_num_words, count_characters, sort_map
import sys

if len(sys.argv)<2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents



def main():
        book_path = sys.argv[1]
        res = get_book_text(book_path)
        num_words = get_num_words(res)
        char_map = count_characters(res)
        map_sorted = sort_map(char_map)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in map_sorted:
                if not item["char"].isalpha():
                        continue
                print(f"{item['char']}: {item['num']}")

        print("============= END ===============")  


main()

