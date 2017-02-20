#Написать скрипт, который выводит на экран «True», если
#элементы программно задаваемого списка представляют
#собой возрастающую последовательность, иначе – «False».

def check(arr):
    for i in range(1, len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True
list_one = [1, 2, 3, 4, 5]
list_two = [1, 3, 2, 4, 5]
print(check(list_one))
print(check(list_two))
