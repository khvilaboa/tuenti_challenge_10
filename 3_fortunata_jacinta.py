import os
import re
import sys
from collections import defaultdict

data_path = os.path.join("data", os.path.splitext(os.path.basename(sys.argv[0]))[0])

tc_filename = "submitInput"
tc_path = os.path.join(data_path, tc_filename)
tc_out_path = os.path.join(data_path, os.path.splitext(tc_filename)[0] + "_out")

book_path = os.path.join(data_path, "book.txt")
words = defaultdict(int)
#valid_chars = "abcdefghijklmnñopqrstuvwxyzáéíóúü"
invalid_chars_rgx = "[^abcdefghijklmnñopqrstuvwxyzáéíóúü]"


def get_valid_words(line):
    words = []
    line_valid = re.sub(invalid_chars_rgx, " ", line.lower())
    for word in line_valid.split():
        if word != "" and len(word) >= 3:
            words.append(word)
    #print(line, words)
    return words


def sort_word_slice(word_list, start_idx, end_idx):
    words_slice = word_list[start_idx:end_idx]
    word_list[start_idx:end_idx] = sorted(words_slice)


with open(book_path, "r") as book_file:
    for line in book_file.readlines():
        if line == "":
            continue

        line_words = get_valid_words(line)
        for lw in line_words:
            words[lw] += 1


words_decreasing_order = sorted(words, key=words.get, reverse=True)
#print(words_decreasing_order)
start_idx = None
last_count = None

for idx, word in enumerate(words_decreasing_order):
    word_count = words[word]

    if word_count == last_count:
        if start_idx is None:
            start_idx = idx-1
    elif start_idx is not None:
        #print([(w, words[w]) for w in words_decreasing_order[start_idx-1:idx+1]])
        sort_word_slice(words_decreasing_order, start_idx, idx)
        #print([(w, words[w]) for w in words_decreasing_order[start_idx - 1:idx + 1]])
        start_idx = None

    last_count = word_count

if start_idx is not None:
    sort_word_slice(words_decreasing_order, start_idx, len(words_decreasing_order))

with open(tc_path, "r") as in_file:
    with open(tc_out_path, "w") as out_file:
        num_tc = int(in_file.readline().strip())

        for cidx in range(1, num_tc + 1):
            in_data = in_file.readline().strip()

            if in_data.isnumeric():
                ranked_word = words_decreasing_order[int(in_data) - 1]
                word_count = words[ranked_word]
                resp = "%s %d" % (ranked_word, word_count)
            else:
                idx = words_decreasing_order.index(in_data)
                word_count = words[in_data]
                resp = "%d #%d" % (word_count, idx + 1)

            out_file.write("Case #%d: %s\n" % (cidx, resp))


