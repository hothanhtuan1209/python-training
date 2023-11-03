"""
This module has the function of reading and retrieving the content of a file
"""


def read_file_content(file_path):
    """
    Read and return the content of a text file.

    Args:
        file_path (str): The path to the input file to be read.

    Returns:
        str or None: The content of the file if successful, or None if there
        was an error.
    """

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        return content

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

        return None

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

        return None
