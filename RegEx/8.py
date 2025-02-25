import re 

string = input()

list = re.split(r"(?=[A-Z])", string)
print(list)