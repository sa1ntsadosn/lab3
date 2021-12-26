def CheckSenquence(senquence):
	if(len(senquence)<3):
		return False
	else:
		for i in range(2,len(senquence)):
			if(senquence[i-2]-senquence[i-1]!=senquence[i-1]-senquence[i]):
				return False
	return True

senquence = [int(i) for i in input('Введите числовую последовательность\n').split()]
if(CheckSenquence(senquence)):
	print("Шаг прогрессии:\t" + str(senquence[1]-senquence[0]))
else:
	print("Ошибка")