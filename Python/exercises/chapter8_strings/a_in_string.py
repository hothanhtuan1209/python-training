def count_a():
    """
    Count the number of occurrences of the character 'a' in the word 'banana'.

    Prints the count to the console.
    """

    word = 'banana'
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)


count_a()
