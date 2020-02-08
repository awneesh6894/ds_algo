s="07:05:45PM"
if s[0:2]=="12" and s[8:10]=="PM":
        print(s[0:8])
elif s[8:10]=="PM":
    x=int(s[0:2])+12
    print(str(x)+s[2:8])
elif s[8:10]=="AM":
    print(s[0:8])