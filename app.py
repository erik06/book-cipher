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
