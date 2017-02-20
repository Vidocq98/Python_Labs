#Напишите программу, позволяющую ввести с клавиатуры
#текст предложения и вывести на консоль все символы,
#которые входят в этот текст ровно по одному разу.

#text = "Дайте мне одну минуту"
text=input()
def count_char (text):
    low_text = text.lower()
    char = list(low_text)
    for i in range (len(char)):
        if char.count(char[i]) == 1:
            print(char[i], end = ' ')
count_char(text)
