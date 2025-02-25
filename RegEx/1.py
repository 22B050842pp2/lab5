import re

pattern = r"ab*"

string = input()
if re.fullmatch(pattern, string):
    print("Matched")
else:
    print("Not matched")