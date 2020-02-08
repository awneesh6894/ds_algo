'''
array = {0:0,1:1}

def solve(n):
    if n in array:
        return array[n] #retruns the value of the key if found in array
    else:
        array[n] = max(n,solve(n//2)+solve(n//3)+solve(n//4))
        return array[n]

if __name__ == '__main__':
    # taking the input
    i = 10
    while(i > 0):
        n = int(input())
        print(solve(n))
        i -= 1
'''

d={0:0}
def exchange(n):
    if n in d:
        return d[n]
    else:
        d[n]=max(n,(exchange(n//4)+exchange(n//3)+exchange(n//2)))
        return d[n]
while True:
    try:
        print(exchange(int(input())))
    except:
        break