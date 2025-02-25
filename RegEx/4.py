import re

pattern = r"^[A-Z]{1}+[a-z]+$"

string = input()
if re.fullmatch(pattern, string):
    print("Matched")
else:
    print("Not matched")