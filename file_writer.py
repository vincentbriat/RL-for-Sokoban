message = 'Hello World!'
filepath = 'test.txt'

with open(file=filepath, mode='w') as f:
    f.write(message)

print(f'"{message}" written in "{filepath}"')