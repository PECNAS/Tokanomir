import datetime

array = ['Джеси;единорог;бешенство;Нет;23.9.2015', 'Шарик;собака;падение с высоты;Нет;28.4.2020',
		'Михалыч;единорог;падение с высоты;Да;25.11.2019',
		'Михалыч;попугай;пьянство;Да;4.5.2020', 'Михалыч;сосед снизу;пьянство;Нет;2.1.2015']

names        = [] # здесь я создаю массив для имен
types        = [] # здесь я создаю массив для типа
diseases     = [] # здесь я создаю массив для симптома
vaccination  = [] # здесь я создаю массив для вакцинирования
arrival_date = [] # здесь я создаю массив для даты поступления
exceptions   = []

time_now = datetime.date.today() # получаем время сейчас
time_now = time_now.strftime("%d.%m.%Y").replace("/", ".").strip() # меняем местами год и день и убираем пробелы

for _ in array:
	animals_inform = _.split(";")
	if animals_inform[4].strip() <= time_now:
		names.append(animals_inform[0])
		types.append(animals_inform[1])
		diseases.append(animals_inform[2])
		vaccination.append(animals_inform[3])
		arrival_date.append(animals_inform[4].strip())
		print(_)
	else:
		exceptions.append(array.index(_))

# if __name__ == "__main__":
# 	for i in array:
# 		print(i)