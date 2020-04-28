'''
Данная программа анализирует ТЕКСТОВУЮ базу данных с больными
Больные имеют пять параметров:
имя, класс, симптом, наличие прививки и дата поступления

Выполненные бонусы:
—При запуске с аргументом --color заболевшие с прививкой выводятся зелёным цветом, без прививки — красным
—Запуск с аргументом --help выводит информационное письмо

Добавлено:
—Отключение и включение расцветки в меню
—Поиск больных по двум параметрам(третий метод поиска)

Исправить:
—Коментарии	                                                                   <<<ИСПРАВЛЕНО>>>
—Добавить help. ОБЯЗАТЕЛЬНО!                                                   <<<ИСПРАВЛЕНО>>>
—Исправить olor                                                                <<<ИСПРАВЛЕНО>>>
—Убрать тестовый файл при заливе...                                            <<<ИСПРАВЛЕНО>>>
—Переделать под словарь                                                        <<<ИСПРАВЛЕНО>>>
—Сделать метод split(";")                                                      <<<ИСПРАВЛЕНО>>>
—Исправить действительность дат                                                <<<ИСПРАВЛЕНО>>>
—Поменять termcolor на Escape выражение '/033[32mТЕКСТЕКСТЕКСТ[0m' для цвета   <<<ИСПРАВЛЕНО>>>

'''
import sys
import argparse
import datetime
import re

from information.help import get_help

parser   = argparse.ArgumentParser() #создаём образ парсера
parser.add_argument('-c', '--color', action="store_true") # добавляем необязательный аргумент
parser.add_argument('-gh', '--get_help', action="store_true") # добавляем необязательный аргумент
args     = parser.parse_args()

if args.color == "--color": # проверяем аргумент
	color = True
elif args.get_help == True:
	get_help()

print("Идёт сканирование базы данных, это может занять некоторое время")

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

def color_set(index): # функция определения цвета
		if args.color == True:
			if animals[index]['vaccination'].lower() == "да": #  если в массиве в срезе содержится да
				return 33 # то возвращаем зелёный цвет
			else: # если в массиве в срезе содержится нет
				return 31 # то возвращаем красный цвет
		else: # если аргумент -color не указан
			return 0 # то ставим белый цвет


def first(): # первый метод поиска 
	def print_value(conclusion, val):
		if conclusion.lower() == "имя":
			print(f"\033[{color_set(val)}m{animals[val]['name'].capitalize()}\033[0m") # вывожу имена и сортирую их атрибутом end="\t"
		elif conclusion.lower() == "класс":
			print(f"\033[{color_set(val)}m{animals[val]['type'].capitalize()}\033[0m") # то же самое, что и в прошлый раз
		elif conclusion.lower() in variations_diseases:
			print(f"\033[{color_set(val)}m{animals[val]['diseases'].capitalize()}\033[0m") # то же самое, что и в прошлый раз
		elif conclusion.lower() in positive_vaccination:
			print(f"\033[{color_set(val)}m{animals[val]['vaccination'].capitalize()}\033[0m") # то же самое, что и в прошлый раз
		elif conclusion.lower() == "дата":
			print(f"\033[{color_set(val)}m{animals[val]['arrival_date'].capitalize()}\033[0m") # то же самое, что и в прошлый раз
		elif conclusion.lower() == "другой": # проверка для выбора другого номера
			ask_first() # вызываем функцию
		elif conclusion.lower() == "стоп": # проверяем на остановку
			sys.exit() # заканчиваем исполнение прогрммы
		elif conclusion.lower() == "всё": # проверяем на вывод всех показателей
			print(f"\033[{color_set(val)}m{animals[val]['name']}, {animals[val]['type']}, {animals[val]['diseases']}, " +  
			f"{animals[val]['vaccination']}, {animals[val]['arrival_date']}\033[0m") # выводим все показатели с заменой точки с зпаятой на запятую
		elif conclusion.lower() == "методы": # вызываем стартовое меню для смены методы поиска
			choice() # вызываем функцию
		else:
			print("Введён неверный параметр!\nПожалуйста введите параметр из существующих.\n'Имя', 'класс', 'симптом', 'наличие прививки', 'дата'\nВв" +
				"едите слово 'стоп', для остановки\nДля смены больного введите 'Другой'\nТак же можете использовать комманду 'всё' для вывода " +
				"всей информации о больном\nКоммманда 'методы' позволит сменить метод поиска больных ") # это сообщение об ошибке

	def ask_first():
		val = input("Введите номер больного: ")
		if val != "":
			if val[0] in "0123456789": #если номер больного это цифра
				try: # начинаем ловить исключения
					val = int(val) # переменной val ставим тип integer
					while True: # бесконечный цикл 
						if 0 <= val <= (len(animals) - 1): # если номер больного введён правильно
							conclusion = input("Введите параметр: ") # то спрашиваем желаемый параметр у пользователя
							print_value(conclusion, val) # вызываем функцию
						else: # если значение введено неверно
							print("В нашей базе данных нет больного с таким номером!\nВсего заболевших " + str(len(animals) - 1)) # выводим максимум больных и сообщение об ошибке
							ask_first() # вызываем функцию заново
				except ValueError: # если поймали исключение о вводе строки
					print("Введён неверный тип данных") # то выводим сообщение об ошибке
					ask_first()	 # и вызываем функцию заново
			elif val == "стоп": # однако если val равен стоп
				sys.exit() # останавливаем программу
			elif val.lower() == "методы":
				choice()
			else: 
				print("Вы ввели неверный тип данных, нужно ввести нумерацию больного!\n") # Выдаём сообщение об ошибке
				ask_first() # заново вызываем функцию
		else:
			print("Это поле является обязательным для ввода!")
			ask_first()

	ask_first() # запускаем функцию

def second(): # второй метод поиска
	def print_value(parametr):
		count = 0
		val = parametr
		for an in animals: # проходим по списку
			if ((val in an['name']) or (val in an['type']) or (val in an['diseases']) or (val in an['vaccination']) or (val in an['arrival_date'])): # проверка на то, есть ли значение в списке
				print(f"\033[{color_set(animals.index(an))}m" + 
					an['name'] + ", ", an['type'] + ", ", an['diseases'] + ", ", an['vaccination'] + ", ", an['arrival_date'] + # вывод с расцветкой
					"\033[0m")
				count += 1
			elif val.lower() == "методы": # смена метода поиска
				choice()
			elif val.lower() == "стоп": # остановка программы
				sys.exit()
			else: 
				print("Такого значения нет в базе данных")
				ask_second()

		ask_second()

	def ask_second():
		val = input("Введите параметр: ")
		count = 0
		regex_result = re.search(r"[а-яА-Я0-9.]", val)
		if regex_result:
			if val.lower() in positive_vaccination: # упрощаем синтаксис запроса
				print_value("Да")
			elif val.lower() in negative_vaccination: # упрощаем синтаксис запроса
				print_value("Нет")
			elif val.lower() not in positive_vaccination and val not in negative_vaccination: # упрощаем синтаксис запроса
				print_value(val)
		else:
			print("Вы ввели неверный тип данных!")
			ask_second()

	ask_second()

def third():
	def check_with_two_parametrs(first_arg, second_arg):
		count = 0
		for an in animals: # проходим по списку
			if (first_arg in an['name']) or (first_arg in an['type']) or (first_arg in an['diseases']) or (first_arg in an['vaccination']) or (first_arg in an['arrival_date']):
				if ((second_arg in an['name']) or (second_arg in an['type']) or (second_arg in an['diseases']) or (second_arg in an['vaccination']) or (second_arg in an['arrival_date'])):
					print(f"\033[{color_set(animals.index(an))}m" + 
						an['name'] + ", ", an['type'] + ", ", an['diseases'] + ", ", an['vaccination'] + ", ", an['arrival_date'] + # вывод с расцветкой
						"\033[0m")
					count += 1
		if count == 0:
			print("В базе данных нет больных с такими параметрами")
			ask_third()
		else:
			print("Всего насчитано " + str(count) + " больных с такими показателями")
			ask_third()

	def ask_third():
		val = str(input("Введите значение, по которому хотите найти больных: ")) # принимаем значение от пользователя
		separator = val.find(",") # задаём переменной разделитель
		space = separator + 2 # задаём переменной значение разделителя плюс один, что бы не брать в учёт запятую
		first_arg, second_arg = val[:separator], val[space:] # тут в действие идёт магия питона
		if first_arg == second_arg:
			print("Для поиска одного значения используйте первую функцию")

		if val[separator + 1] == " ": # если после запятой стоит пробел
			space = separator + 2 # мы задаём перменной значение разделителя плюс два, что бы не брать запятую с пробелом

		if val.lower() == "методы": # смена метода поиска
			choice()
		elif val.lower() == "стоп": # остановка программы
			sys.exit()
		else:
			if first_arg.lower() in positive_vaccination: # упрощаем синтаксис запроса
				check_with_two_parametrs("Да", second_arg)
			elif first_arg.lower() in negative_vaccination: # упрощаем синтаксис запроса
				check_with_two_parametrs("Нет", second_arg)
			elif second_arg.lower() in positive_vaccination: # упрощаем синтаксис запроса
				check_with_two_parametrs(first_arg, "Да")
			elif second_arg.lower() in negative_vaccination: # упрощаем синтаксис запроса
				check_with_two_parametrs(first_arg, "Нет")
			else:
				check_with_two_parametrs(first_arg, second_arg)

	ask_third()

def choice(): # функция выбора методов поиска
	select = input("Какую функцию поиска запустить(первая, вторая, третья)?\n") # спрашиваем пользователя
	if select.lower() == "первая": # если первый метод, то вызываем функцию первого метода
		first()
	elif select.lower() == "вторая": # то же самое
		second()
	elif select.lower() == "третья":
		print("Введите два значения через запятую")
		third()
	elif select.lower() == "стоп": # то же самое
		sys.exit()
	elif select.lower() == "отключить расцветку":
		args.color = False
		print("Расцветка выключена")
		choice()
	elif select.lower() == "включить расцветку":
		args.color = True
		print("Расцветка включена")
		choice()
	else: 
		print("Функции с такиим номером не существует!\nВведите 'первая', 'вторая' или 'стоп'.\nДля отключения расцветки пропишите 'отключить расцветку'\nДля включения подсветки" +
			" пропишите 'включить расцветку'") # выввести сообщение об ошибке
		choice() # заново вызываем функцию

insert()# запуск программы, входная точка
choice() # функция выбора методов поиска