code = {"A": "*_", "B": "_***", "C": "-*-*", "D": "-**", "E": "*", "F": "**-*",
        "G": "--*", "H": "****", "I": "**", "J": "*--", "K": "-*-", "L": "*-**",
        "M": "--", "N": "-*", "O": "---", "P": "*--*", "Q": "--*-", "R": "*-*",
        "S": "***", "T": "-", "U": "**-", "V": "***-", "W": "*-", "X": "-**-",
        "Y": "-*--", "Z": "--**", "1": "*----", "2": "**---", "3": "***--",
        "4": "****-", "5": "*****", "6": "-****", "7": "--***", "8": "---**", "9": "----*"}

keys = code.keys()
list_of_letters = []
morse_word = ""


def letter_to_morse(letter):
    letter = letter.upper()
    if letter in keys:
        return str(code[letter])


word = input("Text to convert: ")
for i in word:
    if i and i.strip():
        morse_signal = letter_to_morse(i)
        morse_word += morse_signal + " "
    else:
        morse_word += " "
print(morse_word)



