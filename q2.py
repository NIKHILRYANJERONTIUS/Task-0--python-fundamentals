def process_list(numbers):
    newlist=numbers.copy()
    for x in numbers:
        if x<0:
            newlist.remove(x)
    newlist.append(0)
    newlist.sort()
    return newlist

original=eval(input("enter a list:"))
result=process_list(original)
print("original:",original)
print("result:",result)
