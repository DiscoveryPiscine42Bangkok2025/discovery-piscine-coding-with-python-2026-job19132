#!/Users/mrmeowz/.pyenv/shims/python
number = input("Give me a number: ")
number_ch = float(number)

if number_ch.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
