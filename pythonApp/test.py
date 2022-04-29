from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from random import randint
import nltk.data

text = "He is a good boy, that speaks English fast."

output = ""

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
tokenized = tokenizer.tokenize(text)
words = word_tokenize(text)
tagged = nltk.pos_tag(words)
print(tagged)
for i in range(0, len(words)):
    replacements = []

    for syn in wordnet.synsets(words[i]):

        if tagged[i][1] == 'NN' or tagged[i][1] == 'DT' or tagged[i][1] == 'PRP' or tagged[i][1] == 'WP' or tagged[i][1] == 'MD' or tagged[i][1] == 'VBZ':
            break

        word_type = tagged[i][1][0].lower()

        if syn.name().find("." + word_type + "."):
            r = syn.name()[0:syn.name().find(".")]

            replacements.append(r)

    if len(replacements) > 0:
        replacement = replacements[randint(0, len(replacements) - 1)]
        output = output + " " + replacement
    else:

        output = output + " " + words[i]

print(output)