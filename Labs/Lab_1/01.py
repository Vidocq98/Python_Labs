#Напишите скрипт, который преобразует введенное с клавиатуры вещественное число в денежный формат.
#Например, число 12,5 должно быть преобразовано к виду «12 руб. 50 коп.».
#В случае ввода отрицательного числа выдайте сообщение «Некорректный формат!» путем обработки исключения в коде.
#ввести исключение 9,8
print("Print your money (float)")
# ������ �����
money = float(input())
def duration_string(money):
        if money < 0.0:
                raise
        else:
                return'{}руб.{}коп.'.format(int(money), int((money-int(money))*100))
try:
        print(duration_string(money))
except:
        print('Некоректный ввод')

