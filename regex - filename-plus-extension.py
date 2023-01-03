import re
filename = "369585767401311965_Mlisa Kelley.txt"
"""Explanation of regex:
(?<=\_) Called a "Positive Lookbehind". The ?<= means this regex
is directly preceded (behind) the regex pattern that follows. So
[A-Za-z\-\_ ]+\.[a-z]+ comes right AFTER an underscore \_
[A-Za-z\-\_ ] Any letter between A-Z or a-z or a dash or an underscore
or a space, which matches Mlisa Kelley, Mlisa-Kelley, or Mlisa_Kelley
+ one or more 
\. a literal dot
[a-z]+ One or more letters between a-z which matches mlisakelley"""
regex = r"(?<=\_)[A-Za-z\-\_ ]+\.[a-z]+"
for match in re.finditer(regex, filename):
    print(match.group())

filename = filename.split("_")
print(filename)
print(filename[-1])