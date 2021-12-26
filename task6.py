def sumItteractive(x):
    result = 0
    for i in range(len(x)):
        result+=x[i]
    return result
def sumRecursive(x):
    if(len(x)==0):
        return 0
    return x[0]+sumRecursive(x[1:])
def minItteractive(x):
    min = x[0]
    for i in range(1,len(x)):
        if(min>x[i]):
            min = x[i]
    return min
def minRecursive(x, min):
    if(len(x)==0):
        return min
    if(min>x[0]):
        min = x[0]
    return  minRecursive(x[1:], min)
list = [1,2,3,4,5,6,7,8,9,10]
print(sumItteractive(list))
print(sumRecursive(list))
print(minItteractive(list))
print(minRecursive(list, list[0]))