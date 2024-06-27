"""
A little assignment to practice receiving text input from the user in Python programming.
Do not run this file... run main.py instead.
"""
def print_with_line_break():
  """
  Prints out the text, 'Hello world!' with a line break at the end
  """
  # write your code here

def get_favorite_vegetable():
    """
    Asks the user to enter their favorite vegetable
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite vegetable.
    """
    vegetable = input("Please enter your favorite vegetable: ")
    print(f"Interesting! I also love {vegetable}!")


def get_favorite_number():
    """
    Asks the user to enter their favorite number
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite number.
    """
    number = input("Please enter your favorite: ")
    print(f"Interesting! I also love {number}!")


def get_name_and_zodiac_sign():
    """
    Asks the user to enter their name.
    Then ask them to enter their zodiac sign.
    Then print out, "Interesting! My name is also X, and I'm also a Y!",
    where X and Y are replaced by the user's name and zodiac sign, respectively.
    """
    name = input("Please enter your name: ")
    zodiac_sign = input("Please enter your zodiac sign: ")
    print(f"Interesting! My name is also {name}, and I'm also a {zodiac sign}!")
    


def get_name_and_age():
    """
    Asks the user to enter their name.
    Then ask them to enter their age.
    Then print out, "Interesting! My name is also X, and I'm also Y years old!",
    where X and Y are replaced by the user's name and age, respectively.
    """
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    print(f"Interesting! My name is also {name}, and I'm also {age} years old!")
