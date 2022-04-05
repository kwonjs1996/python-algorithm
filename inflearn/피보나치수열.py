user_in = int(input())

x = [0,1]
y = []

if user_in < 2:
    print(x[0])
elif user_in <3:
    print(x[0], x[1])
else:
    for i in range(2,user_in):
        y = x[-1] + x[-2]
        x.append(y)

print(x)