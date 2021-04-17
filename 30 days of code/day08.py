n = int(input())
phonebook = {}

for i in range(n):
    name, number = map(str, input().split())
    name, num = [str(name), int(number)]
    phonebook[name] = number


while True:
    try:
        query = str(input())

        if query in phonebook:
            print(f'{query}={phonebook[query]}')
        else:
            print('Not found')
    except EOFError:
        break
