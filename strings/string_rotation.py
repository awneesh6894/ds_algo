def left_rotation(s2,y):
    l1=s2[0:y]
    l2=s2[y:]
    return l2+l1
def right_rotation(s2,y):
    r1=s2[len(s2)-y:]
    r2=s2[:len(s2)-y]
    return r1+r2

x=int(input())
for i in range(x):
    s1=input()
    s2=list(input())
    '''print(''.join(left_rotation(s2,2)))
    print(''.join(right_rotation(s2,2)))'''
    if ''.join(left_rotation(s2,2))==s1 or ''.join(right_rotation(s2,2))==s1:
        print(1)
    else:
        print(-1)

