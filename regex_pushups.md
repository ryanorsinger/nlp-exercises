## Consider the Following Expressions

## From English to Regex
- Write a function named is_consonant that takes in a string and returns True/False 
- Write a function named get_lowercase_letters that takes in a string and returns only the lower cased letters in order from left to right with no numbers or symbols
- Write a function named get_uppercase_letters that takes in a string and returns only the uppercased characters with no numbers or symbols
- Write a function named is_digit that takes in a string and returns True if that string is a single digit
- Write a function named is_only_digits that takes in a string and returns True/False if the string is only composed of digits
- Write a function named is_all_the_same_character that takes in a string and returns True/False if the entire string is composed of exactly the same character.
- Write a function named starts_with_vowel that returns True/False
- Write a function named ends_with_vowel that returns True/False
- Write a function named starts_and_ends_with_vowel that returns True/False
- Write a function named contains_one_consonant that returns True/False
- Write a function named contains_one_vowel that returns True/
- Given the sentence "12 drummers drumming, 11 pipers piping, 10 lords a-leaping", write the regex necessary to get only the number characters as a list.

## From Regex to English
- `a[bcd]*b`, what does this do?
- `ca*t`
- `ca+t`
- `[a-z]+`
- `\d+`

## How To
- Ignore Case: re.findall(needle, haystack, re.IGNORECASE) or 



Find all occurrences of one capital character followed by four or more letters.

# Find the last digit in the string
re.findall(r'\d$', "ba323b9")

# Find the last 3 digits of a string
re.findall(r'\d{3}$', "ba323b29222")

# Find the last character of the string
re.findall(r'.$', "whatever")

# Find two of anything at the end of a string
re.findall(r'.{2}$', "whatever")




# Find the first letter of every word
\b is an anchor for a word boundary
