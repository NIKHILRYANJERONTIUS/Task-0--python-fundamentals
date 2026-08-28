n=int(input("enter no of integers:"))
l=[];revl=[];ecount=0;ocount=0;s=0
for x in range(n):
    val=int(input("enter no:"))
    l.append(val)
for x in range(len(l)-1,-1,-1):
    revl.append(l[x])
Min=l[0];Max=l[0]
for x in l:
    s+=x
    if x%2==0:
        ecount+=1
    else:
        ocount+=1
    if x<Min:
        Min=x
    elif x>Max:
        Max=x
    else:
        continue
print("Largest:",Max)
print("Smallest:",Min)
print("Sum:",s)
print("Even Count:",ecount)
print("Odd Count:",ocount)
print("Reversed:",revl)
