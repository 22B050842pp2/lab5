import re

camelCase = input()

snake_case = re.sub(r"([A-Z])", r"_\1", camelCase).lower()
print(snake_case)