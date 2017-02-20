#Напишите скрипт, позволяющий определить надежность вводимого
#пользователем пароля. Это задание является творческим: алгоритм
#определения надежности разработайте самостоятельно.
#https://habrahabr.ru/sandbox/27520/
#\   
password = input()
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}']
count_num = 0
count_sym = 0
count_upp = 0
numeric=0
numsymbols=0
upper=0
crash_pass=list(password)
pwlength = len(password)
for i in range (len(crash_pass)):
    if crash_pass[i].isdigit():
        count_num +=1
    if crash_pass[i].isupper():
        count_upp+=1
    for j in range (len(symbols)):
        if crash_pass[i]==symbols[j]:
            count_sym+=1
numeric = count_num
numsymbols = count_sym
upper = count_upp
print(pwlength)
print(numeric)
print(numsymbols)
print(upper)
pwstrength = ((pwlength*10)-20)+(numeric*10)+(numsymbols*15)+(upper*10)
if pwstrength>100:
    pwstrength = 100
elif pwstrength<0:
    pwstrength = 0 
print(pwstrength)
