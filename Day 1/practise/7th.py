#check the alphabet is vowel or consonent

char = input("Enter a letter: ")
def check_alphabet(char):
    vowels = "aeiou"
    if char in vowels:
        print(f"{char} is a vowel.")
    elif char.isalpha():
        print(f"{char} is a consonant.")
    else:
        print(f"{char} is not a valid alphabet.")

check_alphabet(char)