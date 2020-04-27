import datetime

database = open("database.txt", "r")
array    = [i for i in database.readlines()]
animals  = []

positive_vaccination = ["имеют прививку", "с прививкой", # здесь я создаю массив для слов, вариаций которых может быть множество
						"вакцинированы", "наличие прививки", "прививка"]

negative_vaccination = ["без прививки", "не имеют прививки", # здесь я создаю массив для слов, вариаций которых может быть множество
						"не вакцинированы"]

variations_diseases  = ["симптом", "болезнь", "диагноз"]
exceptions = []

def insert():
	iterat = 0
	for _ in range(len(array)):
		animals_inform = array[_].split(";")
		day, month, year = array[_][array[_].rfind(";") + 1:-1].split(".")	
		time_now = datetime.datetime.now()
		try: # ищем февральские дни
			data = datetime.datetime(int(year), int(month), int(day)) # в переменную дата записываем дату больного
			if data <= time_now: # если дата действительная
				name = animals_inform[0]
				typ = animals_inform[1]
				diseases = animals_inform[2]
				vaccination = animals_inform[3]
				arrival_date = animals_inform[4][:-1]
				animals.append({'name' : name, 'type' : typ, 'diseases' : diseases, 'vaccination' : vaccination, 'arrival_date' : arrival_date, })
			elif data > time_now: # если дата недействительная
				pass
		except ValueError: # Если нашли неверный дни в феврале
			exceptions.append(_)
		

insert()

if __name__ == "__main__":
	val = input("Значение >>> ")
	for i in range(len(animals)):
		if val in animals[i]['name']:
			print(animals[i])