def get_help():
	print('''
	Программа предназначена для помощи в ориентировке заболевших животных Токаномира.
	Так же принимает три аргумента:
		-gh/ --get_help # выводит на экран письмо помощи
		-c/--color # выставляет расцветку заболевшим
		-cd/--check_date # отключает проверку дат

	При выборе функции поиска можно поменять режим расцветки, используя команды
		'включить расцветку' или "отключить расцветку"

	Есть три функции поиска:
		Первая:
			Предназначена для просмотра параметров больного по его уникальному номеру
			Пример запроса: имя
			Пример ответа: Гермиона

			Есть уникальные команды:
				другой — выбор другого больного, работает только на этапе выбора параметра
				всё — вывод всех параметров, работает только на этапе выбора параметра

		Вторая:
			Предназначена для поиска всех больных по одному, общему параметру
			Пример запроса: Гермиона
			Пример ответа:
				5) Гермиона, сосед снизу, падение с высоты, нет, 3.8.2017
				12) Гермиона, собака, падение с высоты, да, 11.9.2019
			Выводится их уникальный номер, Имя, тип, симптом, наличие прививки и дата поступления

		Третья:
			Предназначена для поиска по двум параметрам.
			Пример запроса: Гермиона, с прививкой
			Пример ответа: 
				125) Гермиона, попугай, укусы, Да, 21.7.2018
				72) Гермиона, единорог, укусы, Да, 3.4.2019
			Выводится их уникальный номер, Имя, тип, симптом, наличие прививки и дата поступления

	Для всех функций поиска есть общие команды:
		стоп — останавливает работу программы
		методы — выполняет смену функции поиска

	В самом начале генерируется новая база данных, в которую записываются действительные даты
	Данную операцию можно отключить при запуске программы, прописав аргумент -cd/--check_date
	\033[31mCreated by Pecnas
	date: 26.04.2020\033[0m\n'''
)