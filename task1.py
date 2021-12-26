import random
n = int(input('Введите кол-во элементов массива:'))
array = []
array1 = []
count = 0
for i in range(n):
    array.append(random.randint(-30, 45))
    count = count + 1
    n = n - 1
    if count == 10:
        print(array)
        array1 += array
        array = []
        count = count - 10
if count < 10:
    array1 += array
    print(array)
array = array1
array = [i for i in array if i >= 0]
array.reverse()
print('Вывод массива в обратном порядке без отрицательных чисел: {}'.format(array))