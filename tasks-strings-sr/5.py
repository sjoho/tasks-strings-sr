N = int(input())
advices = []
for _ in range(N):
    advice = input()
    advices.append(advice)
for advice in advices:
    if advice[:3].lower() == 'не ':
        print(advice[3:])
    else:
        print(advice)
