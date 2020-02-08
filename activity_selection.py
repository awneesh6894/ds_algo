'''for _ in range(int(input())):
    n=int(input())
    st=list(map(int,input().split()))
    fi=list(map(int,input().split()))
    f=list(zip(st,fi))
    #print(f)
    f.sort(key=lambda x:x[1])
    #print(f)
    j=0
    cnt=1
    for i in range(1,len(f)):
        #print(f[i][0],f[j][1])
        if f[i][0] >= f[j][1]:
            j=i
            cnt +=1
    print(cnt)'''

for _ in range(int(input())):
    n=int(input())
    st=list(map(int,input().split()))
    fi=list(map(int,input().split()))
    f=list(zip(st,fi))
    f.sort(key=lambda x:x[1])
    j=0
    cnt=1
    arr=[]
    arr.append(st.index(f[0][0])+1)
    for i in range(1,len(f)):
        if f[i][0] >= f[j][1]:
            j=i
            arr.append(st.index(f[i][0])+1)
    for i in arr:
        print(i,end=" ")