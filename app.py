import sys
import os
import random
from collections import defaultdict, Counter


def main():
    message = input("Enter plaintext or ciphertext: ")
    process = input("Enter 'encrypt' or 'decrypt': ")
    while process not in ("encrypt", "decrypt"):
        process = input("Invalid process. Enter 'encrypt' or 'decrypt': ")
    shift = int(input("Shift value \(1-366\) = "))
    while not 1 <= shift <= 366:
        shift = int(input("Invalid value. Enter digit from 1 - 366: "))
    infile = input("Enter filename with extension: ")

    if not os.path.exists(infile):
        print("File {} not found. Terminiating.".format(infile), file=sys.stderr)
        sys.exit(1)
    text = load_file(infile)
    char_dict = make_dict(text, shift)

    if process == "encrypt":
        ciphertext = encrypt(message, char_dict)
        if check_for_fail(ciphertext):
            print("\nProblem finding unique keys.", file=sys.stderr)
            print("Try again, change message, or change code book.\n", file=sys.stderr)
            sys.exit()
        print("\nCharacter and number of occurances in char_dict: \n")
        print("{:>10}{:>10}{:>10}".format("Character", "Unicode", "Count"))
        for key in sorted(char_dict.keys()):
            print(
                "{:>10}{:>10}{:>10}".format(
                    repr(key)[1:-1], str(ord(key)), len(char_dict[key])
                )
            )
        print("\nNumber of distinct charcters: {}".format(ciphertext))
        print("decrypted plaintext = ")

        for i in ciphertext:
            print(text[i - shift], end="", flush=True)

    elif process == "decrypt":
        plaintext = decrypt(message, text, shift)
        print("\ndecrypted plaintext = \n {}".format(plaintext))


def load_file(infile):
    """Read and return text file as a string of lowercase characters."""
    with open(infile) as f:
        loaded_string = f.read().lower()
    return loaded_string


def make_dict(text, shift):
    """Return dictionary of characters and shifted indexes."""
    char_dict = defaultdict(list)
    for index, char in enumerate(text):
        char_dict[char].append(index + shift)
    return char_dict


def encrypt(message, char_dict):
    """Return list of indexes representing characters in a message"""
    encrypted = []
    for char in message.lower():
        if len(char_dict[char]) > 1:
            index = random.choice(char_dict[char])
        elif len(char_dict[char]) == 1:  # Random.choice fails if only one choice
            index = char_dict[char][0]
        elif len(char_dict[char]) == 0:
            print("\nCharacter {} not in dictionary.".format(char), file=sys.stderr)
            continue
        encrypted.append(index)
    return encrypted
