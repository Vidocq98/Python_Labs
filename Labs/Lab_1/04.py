#Напишите скрипт, который разделяет введенный с клавиатуры текст на слова
#и выводит сначала те слова, длина которых превосходит 7 символов, затем
#слова размером от 4 до 7 символов, затем – все остальные.

#text = "Дайте мне еще одну минуту"

#To DO
#text = input()
text = '����� ������ ���� ��������'
more_7=[]
between_4and7=[]
less_4=[]
def script_split(text):
    word=text.split()
    for i in range (len(word)):
        if len(list(word[i]))>7:
            more_7.append(word[i])
        elif len(list(word[i]))>4 and len(list(word[i]))<7:
            between_4and7.append(word[i])
        else:
            less_4.append(word[i])
    print(more_7)
    print(between_4and7)
    print(less_4)
script_split(text)

