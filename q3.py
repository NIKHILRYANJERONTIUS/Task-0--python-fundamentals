def is_prime(n):
    for x in range(2,n):
        if n%x==0:
            p=False
            break
    else:
        p=True
    return p
'''the else block associated with a for loop execute as done in above function is_prime(n)
only when the entriety of the code inside the for block runs perfectly wihtout any
break statement,return or error,then only the code inside the else block execute'''

n=int(input("enter a prime check number:"))
val=is_prime(n)
print("given number ",n,"to be prime is:",val)
for x in range(2,n+1):
    value=is_prime(x)
    if value==True:
        print(x,end=" ")
    
