word_list = [
    "another",
    "word",
    "in",
    "my",
    "amazing",
    "array",
    "because",
    "it",
    "is",
    "excellent",
    "original",
    "introduce",
    "nail",
    "friendship",
    "myth",
    "lily",
    "campaign",
    "pride",
    "diplomat",
    "deficit",
    "contain",
    "experience",
    "lease",
    "key",
    "fine",
    "umbrella",
    "fame",
    "record",
    "blast",
    "revenge",
    "crevice",
    "flourish",
    "fish",
    "remember",
    "lesson",
    "promotion",
    "defeat",
    "to",
    "flowers",
    "knit",
    "magnitude",
    "why",
    "engine",
    "realism",
    "close",
    "effect",
    "fly",
    "tire",
    "slab",
    "coup",
    "zero",
    "hostility",
    "pier",
    "rhythm",
]
#  DO NOT CHANGE ANY CODE ABOVE THIS LINE

print(word_list, '<< complete list of words')

# Task 1
first_three_words = word_list[:3]
print(first_three_words)

# Task 2
last_three_words = word_list[-3:]
print(last_three_words)

# Task 3
word_count = len(word_list)
print(word_count)

# Task 4
two_letter_words = [word for word in word_list if len(word) == 2]
print(two_letter_words)

# Task 5
longest_word = sorted(word_list, reverse=True, key=len)[0]
print(longest_word)

# Task 6
contains_c = [word for word in word_list if "c" in word]
print(contains_c)

# Task 7
reversed_words = word_list[::-1]
print(reversed_words)

# Task 8
import re
no_vowels = [word for word in word_list if re.search("^[^aeiou]*$", word)]
print(no_vowels)

# Task 9
repeated_letters = []
for word in word_list:
    for c in word:
        if word.count(c) > 1:
            repeated_letters.append(word)
            break

print(repeated_letters)