x = 1534236469
y = list(reversed(str(x)))
z = ''

elif '-' in y:
    y.remove('-')
    for i in y:
        z += i
    answer = int(z)*(-1)
else:
    for i in y:
        z += i