def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters = count_letters(text)
    alphabetic = [k for k in letters.keys() if k.isalpha()]
    sorted_keys = sorted(alphabetic)
    sorted_dict = {k: letters[k] for k in sorted_keys}
    print_report(book_path, num_words, sorted_dict)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_letters(text):
    letters = {}
    words = text.split()
    for i in range(0, len(words)):
        word = words[i].lower()
        for l in word:
            if l in letters:
                cur_value = letters[l]
                update = cur_value + 1
                letters[l] = update
            else:
                letters[l] = 1
    return letters

def sort_on(dict):
    return dict["char"]

def print_report(path, words, chars):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    for key in chars:
        print(f"The '{key}' was found {chars[key]} times")

main()
