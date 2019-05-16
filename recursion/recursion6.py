reverse sentence using recursion


def rev(s,i,j):
    if i > j-1:
        return
    rev(s,i+1,j-1)
    s[i],s[j] = s[j],s[i]


s = "i love word books"
s = s.split()
r = rev(s,0,len(s)-1)
print(s)
