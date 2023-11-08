def clean_words(text):
    """
    Clean a text by removing punctuation, converting words to lowercase,
    and counting the frequency of each word.

    Args:
        text (str): The input text to be processed.

    Returns:
        list of str: A list of cleaned words without punctuation and in
        lowercase.

    """

    cleaned_words = []

    for line in text:
        words = line.strip().split()

        for word in words:
            cleaned_word = "".join(c.lower() for c in word if c.isalnum())
            if cleaned_word:
                cleaned_words.append(cleaned_word)

    return cleaned_words
