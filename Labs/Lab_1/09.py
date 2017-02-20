#Напишите программу, имитирующую работу банкомата. Выберите структуру данных для хранения
#купюр разного достоинства в заданном количестве. При вводе пользователем запрашиваемой
#суммы денег, скрипт должен вывести на консоль количество купюр подходящего достоинства.
#Если имеющихся денег не хватает, то необходимо напечатать сообщение «Операция не может
#быть выполнена!». Например, при сумме 5370 рублей на консоль должно быть выведено
#«5*1000 + 3*100 + 1*50 + 2*10». 
vvod = raw_input()
#vvod = '12310'
chek = True
count_0 = len(list(vvod)) - 1
summa = int(vvod)
bank = dict(short='dict', long='dictionary')
bank = dict([(1000, 10), (500, 5), (100, 10), (50, 10), (10, 10)])
bank_false = bank.copy()
bill = list(bank.keys())
j=0
for i in range (len(list(vvod))):
    delit = int('1'+ count_0*'0')
    ostatok = summa%delit
    summa = summa - summa%delit    
    while summa>0:
        if bank[bill[j]] == 0 or summa - bill[j]<0:
            if bank[bill[4]]==0 or summa - bill[4]<0:
                chek = False
                print('Невозможно произвести операцию! Нехватает купюр')
                bank = bank_false 
                summa=0
                break
            j+=1
        else:
            summa=summa - bill[j]
            bank[bill[j]]-=1
        #print(summa)
    summa = ostatok
    count_0-=1
if chek:
    sravnenie =[]
    for i in range (len(bank)):
        sravnenie = bank_false[bill[i]] - bank[bill[i]]
        if i==len(bank)-1:
            print(sravnenie, '*', bill[i], sep = '')
        else:
            print(sravnenie, '*', bill[i], sep = '', end = '+')
print(bank)
