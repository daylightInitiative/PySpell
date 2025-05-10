import difflib
import sys

# that finds all misspelled words in the text
def find_misspelled_words(text, dictionary) -> bool:
    pass

# finds and suggests corrections for a misspelled word
def suggest_corrections(word, dictionary) -> []:
    pass

# allows the user to add a new word to the dictionary
def add_word_to_dictionary(word, dictionary):
    print("Do you want to add it to the dictionary? (y/n)")
    add_dictionary = input("").lower().strip()

    if add_dictionary.lower() in ("y", "yes"):

        print(f"Added {word} to the dictionary")
        dictionary.append(word)

    else: 
        pass

# loads the dictionary and returns it without newlines
def load_dictionary(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

# https://pypi.org/project/cdifflib/
# interesting for large autocompletions

#import english_words
#dictionary = english_words.get_english_words_set(['gcide'], lower=True)

# using
# https://python.sdv.u-paris.fr/data-files/english-common-words.txt


def main():
    print("PySpell word spelling checker")

    dictionary = load_dictionary("english-common-words.txt")

    while True:
        prompt = input(">>> ").lower()
        
        if prompt != "":
            #print(prompt)

            # create an array for suggested words
            #newWords = []
            for word in prompt.split():
                if word.lower() not in [w.lower() for w in dictionary]:
                    print(f"I didn't find '{word}' in the dictionary.")

                    result = difflib.get_close_matches(word, dictionary, n=1, cutoff=0.6)
                    if result:
                        print(f"\nDid you mean: {result[0]}?")
                    else:
                        print("No matches found.")

                    add_word_to_dictionary(word, dictionary)
                    
                        
                else:
                    print(f"'{word}' is spelled correctly.")



if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print("Exiting")
        sys.exit(0)