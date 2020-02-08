tc = int(input())
while tc>0:
    x,y=map(str,input().split())
    #x= list(x)
    #y= list(y)
    z=str(int(x[::-1])+int(y[::-1]))
    print(int(z[::-1]))
    tc-=1


'''
def reverse_number(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n /= 10
    return r

print(reverse_number(123))
'''