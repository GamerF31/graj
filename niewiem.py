# -*- coding: utf-8 -*-
import re
from string import whitespace
from collections import Counter

text = input("Wpisz tekst :")

vowels = "aeiouyóęą"
digits = "0123456789"
counter = Counter(text)
consonants = "qwrtpsdfghjklzxcvbnmńśćżźł"
vowels_count = 0
digits_count = 0
not_alphanumeric_count = 0
others_count = 0
consonants_count = 0

for key, value in counter.items():
    formatted_char = str(key).lower()
    if formatted_char in vowels:
        vowels_count += 1
    elif formatted_char in digits:
        digits_count += 1
    elif not formatted_char.isalnum():
        not_alphanumeric_count += 1
    if formatted_char in consonants:
        consonants_count += 1
    else:
        others_count += 1

print("Ilość samogłosek to", vowels_count)
print("Ilość cyfr to", digits_count)
print("Ilość spóółgłosek to", consonants_count)
print("Ilość innych znaków to", not_alphanumeric_count)