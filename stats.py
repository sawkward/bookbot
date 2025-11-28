def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    return text

def get_num_words(text):
        text = str(main())
        words = text.split()
        num_words = len(words)
        print(f"Found {num_words} total words")

def get_chars_dict(text):
	text = text.lower()
	character_dict = {}
	for character in text:
		if character in character_dict:
			character_dict[character] += 1
		else:
			character_dict[character] = 1
	return character_dict

def sort_on(d):
	return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
	sorted_list = []
	for ch in num_chars_dict:
		sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list
