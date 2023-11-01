import random
sentence = "what is the Aiespeed velocity of an Unladen Swallow?"

sentence_split = {letter: random.randint(
    10, 100)for letter in sentence.split()}

print(sentence_split)
