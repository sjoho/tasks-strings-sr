s1 = input()
s2 = input()

bulls = 0
cows = 0

for i in range(len(s1)):
    if s1[i] == s2[i]:
        bulls += 1
    elif s1[i] in s2:
        cows += 1

print(bulls, cows)
