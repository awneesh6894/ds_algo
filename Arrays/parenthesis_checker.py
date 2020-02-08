t=int(input())
for _ in range(t):
    string=input()
    left=['{','[','(']
    right=['}',']',')']
    arr=[]
    balanced=True
    for i in string:
        if i in left:
            arr.append(i)
        else:
            try:
                if arr[-1]==left[right.index(i)]:
                    arr.pop()
                else:
                    balanced=False
            except:
                balanced=False
    if len(arr)==0 and balanced:
        print("balanced")
    else:
        print("not balanced")

