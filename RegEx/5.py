import re

pattern = r"^a.b$"

string = input()
if re.fullmatch(pattern, string):
    print("Matched")
else:
    print("Not matched")