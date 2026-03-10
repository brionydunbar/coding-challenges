###################################################################
# 2. Average Words Length

# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

import string # import string to use string.punctuation

def solution2(sentence):
    translator = str.maketrans("", "", string.punctuation) # use maketrans method to map and remove punctuation
    clean_text = sentence.translate(translator)
    split_text = clean_text.split() # split the clean text into a list
    avg = sum(len(word) for word in split_text) / len(split_text) # calculate the avg
    return float(round(avg, 2)) # round to 2 d.p.

sentence1 = "Hi class, we are practicing solving algorithms. It is fun, don't you think?.."
sentence2 = "We need to work very hard to learn more about algorithms!"

print(solution2(sentence1))
print(solution2(sentence2))

