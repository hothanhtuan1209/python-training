"""
This is the main entry point for the program.
It calls the main function from modules.
"""


from path1 import (
    age_condition_checker,
    abecedarian_word_counter,
    forbidden_letter_counter,
    word_e_checker,
    symmetrical_numbers,
)


modules = [
    age_condition_checker,
    abecedarian_word_counter,
    forbidden_letter_counter,
    word_e_checker,
    symmetrical_numbers,
]


def main():
    """
    To run all files code in practice-3 through main.py file
    """

    for module in modules:
        module.main()


if __name__ == "__main__":
    main()
