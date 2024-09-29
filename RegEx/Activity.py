# Exercise 1: Extract Words Starting with a Specific Letter
# Write a function `extract_words` that takes a string and a letter as input and returns a list of all words in the string that start with the given letter (case insensitive). Use regular expressions.
    # **Input**: `"The quick brown fox jumps over the lazy dog"`, letter = `"t"`
    # **Expected Output**: `['The', 'the']`

# solution
import re
def extract_words(input_str, char):
    results = re.findall(f"{char}..", input_str, re.IGNORECASE)
    return results

result = extract_words("The quick brown fox jumps over the lazy dog", "t")
print(result)
# alternative solution
# def extract_words(input_str, char):
#     results = re.findall(rf"\b{char}\w*", input_str, re.IGNORECASE)
#     return results


print("\r")
### Exercise 2: Validate an Email Address
# Create a function `validate_email` that checks whether a given string is a valid email address using regex. A valid email should follow this pattern: it must start with one or more letters, numbers, dots, or underscores, followed by an `@` symbol, then a domain name that contains letters, numbers, and dots, and ends with a domain suffix like `.com`, `.org`, etc.
    # **Input**: `"test.email@domain.com"`
    # **Expected Output**: `True`
    # **Input**: `"invalid_email@domain"`
    # **Expected Output**: `False`

# solution
def validate_email(email_input):
    result = re.search("^.+\@.+.com|.org", email_input)
    if result:
        print(True)
    else:
        print(False)

validate_email("test.email@domain.com")
validate_email("invalid_email@domain")
# alternative solution
# def validate_email(email_input):
#     result = re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org)$", email_input)  # Improved regex
#     return bool(result)


print("\r")
# Exercise 3: Replace All Words with Length Greater Than N
# Write a function `replace_long_words` that takes a string and an integer `n`. It should replace every word in the string longer than `n` characters with the word `"REPLACED"`.
    # **Input**: `"The quick brown fox jumps over the lazy dog"`, n = 4
    # **Expected Output**: `"The REPLACED REPLACED fox REPLACED over the lazy dog"`

# solution
def replace_long_words(input_str, n_char):
    split_str = input_str.split(" ")
    for str_item in split_str:
        if len(str_item) > n_char:
            input_str = re.sub(f"{str_item}", "REPLACED", input_str)
    return input_str

result = replace_long_words("The quick brown fox jumps over the lazy dog", 4)
print(result)
# alternative solution
# def replace_long_words(input_str, n_char):
#     return re.sub(rf"\b\w{{{n_char+1},}}\b", "REPLACED", input_str)


print("\r")
# Exercise 4: Extract Domain from URL
# Write a function `extract_domain` that extracts the domain name from a given URL using regex. Ensure that it works with URLs that start with either `http`, `https`, or `www`.
    # **Input**: `"https://www.example.com/path"`
    # **Expected Output**: `"example.com"`
    # **Input**: `"http://sub.domain.org"`
    # **Expected Output**: `"sub.domain.org"`

# solution
def extract_domain(input_url):
    match = re.search(r"https?://(?:www\.)?([^/]+)", input_url)
    return match.group(1) if match else None

domain1 = extract_domain("https://www.example.com/path")
domain2 = extract_domain("http://sub.domain.org")
print(domain1)
print(domain2)
# alternative solution
# def extract_domain(input_url):
#     split_result = re.split("[a-zA-Z]+://w*\.*", input_url)
#     return split_result[-1]


print("\r")
# Exercise 5: Count Occurrences of a Pattern
# Create a function `count_pattern` that takes a string and a regex pattern, and returns the number of times the pattern occurs in the string. Use the `re.findall()` method.
    # **Input**: `count_pattern("The rain in Spain stays mainly in the plain", r'in')`
    # **Expected Output**: `4`

# solution
def count_pattern(input_string, pattern):
    find_match = re.findall(pattern, input_string)
    return len(find_match)

count = count_pattern("The rain in Spain stays mainly in the plain", r'in')
print(count)


print("\r")
# Exercise 6: Validate Phone Number
# Create a function `validate_phone` that checks whether a string is a valid phone number. The phone number format should be `(XXX) XXX-XXXX` where `X` is a digit from `0-9`.
    # **Input**: `"(123) 456-7890"`
    # **Expected Output**: `True`
    # **Input**: `"123-456-7890"`
    # **Expected Output**: `False`

# solution
def validate_phone(phone_number):
    search_result = re.search("^\(.+\)\s[0-9]{3}-[0-9]{4}", phone_number)
    if search_result:
        return True
    else:
        return False

validate1 = validate_phone("(123) 456-7890")
validate2 = validate_phone("123-456-7890")
print(validate1)
print(validate2)
# alternative solution
# def validate_phone(phone_number):
#     search_result = re.search(r"^\(\d{3}\) \d{3}-\d{4}$", phone_number)
#     return bool(search_result)


print("\r")
### Exercise 7: Redact Sensitive Information
# Write a function `redact_info` that takes a string and replaces all occurrences of email addresses and phone numbers (in the format `XXX-XXX-XXXX` or `(XXX) XXX-XXXX`) with `"REDACTED"`.
    # **Input**: `"Contact me at test.email@domain.com or (123) 456-7890"`
    # **Expected Output**: `"Contact me at REDACTED or REDACTED"`

# solution
def redact_info(input_str):
    sub_result = re.sub("\(.+\)\s[0-9]{3}-[0-9]{4}", "REDACTED", input_str)
    final_result = re.sub("\w*\.*\w*\@.+.com|.org", "REDACTED", sub_result)
    return final_result

result = redact_info("Contact me at test.email@domain.com or (123) 456-7890")
print(result)
# alternative solution
# def redact_info(input_str):
#     sub_result = re.sub(r"\(\d{3}\) \d{3}-\d{4}", "REDACTED", input_str)
#     final_result = re.sub(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org)", "REDACTED", sub_result)
#     return final_result