import re

pattern = r"^[a-z]+(_[a-z]+)*$"

string = input()
if re.fullmatch(pattern, string):
    print("Matched")
else:
    print("Not matched")