print('Введите номер числа в ряде Фиббоначи:')
a=int(input())
def f(a):
    if(a==0):
        return 1
    if(a==1):
        return 1
    else:
        return f(a-1)+f(a-2)
print('Число',f(a))