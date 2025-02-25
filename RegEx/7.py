import re

snake_case = input()

camelCase = re.sub(r"_([a-zA-Z])", lambda match: match.group(1).upper(), snake_case)
print(camelCase)