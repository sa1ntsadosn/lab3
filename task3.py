k = int(input('введите кол-во шагов:'))
def shift(array, k):
    k = abs(k)
    for i in range(k):
        array.append(array.pop(0))
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(array)
shift(array, -k)
print(array)