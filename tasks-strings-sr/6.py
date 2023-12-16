max_length = int(input())
n = int(input())

for i in range(n):
    title = input()
    if len(title) <= max_length:
        print(title)
    else:
        shortened_title = title[:max_length-3] + "..."
    print(shortened_title)
