#Напишите скрипт, который на основе списка из 16 названий
#футбольных команд случайным образом формирует 4 группы по 4
#команды, а также выводит на консоль календарь всех игр (игры
#должны проходить по средам, раз в 2 недели, начиная с 14 сентября
#текущего года). Даты игр необходимо выводить в формате «14/09/2016,
#22:45». Используйте модули random и itertools.
import random
import itertools
import datetime
n =random.randint(0,15)
twins=[]
print(n)
teams = ['Барселона','Реал Мадрид','Манчестер Юнайтед','Ювентус', 'Бавария', 'Галатасарай', 'Милан', 'Ливерпуль', 'Интер', 'Марсель', 'Фенербахче', 'Арсенал', 'Боруссия', 'Челси', 'Лион', 'Шааахтеер']
#random.shuffle(teams)
start = 0
end = 2
count=0
while end<=len(teams):
    twins += list(teams[start:end]) #Как наполнить твинс срезами?
    start+=2
    end+=2
    print(twins)
print(twins)
#разделяю на 4 блока, сплитом
date_game_start = datetime.datetime(2016, 9, 14, 22, 45)
i=0
while i < 8:
    date_game_next = datetime.timedelta(days=14)
    date_game = date_game_start+date_game_next
    date_game_start = date_game
    print(date_game.strftime("%d/%m/%Y, %H:%M"))
    i+=1
