import re
from collections import Counter

SPACE_NORMALIZER = re.compile("\s+")


def word_tokenize(line):
    line = SPACE_NORMALIZER.sub(" ", line)
    line = line.strip()
    return line.split()


with open(f"europarl_raw/train.de", 'r') as inf:
    de_tokens_list = word_tokenize(inf.read())
    de_word_counts = Counter(de_tokens_list)

de_unk = [word for word, count in de_word_counts.items() if count == 1]

print("German tokens: ", len(de_tokens_list))
print("German word types: ", len(set(de_tokens_list)))
print("German tokens replaced by UNK: ", len(de_unk))
print("Tokens after UNK: ", len(set(de_tokens_list) - set(de_unk)))

with open(f"europarl_raw/train.en", 'r') as inf:
    en_tokens_list = word_tokenize(inf.read())
    en_word_counts = Counter(en_tokens_list)

en_unk = [word for word, count in en_word_counts.items() if count == 1]

print("English tokens: ", len(en_tokens_list))
print("English word types: ", len(set(en_tokens_list)))
print("English tokens replaced by UNK: ", len(en_unk))
print("Tokens after UNK: ", len(set(en_tokens_list) - set(en_unk)))

with open(f"unk_tokens.txt", 'w') as f:
    f.writelines("\n".join(sorted(en_unk)))

print("Shared tokens:", len(set(en_tokens_list).intersection(set(de_tokens_list))))
