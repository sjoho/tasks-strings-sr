n = int(input())
lines = []
for _ in range(n):
    lines.append(input())

for i, line in enumerate(lines):
    index = line.find("кот")
    if index != -1:
        print(i+1, index+1)
