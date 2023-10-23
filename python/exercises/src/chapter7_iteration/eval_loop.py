def eval_loop():
    """
    Repeatedly evaluate and display the result of user-provided expressions.

    This function prompts the user to enter mathematical expressions as
    strings and evaluates them using the 'eval' function. The results are
    printed, and the user can continue entering expressions until they enter
    'done' to finish the loop.

    The function keeps running until 'done' is entered, allowing the user
    to evaluate multiple expressions.
    """

    while True:
        input_values = input('enter an expression or done to finish: ')

        if input_values == 'done':
            break
        else:
            result = eval(input_values)
            print(result)
