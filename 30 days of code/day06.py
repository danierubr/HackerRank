# Enter your code here. Read input from STDIN. Print output to STDOUT
times = int(input())
for t in range(times):
    text = input()
    odds = ''
    evens = ''
    for i in range(len(text)):
        if i % 2 == 0:
            evens += text[i]
        else:
            odds += text[i]
    print(evens, odds)