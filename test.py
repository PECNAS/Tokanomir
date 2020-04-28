import datetime

database = open("database.txt", "r")
array = [i for i in database.readlines()]
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


if __name__ == "__main__":
	insert()
	val = str(input("Введите значение, по которому хотите найти больных: ")) # принимаем значение от пользователя
	separator = val.find(",") # задаём переменной разделитель
	space = separator + 2 # задаём переменной значение разделителя плюс один, что бы не брать в учёт запятую
	first_arg, second_arg = val[:separator], val[space:] # тут в действие идёт магия питона

	print(second_arg)

	if val[separator + 1] == " ": # если после запятой стоит пробел
		space = separator + 2 # мы задаём перменной значение разделителя плюс два, что бы не брать запятую с пробелом

	for an in animals: # проходим по списку
		if (first_arg in an['name']) or (first_arg in an['type']) or (first_arg in an['diseases']) or (first_arg in an['vaccination']) or (first_arg in an['arrival_date']):
			if ((second_arg in an['name']) or (second_arg in an['type']) or (second_arg in an['diseases']) or (second_arg in an['vaccination']) or (second_arg in an['arrival_date'])):
			# print(f"\033[{color_set(animals.index(an))}m" + 
				print(an['name'] + ", ", an['type'] + ", ", an['diseases'] + ", ", an['vaccination'] + ", ", an['arrival_date'])# + # вывод с расцветкой
			# "\033[0m")