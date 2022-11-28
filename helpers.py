def letters_in_word(letters, word):
    for letter in letters:
        if letter not in word:
            return False
    return True

def letters_not_in_word(letters, word):
    for letter in letters:
        if letter in word:
            return False
    return True

def matches_known_positions(known_positions, word):
    first = known_positions.get("first", "")
    second = known_positions.get("second", "")
    third = known_positions.get("third", "")
    fourth = known_positions.get("fourth", "")
    fifth = known_positions.get("fifth", "")

    matches_first = word[0] == first if first else True
    matches_second = word[1] == second if second else True
    matches_third = word[2] == third if third else True
    matches_fourth = word[3] == fourth if fourth else True
    matches_fifth = word[4] == fifth if fifth else True

    return matches_first and matches_second and matches_third and matches_fourth and matches_fifth
 
def return_relevant_words(words, known_letters_pos, known_letters_neg, **kwargs):
    words = words.splitlines()
    words = [word.strip() for word in words]
    five_letter_words = [word for word in words if len(word) == 5]
    known_positions = kwargs.get("known_positions")
    relevant_words = [
        word for word in five_letter_words 
        if letters_in_word(known_letters_pos, word)
        and letters_not_in_word(known_letters_neg, word)
        and matches_known_positions(known_positions, word)
    ]
    return relevant_words

def parse_known_positions(known_positions: str):
    order_keys = {
        "1": "first",
        "2": "second",
        "3": "third",
        "4": "fourth",
        "5": "fifth",
    }
    final_kp = {}
    known_positions = [c for c in known_positions]
    for idx, c in enumerate(known_positions):
        if c == "_":
            continue
        key = order_keys[str(idx + 1)]
        final_kp[key] = c
    return final_kp
