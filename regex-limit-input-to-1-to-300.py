import re

#Explanation of regex:
"""(?<!-) Asserts that what immediately precedes the 
current position in the string is not a - (negative sign)
(Will exclude negative numbers, in the absence of no match for 1-300)
[1-9](st|nd|rd|th)? will match any digit from 1-9 by 
itself or with an optional (? = 0 or more.  Hence optional) (st|nd|rd|th) 
for 1st or 2nd or 3rd etc 
[1-9][0-9](th)? Will match any number from 10 to 99 and the optional th
for 10th, 12th, 20th etc.
[1-2][0-9][0-9](st|nd|rd|th)? Will match any number from 100 to 299
and the optional (st|nd|rd|th) for 101st, 102nd, etc
|300(th)? | means 'or' Will match 300 by itself, or 
with the optional th for 300th"""

while True:
    user_input = input("Enter your input: ")
    regex = r'\b(?<!-)([1-9](st|nd|rd|th)?|[1-9][0-9](th)?|[1-2][0-9][0-9](st|nd|rd|th)?|300(th)?)\b'
    """REGEX EXPLAINED:
    ([1-9](st|nd|rd|th)? Matches 1-9 and optional 1st, 2nd, 3rd, 4th, etc
    [1-9][0-9](th)? Matches 10-99 and optional 10th, 11th, etc.
    [1-2][0-9][0-9](st|nd|rd|th)? Matches 100-299 and optional...
    300(th)? Matches 300 or optional 300th
    All those combined match 1-300 or optional...
    """

    for match in re.finditer(regex, user_input):
        beginning = match.start()
        end = match.end()
        print("There is a match of %s at %d:%d" %
              (user_input[beginning:end], beginning, end))
        print(f"There is a match of {match.group()} at {beginning}:{end}")
        print(f"There is a match of {match.group()} at {match.span()}")

