# ******************************************************************************* #
#                                                                             	  #
#     gen.py                                                     ♥           	  #
#                                                                 ¨/\_/\ ♥    	  #
#     By: zkerriga                                                 >^,^<     	  #
#                                                                   / \     	  #
#     Created: 2020-04-19 10:51:34 by zkerriga                     (___)__  	  #
#     Updated: 2020-04-19 11:21:08 by zkerriga                              	  #
#                                                                             	  #
# ******************************************************************************* #

import random

FILE = 'database.txt'

NAMES = [
			'Шарик', 'Барсик', 'Зевс', 'Барбос',
			'Вольт', 'Мурзик', 'Михалыч', 'Джеси',
			'Гермиона', 'Кеша'
		]
TYPES =  [
			'собака', 'кошка', 'попугай',
			'единорог', 'сосед снизу'
		 ]
ILLS = 	[
			'бешенство', 'укусы', 'падение с высоты', 'пьянство'
		]

DATA_VOLUME = 14820

print('Start the generator.')
with open(FILE, 'a') as filee:
	for i in range(DATA_VOLUME):
		_name = random.choice(NAMES)
		_type = random.choice(TYPES)
		_ill = random.choice(ILLS)
		_vactin = random.choice(['Да', 'Нет'])
		_data = str(random.randint(1, 30)) + '.' + str(random.randint(1, 12)) + '.' + str(random.randint(2015, 2020))
		result = ';'.join((_name, _type, _ill, _vactin, _data))
		filee.write(result + '\n')
print('Success!')
print(i)