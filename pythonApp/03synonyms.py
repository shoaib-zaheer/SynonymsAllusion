import time
textInOut = ""

def text_parser_synonym_maker(text:str):
    from nltk.corpus import wordnet
    from nltk.tokenize import word_tokenize
    from random import randint
    import nltk.data

    # Load a text file if required
    #text = "Pete ate a large cake. Sam has a big mouth."
    output = ""
    global textInOut

    # print("input", text)

    # Load the pretrained neural net
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    # Tokenize the text
    tokenized = tokenizer.tokenize(text)

    # Get the list of words from the entire text
    words = word_tokenize(text)

    # Identify the parts of speech
    tagged = nltk.pos_tag(words)

    for i in range(0,len(words)):
        replacements = []

        # Only replace nouns with nouns, vowels with vowels etc.
        for syn in wordnet.synsets(words[i]):

            # Do not attempt to replace proper nouns or determiners
            if  tagged[i][1] == 'NN' or tagged[i][1] == 'DT' or tagged[i][1] == 'PRP' or tagged[i][1] == 'WP' or tagged[i][1] == 'MD' or tagged[i][1] == 'VBZ':
                break

            # The tokenizer returns strings like NNP, VBP etc
            # but the wordnet synonyms has tags like .n.
            # So we extract the first character from NNP ie n
            # then we check if the dictionary word has a .n. or not
            word_type = tagged[i][1][0].lower()
            if syn.name().find("."+word_type+"."):
                # extract the word only
                r = syn.name()[0:syn.name().find(".")]
                replacements.append(r)

        if len(replacements) > 0:
            # Choose a random replacement
            replacement = replacements[randint(0,len(replacements)-1)]
            output = output + replacement + " "
        else:
            # If no replacement could be found, then just use the
            # original word
            output = output + words[i] + " "
    #print(output)
    textInOut = output

text_parser_synonym_maker(text="As metaphor, 'social space contributes a relational rather than an abstract dimension...has received a large variety of attributes, interpretations, and metaphors")
time.sleep(1)
for i in range(0,10):
    print(i, "inputstring: ", textInOut)
    text_parser_synonym_maker(text = textInOut)
    time.sleep(0.2)
