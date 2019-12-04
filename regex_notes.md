# Regular Expressions
A regular expression is a sort of meta-language that can be used to describe patterns in text.

Regexes are most commonly used in one of two ways:

## Usage
- To find/extract text that matches a pattern.
- To replace/substitute text that matches a pattern.

## Now We Know
- Regular expressions can be concatenated to form new regular expressions; if A and B are both regular expressions, then AB is also a regular expression.

## Best Practices
- `print(r'Use raw strings whenever possible')`
- Most ordinary characters, like 'A', 'a', or '0', are the simplest regular expressions; they simply match themselves.

## Vocabulary
- Character Class is a set of characters that we wish to match

## Metacharacters and Character classes
| metacharacter | matches                                 |
| ------------- | --------------------------------------- |
| `.`           | anything                                |
| `[^n]`        | anything except for regex after the ^   |
| `^`           | starts with pattern after the ^         |
| `*`           | zero or more times                      |
| `+`           | one or more times                       |
| `?`           | matches either once or zero times       |
| `$`           |   
| `?`           |
| `{}`          |
| `/`           |
| `\`           |
| `()`          |
| `[` and `]`   | Specify a character class               |
| `\w`          | any letter or number is `[a-zA-Z0-9_]`  |
| `\W`          | anything not a letter or number         |
| `\d`          | any digit, equivalent to `[0-9]`        |
| `\D`          | anything not a digit, is `[^0-9]`       |
| `\s`          | any whitespace character `[\t\n\r\f\v]` |


## Now We Know
- Metacharacters inside a character class match that character.  Metacharacters are not active inside classes. 
- Some of the special sequences beginning with '\' represent predefined sets of characters that are often useful, such as the set of digits, the set of letters, or the set of anything that isn’t whitespace.
- Repetitions such as * are greedy (meaning they keep going through the haystack)

## Examples
- `[abc]` matches the same as `[a-c]`
- `[a-z]` matches all lowercase characters a through z
- `[abc$]` matches all a, b, c, or $ characters b/c metacharacters are not active inside of classes
- `[^5]` matches any character except for 5
- `[4^]` matches all `4` or `^` characters in the class
- `[\s,.]` matches all whitespace characters, `.`, or `,`
- `re.findall(r'[^3]', "123")` returns `["1", "2"]`
- `re.findall(r'[^2-7]', "123456789")` returns `["1", "8", "9"]`
- `ca*t` matches `ct`, `cat`, `caat`, and `caaaaat`
- `ca+t` matches `cat`, `caat`, etc.. but no `ct` b/c `+` requires at least one occurrence.

## More Exercises 
- https://www.w3resource.com/python-exercises/re/
- https://developers.google.com/edu/python/exercises/baby-names

## Reference
- Library Reference - https://docs.python.org/3/library/re.html
- How To - https://docs.python.org/3/howto/regex.html
- https://developers.google.com/edu/python/regular-expressions#repetition

## RE Methods
- `.match()` determines if the RE matches at the beginning of the string
- `.search()` scans the entire string
- `.findall()` finds all substrings where the RE and returns them as a list
- `.finditer` finds all substrings and returns an iterator (for lazy usage)


## Match Object Methods
- `.group()` return the string matched by the RE
- `.start()` return the starting position of the match
- `.end()` return the ending position of the match
- `.span()` return a tuple containing (start, end) positions of the match

## Anchors
There are several special metacharacters that don't match any individual characters, but serve as an "anchor" for the rest of the regular expression.

| metacharacter |  matches                       |
| ------------- | ------------------------------ |
| `^`           | The start of the string/line   |
| `$`           | The end of the string/line     |
| `\b`          | A word boundary                |




re.sub(needle, replacement, haystack)