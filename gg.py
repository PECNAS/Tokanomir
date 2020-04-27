'''
Данная программа анализирует ТЕКСТОВУЮ базу данных с больными
Больные имеют пять параметров:
имя, класс, симптом, наличие прививки и дата поступления
Просто гусь
+-------------------------------------------------+
|						░░░░░▄▀▀▀▄░░░░░░░░░		  |
|						▄███▀░◐░░░▌░░░░░░░		  |
|						░░░░▌░░░░░▐░░░░░░░		  |
|						░░░░▐░░░░░▐░░░░░░░		  |
|						░░░░▌░░░░░▐▄▄░░░░░		  |
|						░░░░▌░░░░▄▀▒▒▀▀▀▀▄		  |
|						░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄	  |
|						░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄	  |
|						░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄  |
|						░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀ |
|						░░░░░░░░░░░▌▌░▌▌░░░░░	  |
|						░░░░░░░░░░░▌▌░▌▌░░░░░	  |
|						░░░░░░░░░▄▄▌▌▄▌▌░░░░░	  |
+-------------------------------------------------+

Выполненные бонусы:
—При запуске с аргументом -color заболевшие с прививкой выводятся зелёным цветом, без прививки — красным
—В самом начале программы создаётся новая база данных, с только ДЕЙСТВИТЕЛЬНЫМИ датами. Программа работает с новой базой данных

Добавлено:
—Отключение и включение расцветки в меню
—Поиск больных по двум параметрам(третий метод поиска)

Исправить:
—Коментарии	                                                                   <<<ИСПРАВЛЕНО>>>
—Добавить help. ОБЯЗАТЕЛЬНО!                                                   <<<ИСПРАВЛЕНО>>>
—Исправить olor                                                                <<<ИСПРАВЛЕНО>>>
—Убрать тестовый файл при заливе...
—Переделать под словарь(картинка dictionary_for_animals.png)
—Сделать метод split(";") для строк 80-85
—Исправить действительность дат                                                
—Поменять termcolor на Escape выражение '/033[32mТЕКСТЕКСТЕКСТ[0m' для цвета   <<<ИСПРАВЛЕНО>>>
—

'''
import sys
import argparse
import datetime

from information.help import get_help
from termcolor import colored

color    = False
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

def color_set(index): # функция определения цвета
		if args.color == True:
			if vaccination[index].lower() == "да": #  если в массиве в срезе содержится да
				return 33 # то возвращаем зелёный цвет
			else: # если в массиве в срезе содержится нет
				return 31 # то возвращаем красный цвет
		else: # если аргумент -color не указан
			return 0 # то ставим белый цвет


def first(): # первый метод поиска 
	def print_value(conclusion, val):
		if conclusion.lower() == "имя":
			print(f"\033[{color_set(val)}m{names[val].capitalize()}\033[0m") # вывожу имена и сортирую их атрибутом end="\t"
		elif conclusion.lower() == "класс":
			print(f"\033[{color_set(val)}m{types[val].capitalize()}\033[0m") # то же самое, что и в прошлый раз
		elif conclusion.lower() in variations_diseases:
			print(f"\033[{color_set(val)}m{diseases[val].capitalize()}\033[0m") # то же самое, что и в прошлый раз
		elif conclusion.lower() in positive_vaccination:
			print(f"\033[{color_set(val)}m{vaccination[val].capitalize()}\033[0m") # то же самое, что и в прошлый раз
		elif conclusion.lower() == "дата":
			print(f"\033[{color_set(val)}m{arrival_date[val].capitalize()}\033[0m") # то же самое, что и в прошлый раз
		elif conclusion.lower() == "другой": # проверка для выбора другого номера
			ask_first() # вызываем функцию
		elif conclusion.lower() == "стоп": # проверяем на остановку
			sys.exit() # заканчиваем исполнение прогрммы
		elif conclusion.lower() == "всё": # проверяем на вывод всех показателей
			print(f"\033[{color_set(val)}m{array[val].replace(';', ', ').capitalize()}\033[0m") # выводим все показатели с заменой точки с зпаятой на запятую
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
						if 0 <= val <= (len(names) - 1): # если номер больного введён правильно
							conclusion = input("Введите параметр: ") # то спрашиваем желаемый параметр у пользователя
							print_value(conclusion, val) # вызываем функцию
						else: # если значение введено неверно
							print("В нашей базе данных нет больного с таким номером!\nВсего заболевших " + str(len(names) - 1)) # выводим максимум больных и сообщение об ошибке
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
	def find_all_with_parametr(val): # функция вывода всех совпадающих значение
		count = 0 # создаём переменную счёта

		for i in range(len(array)): # циклом пробегаемся по массиву столько раз, какова длина массива
			if val in array[i]: # если введенное значение имеется в строке массива
				print(f"\033[{color_set(i)}m{str(i) + ') ' + array[i].replace(';', ', ').capitalize()}\033[0m") # вывести строку и заменить все точки с запятой на запятый
				count += 1

		print("Всего насчитано " + str(count) + " больных с такими показателями")
		ask_second() # вызываем функцию снова

	def ask_second():
		val = str(input("Введите значение, по которому хотите найти больных: ")) # принимаем значение от пользователя
		if (val in names) or (val in types) or (val in diseases) or (val in vaccination) or (val in arrival_date): # проверка на то, есть ли данное значение в массивах
			if val.lower()[0] in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890.": # если запрос не содержит лишние символы
				find_all_with_parametr(val) # тогда вызываем функцию
			else: 
				print("Введённые вами данные не существуют!\n") # Выдаём сообщение об ошибке
				find_all_with_parametr(val) # заново вызываем функцию
		elif val.lower() in positive_vaccination:
			find_all_with_parametr("Да")
		elif val.lower() in negative_vaccination:
			find_all_with_parametr("Нет")
		elif val.lower() == "стоп":
			sys.exit()
		elif val.lower() == "методы":
			choice()
		else: # если значения в массиве нет
			print("Извините, введённое вами значение не найдено ни в одном списке\nВыберите другое значение") # выдаём сообщение об ошибке
			ask_second() # заново вызываем функцию

	ask_second() # запуск

def third():
	def check_with_two_parametrs(first_arg, second_arg):
		count = 0
		for c in array:
			if first_arg in c and second_arg in c:
				print(f'\033[{color_set(array.index(c))}m{c.replace(";", ", ")}\033[0m')
				count += 1

		print("Всего насчитано " + str(count) + " больных с такими показателями")
		ask_third()

	def ask_third():
		val = str(input("Введите значение, по которому хотите найти больных: ")) # принимаем значение от пользователя
		separator = val.find(",") # задаём переменной разделитель
		space = separator + 1 # задаём переменной значение разделителя плюс один, что бы не брать в учёт запятую

		if val[separator + 1] == " ": # если после запятой стоит пробел
			space = separator + 2 # мы задаём перменной значение разделителя плюс два, что бы не брать запятую с пробелом

		first_arg, second_arg = val[:separator], val[space:] # тут в действие идёт магия питона
		if (first_arg in names) or (first_arg in types) or (first_arg in diseases) or (first_arg in vaccination) or (first_arg in arrival_date): # проверка на то, есть ли первое значение в массивах
			if (second_arg in names) or (second_arg in types) or (second_arg in diseases) or (second_arg in vaccination) or (second_arg in arrival_date): # проверка на то, есть ли первое значение в массивах
				if val.lower()[0] in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890.": # если запрос не содержит лишние символы
					check_with_two_parametrs(first_arg, second_arg) # тогда вызываем функцию
				elif first_arg == "" or second_arg == "": # если один из один из параметров пойска был пустой
					print("Вы обязательно должны ввести оба значения") # выводим сообщение об ошибке
					ask_third() # заново вызываем функцию вопросы
				else: 
					print("Введённые вами данные не существуют!\n") # Выдаём сообщение об ошибке
					ask_third() # заново вызываем функцию

			elif second_arg.lower() in positive_vaccination: # тут мы облегчаем синтаксис
				check_with_two_parametrs(first_arg, "Да") # тут мы облегчаем синтаксис 
			elif second_arg.lower() in negative_vaccination:# тут мы облегчаем синтаксис 
				check_with_two_parametrs(first_arg, "Нет")# тут мы облегчаем синтаксис 
			else:  
				print("Второе введённое значение не найдено!\nВыберите другое значение") # выводим сообщение об ошибке
				ask_third() # вызываем функцию выбора снова

		elif first_arg == "" or second_arg == "": # если один из аргументов пустой 
			print("Вы обязательно должны ввести оба значения") # выводим сообщение об ошибке
			ask_third() # вызываем функцию выбора снова
		elif first_arg.lower() in positive_vaccination: # тут мы облегчаем синтаксис
			check_with_two_parametrs("Да", second_arg) # тут мы облегчаем синтаксис
		elif first_arg.lower() in negative_vaccination: # тут мы облегчаем синтаксис
			check_with_two_parametrs("Нет", second_arg) # тут мы облегчаем синтаксис
		elif val.lower() == "стоп": # проверяем на остановку программы
			sys.exit() # завершаем программу
		elif val.lower() == "методы": # проверяем на смену метода поиска
			choice() # вызываем функцию поиска
		else: # если значения в массиве нет
			print("Первое введённое значение не найдено\nВыберите другое значение") # выдаём сообщение об ошибке
			ask_third() # заново вызываем функцию

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
		global color
		color = False
		print("Расцветка выключена")
		choice()
	elif select.lower() == "включить расцветку":
		color = True
		print("Расцветка включена")
		choice()
	else: 
		print("Функции с такиим номером не существует!\nВведите 'первая', 'вторая' или 'стоп'.\nДля отключения расцветки пропишите 'отключить расцветку'\nДля включения подсветки" +
			" пропишите 'включить расцветку'") # выввести сообщение об ошибке
		choice() # заново вызываем функцию

insert()# запуск программы, входная точка
choice() # функция выбора методов поиска