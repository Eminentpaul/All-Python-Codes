x = [0, 1, 22]
y = ' '.join(map(str, x)).split()
# z = int(y)
print(sum(int(i) for i in y))