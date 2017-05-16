#Напишите скрипт, который читает текстовый файл и
#выводит символы в порядке убывания частоты встречаемости
#в тексте. Регистр символа не имеет значения. Программа
#должна учитывать только буквенные символы (символы
#пунктуации, цифры и служебные символы слудет игнорировать).
#Проверьте работу скрипта на нескольких файлах с текстом на
#английском и русском языках, сравните результаты с таблицами,
#приведенными в wikipedia.org/wiki/Letter_frequencies.

filename = open('Harry_Potter_en.txt', 'r')
text = filename.read()
text = text.lower()
print(len(text))
english = 'abcdefghijklmnopqrstuvwxyz'
russian = '��������������������������������'
liters_count_ru = {russian[i]: text.count(russian[i]) for i in range(len(russian))}
liters_count_en = {english[i]: text.count(english[i]) for i in range(len(english))}
print( sorted(liters_count_ru.items(), key=lambda x: x[1], reverse=True) )
print( sorted(liters_count_en.items(), key=lambda x: x[1], reverse=True) )
