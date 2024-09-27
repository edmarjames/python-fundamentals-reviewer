# A RegEx, or Regular Expression, is a sequence of character that forms a search pattern.
# Regex can be used to check if a string contains the specified search pattern.
# Python has a built-in package called "re", which can be used to work with Regular Expressions.
import re

# The findall() function
# The "findall()" function returns a list containing all matches.
txt = "The rain in spain"
match = re.findall("^[tT]h.", txt)
print(match)

print("\r")
# The search() function
# The "search()" function searches the string for a match, and returns a "match object" if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned.
search_result = re.search("in", txt)
print(search_result)

# A match object is an object containing information about the search and the result.
# The match object has properties and methods used to retrieve information about the search and the result.

# .span() - returns a tuple containing the start-, and end positions of the match.
print(search_result.span())

# .string - returns the string passed into the function
print(search_result.string)

# .group() - returns the part of the string where there was a match
print(search_result.group())

print("\r")
# The split() function
# The "split()" function returns a list where the string has been split at each match.
# You can control the number of occurrences by specifying the "maxsplit" parameter.
split_result = re.split("a", txt)
print(split_result)

max_split_result = re.split("a", txt, 1)
print(max_split_result)

print("\r")
# The sub() function
# The "sub()" function replaces the matches with the text of your choice.
# You can control the number of replacements by specifying the "count" parameter.
sub_result = re.sub("i", "I", txt)
print(sub_result)

max_sub_result = re.sub("i", "I", txt, 1)
print(max_sub_result)