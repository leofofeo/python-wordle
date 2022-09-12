from helpers import return_relevant_words
from words import words

known_letters_positive = "oe"
known_letters_negative = "ratslick"
known_positions = {
    "second": "o",
    "fifth": "e",
}

if __name__ == "__main__":
    result = return_relevant_words(
        words, 
        known_letters_pos=known_letters_positive,
        known_letters_neg=known_letters_negative,
        known_positions=known_positions,
    )
    print(result)
