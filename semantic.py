# pylint: disable=line-too-long
'''NLP task'''
import spacy # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use

# Below is a list of 5 words, 3 given and 2 examples
words = ['cat', 'monkey', 'banana', 'mouse', 'tom']

# Looping through the list of words and comparing each item with itself and all other items
for word in words:
    word = nlp(word)
    for word_ in words:
        word_ = nlp(word_)
        print(word.similarity(word_))

# When comparing these words, we can observe interesting patterns in their semantic relationships:

# Animal Category: Both "cat" and "monkey" belong to the category of animals, specifically mammals.
# They also share a predator-prey relationship as cats are known to prey on monkeys in some regions.

# "Banana" is not an animal, but monkeys are known to consume bananas.
# This association may stem from the popularity of monkeys depicted in media as banana-eating animals.

# Contextual Overlaps: Besides both being animals, "cat" and "mouse" have a well-known cultural association
# due to the classic adversarial relationship between cats and mice, often portrayed in cartoons, and popular culture.

# The word "Tom" is a proper noun, referring to a person's name. I was hoping for an higher semantic similarity betwwen "cat" and "tom"
# beacause male domesticated cats are often called "tom cats", but it seems that without additional context, the model cannot make the association

# From the output I recieved after running the file with the 'en_core_web_sm' model instead of the 'en_core_web_sm',
# I learnt that the former is a smaller model and does not ship with 'word vectors' necessary to give useful similarity judgments
