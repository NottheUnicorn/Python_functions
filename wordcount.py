import re
import collections

def count_words(path):
    with open(path, encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-z']+", file.read())
        all_words = [word.upper() for word in all_words]
        print('\Total Words:', len(all_words))

        word_counts = collections.Counter(all_words)

        print('\n Top 20 Words:')
        for word in word_counts.most_common(20):
            print(word[0], '\t', word[1])