import re

snake_case = input()

camelCase = re.sub(r"(?<!^)([A-Z])", r" \1", snake_case)
print(camelCase)