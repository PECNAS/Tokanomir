import datetime

database = open("database.txt", "r")
array = [i for i in database.readlines()]

names        = [] # здесь я создаю массив для имен
types        = [] # здесь я создаю массив для типа
diseases     = [] # здесь я создаю массив для симптома
vaccination  = [] # здесь я создаю массив для вакцинирования
arrival_date = [] # здесь я создаю массив для даты поступления
exceptions   = [] # здесь я создаю массив для исключений. Тут будут находится индексы тех больных, дата которых недействительная

positive_vaccination = ["имеют прививку", "с прививкой", # здесь я создаю массив для слов, вариаций которых может быть множество
						"вакцинированы", "наличие прививки", "прививка"]

negative_vaccination = ["без прививки", "не имеют прививки", # здесь я создаю массив для слов, вариаций которых может быть множество
						"не вакцинированы"]

variations_diseases  = ["симптом", "болезнь", "диагноз"]

def insert():
	for _ in range(len(array)):
		animals_inform = array[_].split(";")
		day, month, year = array[_][array[_].rfind(";") + 1:-1].split(".")	
		time_now = datetime.datetime.now()
		try: # ищем февральские дни
			data = datetime.datetime(int(year), int(month), int(day)) # в переменную дата записываем дату больного
			if data <= time_now: # если дата действительная
				names.append(animals_inform[0])
				types.append(animals_inform[1])
				diseases.append(animals_inform[2])
				vaccination.append(animals_inform[3])
				arrival_date.append(animals_inform[4].strip())
			elif data > time_now: # если дата недействительная
				exceptions.append(_) # добавляем индекс в массив с исключениями
				print(array[_])
		except ValueError: # Если нашли неверный дни в феврале
			exceptions.append(_) # добавляем индекс в массив с исключениями
			print(array[_])

insert()