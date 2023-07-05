def calculate_age(number):
    age_reverse = list(str(number))
    reversed_number = int(''.join(age_reverse[::-1]))
    if int(number) + 36 == reversed_number:
        print(number)
def reverse_age():
    for number in range(0, 100):
        add_number_0 = str(number).zfill(2)
        calculate_age(add_number_0)
reverse_age()
