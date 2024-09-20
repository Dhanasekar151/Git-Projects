import re

# pattern to match
pattern = r"regex"

# string to search
string = "regex is a sequence of characters that forms a search pattern."

# find the first match
match = re.search(pattern, string)

# print the match
print("Match:", match.group())
