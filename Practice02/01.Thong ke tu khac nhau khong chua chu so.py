import re

if __name__ == "__main__":
    input_data = ""
    for _ in range(int(input())):
        line = input()
        input_data += line + " "
    words = re.split(r'[^a-zA-Z]+', input_data)
    fre_dict = {}
    for word in words:
        word = word.lower()
        if word in fre_dict:
            fre_dict[word] += 1
        else:
            fre_dict[word] = 1
    sorted_words = sorted(fre_dict.items(), key=lambda x: (-x[1], x[0]))
    for word, freq in sorted_words:
        if word:
            print(f"{word} {freq}")
        