#Program on Fabonechi Series
a=0
b=1
for n in range(21):
    b=a+b
    a=b-a
    print(b)
