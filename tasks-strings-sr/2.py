s = input()
for i in s:
    if not(i.islower() or i.isdigit() or i=='_'):
        print('Неверный символ:', i)
        break
else:
    print('OK')
