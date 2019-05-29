
def maxsum(l,strt,end):
    if strt>end:
        return 0
    take = l[strt] + maxsum(l,strt + 2,end);
    skip = maxsum(l,strt + 1,end);

    # return max(l[strt] + maxsum(l,strt + 2,end),maxsum(l,strt + 1,end));

        # maxsum(l,max1,n+l[strt],strt+2,end)
    return max(take,skip)











l = [-12, 9, 7, 33]
max1=[-9999999999]
n=0
print(maxsum(l,0,len(l)-1))
