import sys
try:
    name = ' '.join(sys.argv[1:])
except IndexError:
    pass
if name == "":
    name = "World"
print(f'Hello, {name}!')
