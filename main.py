from helpers import parse_known_positions, return_relevant_words
from words import words

if __name__ == "__main__":
    known_letters_positive = input("Letters that exist: ")
    known_letters_negative = input("Letters that don't exist: ")
    known_positions = input("Known positions: ")
    known_positions = parse_known_positions(known_positions)

    result = return_relevant_words(
        words, 
        known_letters_pos=known_letters_positive,
        known_letters_neg=known_letters_negative,
        known_positions=known_positions,
    )
    print(result)
