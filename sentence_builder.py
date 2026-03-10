"""
Implement a function, so it will produce a sentence out of the given parts.

Array of parts could contain:

words;
commas in the middle;
multiple periods at the end.
Sentence making rules:

there must always be a space between words;
there must not be a space between a comma and word on the left;
there must always be one and only one period at the end of a sentence.
Example:

makeSentence(['hello', ',', 'my', 'dear']) // returns 'hello, my dear.'
"""

import string

def make_sentences(parts):
    sentence = ""
    for i, part in enumerate(parts): # iterate through each part along with its index
        if part in string.punctuation:
            sentence = sentence.rstrip() + part # strip the trailing space then attach the punctuation directly
        else: # if not punctuation then a word
            if i > 0: # if not the first word, add a space first
                sentence += " "
            sentence += part # add the word
    sentence = sentence.rstrip(".") + "." # ensure one full stop at end
    return sentence

print(make_sentences(["hello", "world"]))
print(make_sentences(["hello", ",", "my", "dear"]))