import re
from collections import defaultdict

def read(file_path):
    dictt = defaultdict(int)
    with open(file_path, 'r') as file:
        content = file.read()

    #tokens = re.split(r'\s+', content)       was thinking of using this but this wasn't handling punctuation correctly
    tokens = re.findall(r'\w+|[^\w\s]', content)   
    for token in tokens:
        if token != "":
            dictt[token] += 1
    # print(dictt, "\n")
    return dictt

def compute_pair_scores(splits):
    letter_freqs = defaultdict(int)
    pair_freqs = defaultdict(int)
    for word, freq in vocab.items():
        split = splits[word]
        for i in range(len(split) - 1):
            pair = (split[i], split[i + 1])
            letter_freqs[split[i]] += freq
            pair_freqs[pair] += freq
        letter_freqs[split[-1]] += freq

    scores = {}
    for pair, freq in pair_freqs.items():
        t1, t2 = pair
        score = freq / (letter_freqs[t1] * letter_freqs[t2])
        scores[pair] = score

    return scores


def merge_pair(x, splits):
    a , b = x
    for word in vocab:
        split = splits[word]
        if len(split) == 1:
            continue
        i = 0
        while i < len(split) - 1:
            if split[i] == a and split[i + 1] == b:
                merge = a + b[2:]
                split = split[:i] + [merge] + split[i + 2 :]
            else:
                i += 1
        splits[word] = split
    return splits


vocab = read("wordpiece_input.txt")
alphabet = []

# for i in vocab.keys():
#     print(i)

for word in vocab.keys():
    if word[0] not in alphabet:
        alphabet.append(word[0])
    for letter in word[1:]:
        # print(word[1:])
        if f"##{letter}" not in alphabet:
            alphabet.append(f"##{letter}")
            # print(alphabet,"\n")

alphabet.sort()
# print(alphabet,"\n")

def split_word(word):
    return [word[0]] + [f"##{c}" for c in word[1:]]

splits = {word: split_word(word) for word in vocab.keys()}

# print(splits,"\n")

num_merges = 50
for i in range(num_merges):
    scores = compute_pair_scores(splits)
    #print(scores,"\n")
    best_pair = "" 
    max_score = -99
    for pair, score in scores.items():
        # print(pair,score)
        if score > max_score:
            best_pair = pair
            max_score = score
    splits = merge_pair(best_pair, splits)
    new_token = (best_pair[0] + best_pair[1][2:])
    print(f"Merged: {best_pair} ---> {new_token}")
    alphabet.append(new_token)






