import re

string = input()

text = re.sub(r"(?<!^)([A-Z])", r" \1", string)
print(text)
