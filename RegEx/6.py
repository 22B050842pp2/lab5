import re
def replace_to_colon(string):
    return re.sub(r"[ ,.]", ":", string)

str = replace_to_colon(input())
print(str)
