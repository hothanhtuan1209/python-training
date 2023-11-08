"""
This is the main entry point for the program.
It calls the main function from modules.
"""


from path1 import (
    age_condition_checker,
    required_letter_word_counter,
    long_words_printer,
    letter_validation,
    abecedarian_word_counter,
    forbidden_letter_counter,
    word_e_checker,
    symmetrical_numbers,
    triple_double_letters,
)

from path2 import (
    markov_analysis,
    missing_words_checker,
    random_dict,
    random_word_selector,
    word_frequencies_and_logs,
    no_whitespace_punctuation_words,
)


modules = [
    age_condition_checker,
    required_letter_word_counter,
    long_words_printer,
    letter_validation,
    abecedarian_word_counter,
    forbidden_letter_counter,
    no_whitespace_punctuation_words,
    markov_analysis,
    word_e_checker,
    triple_double_letters,
    symmetrical_numbers,
    random_word_selector,
    missing_words_checker,
    word_frequencies_and_logs,
    random_dict
]


def main():
    """
    To run all files code in practice-3 through main.py file
    """

    for module in modules:
        module.main()


if __name__ == "__main__":
    main()
