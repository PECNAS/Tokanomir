import datetime

database = open('database.txt', 'r')
array = [i for i in database.readlines()]

names        = [] # здесь я создаю массив для имен
types        = [] # здесь я создаю массив для типа
diseases     = [] # здесь я создаю массив для симптома
vaccination  = [] # здесь я создаю массив для вакцинирования
arrival_date = [] # здесь я создаю массив для даты поступления
exceptions   = []

time_now = datetime.date.today() # получаем время сейчас
time_now = time_now.strftime("%d/%m/%Y").replace("/", ".").strip() # меняем местами год и день и убираем пробелы

for _ in array:

	animals_inform = _.split(";")
	if time_now <= animals_inform[4].strip():
		arrival_date.append(animals_inform[4].strip())
		names.append(animals_inform[0])
		types.append(animals_inform[1])
		diseases.append(animals_inform[2])
		vaccination.append(animals_inform[3])

database.close()

if __name__ == "__main__":
	for i in range(len(arrival_date)):
		print(names[i], types[i], diseases[i], vaccination[i], arrival_date[i])