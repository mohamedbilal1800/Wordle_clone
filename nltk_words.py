from nltk.corpus import words
from nltk.corpus import wordnet

# nltk.download('words')
# nltk.download('wordnet')

word_list = words.words()

# Filtering to get only 5-letter words
five_letter_words = [word.lower() for word in word_list if len(word) == 5]

def is_meaningful(word):
    return bool(wordnet.synsets(word))
    # Returns True if the word has a meaning

# Filtering out only meaningful 5-letter words
meaningful_five_letter_words = [word for word in five_letter_words if is_meaningful(word)]







# # Finding synsets for a word
# word = 'example'
# synsets = wordnet.synsets(word)
#
# # Displaying the first synset's definition (there might be multiple synsets)
# if synsets:
#     print(f"Definition of {word}: {synsets[0].definition()}")
#     print(synsets)
# else:
#     print(f"No synsets found for {word}")

