n = int(input())
a = list(map(int, input().split()))
def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum
max= -2147000000
for x in a:
    tot=digit_sum(x)
    res=x
print(res)