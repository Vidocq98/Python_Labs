#Напишите скрипт, который обрабатывает список строк-адресов
#следующим образом: сначала определяет, начинается ли каждая
#строка в списке с префикса «www». Если условие выполняется,
#то скрипт должен вставить в начало этой строки префикс
#«http://», а затем проверить, что строка заканчивается на
#«.com». Если у строки другое окончание, то скрипт должен
#вставить в конец подстроку «.com». В итоге скрипт должен
#вывести на консоль новый список с измененными адресами.
#Используйте генераторы списков.

adress = ['www.google.ru','google.com','google.ru']
#adress = [c * 3 for c in 'list']
def change_adress (adress):
    for i in range (len(adress)):
        if adress[i].startswith('www.'):
            adress[i] = 'http://' + adress[i]
        if adress[i].endswith('.com')== False:
            adress[i] = adress[i] + '.com'
        print (adress[i])
change_adress(adress)
