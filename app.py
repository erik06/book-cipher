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
