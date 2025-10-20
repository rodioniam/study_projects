# anagram checker. Check if user inputed words are anagrams
user_input_word_1 = input('Enter word: ')  # Live
user_input_word_2 = input('Enter word: ')  # Evil


def text_input():
    word_1 = user_input_word_1.lower()
    word_2 = user_input_word_2.lower()
    return sorted(word_1) == sorted(word_2)


def text_check():
    if text_input():
        print(
            f"Words '{user_input_word_1}' and '{user_input_word_2}' are anagrams.")
    else:
        print(
            f"Words '{user_input_word_1}' and '{user_input_word_2}' are not anagrams.")


text_check()


# display how many days are in user inputed month.
days_31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
days_30 = ['April', 'June', 'September', 'November']
days_28 = 'February'
user_input = input('Enter month: ')


def month_check():
    if user_input in days_31:
        print(f'{user_input} has 31 days')
    elif user_input in days_30:
        print(f'{user_input} has 30 days')
    elif user_input == days_28:
        print(f'{user_input} has 28 or 29 days')
    else:
        print('There is no such month')


month_check()


# display how many days does month have depending on the year
user_input_year = int(input('Please enter year: '))
user_input_month = int(input('Please enter number of month: '))


def is_leap_year():  # checking if year is leap
    if user_input_year % 400 == 0 or (user_input_year % 4 == 0 and user_input_year % 100 != 0):
        return True  # True if leap
    return False  # False if not leap


def days_checker():
    if user_input_month in (1, 3, 5, 7, 8, 10, 12):
        return f'Month number {user_input_month} in {user_input_year} had 31 days'
    elif user_input_month == 2:
        if is_leap_year:
            return f'Month number {user_input_month} in {user_input_year} had 29 days'
        else:
            return f'Month number {user_input_month} in {user_input_year} had 28 days'
    elif user_input_month > 12:
        return 'Month is not valid'
    else:
        return f'Month number {user_input_month} in {user_input_year} had 30 days'


dc = days_checker()

print(dc)
