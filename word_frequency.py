#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.?!]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

# Function to get and validate user input
def get_sentence():
    while True:
        sentence = input("Enter a sentence: ")
        if is_sentence(sentence):
            return sentence
        else:
            print("Invalid sentence. Sentence should start with a capital letter and end with a punctuation.")


# Function to calculate word frequencies
def calculate_frequencies(sentence):
    words = sentence.split() # Split sentence into words

    # Lists for unique words and their counts
    unique_words = []
    frequencies = []

    for word in words:
        # Clean up punctuations for counting
        word_clean = word.strip('.,!?')

        # Make lowercase for consistent counting
        word_clean = word_clean.lower()

        if word_clean in unique_words:
            index = unique_words.index(word_clean)
            frequencies[index] += 1
        else:
            unique_words.append(word_clean)
            frequencies.append(1)

    return unique_words, frequencies

# Function to print the frequencies
def print_frequencies(words, counts):
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {counts[i]}")


# Main program
def main():
    sentence = get_sentence()
    words, counts = calculate_frequencies(sentence)
    print_frequencies(words, counts)


# Run the program
main()
