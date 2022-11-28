from helpers import (letters_in_word, letters_not_in_word,
                     matches_known_positions, parse_known_positions,
                     return_relevant_words)


def test_letters_in_word():
    letters = "tia"
    word = "tibia"
    result = letters_in_word(letters, word)
    assert result

    letters = "ab"
    word = "tennessee"
    result = letters_in_word(letters, word)
    assert not result

def test_letters_not_in_word():
    letters = "tia"
    word = "tibia"
    result = letters_not_in_word(letters, word)
    assert not result

    letters = "ab"
    word = "tennessee"
    result = letters_not_in_word(letters, word)
    assert result

def test_matches_known_positions():
    first_word = "tibia"
    second_word = "tacit"
    third_word = "await"
    known_position = {
        "first": "t",
    }

    assert matches_known_positions(
        known_positions=known_position,
        word=first_word,
    )
    assert matches_known_positions(
        known_positions=known_position,
        word=second_word,
    )
    assert not matches_known_positions(
        known_positions=known_position,
        word=third_word,
    )


    first_word = "trais"
    second_word = "thais"
    third_word = "chasis"

    known_position = {
        "first": "t",
        "third": "a",
        "fifth": "s",
    }

    assert matches_known_positions(
        known_positions=known_position,
        word=first_word,
    )
    assert matches_known_positions(
        known_positions=known_position,
        word=second_word,
    )
    assert not matches_known_positions(
        known_positions=known_position,
        word=third_word,
    )

def test_return_relevant_words():
    words = """await
    habit
    haiti
    tibia
    hello
    loony
    """
    known_letter_pos = "tia"
    known_letters_neg = "roeslcknfumed"
    known_positions = {
        "first": "t",
    }
    results = return_relevant_words(
        words=words,
        known_letters_pos=known_letter_pos,
        known_letters_neg=known_letters_neg,
        known_positions=known_positions,
    )
    expected_words = ["tibia"]
    assert expected_words == results

    known_positions = {}
    expected_words = ["await", "habit", "haiti", "tibia"]
    results = return_relevant_words(
        words=words,
        known_letters_pos=known_letter_pos,
        known_letters_neg=known_letters_neg,
        known_positions=known_positions,
    )

def test_parse_known_positions():
    kp = "_e__l"
    result = parse_known_positions(kp)
    expected = {"second": "e", "fifth": "l"}
    assert result == expected

    kp = ""
    result = parse_known_positions(kp)
    assert result == {}
