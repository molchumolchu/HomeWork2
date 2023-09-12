# Задача 10
# from random import randint
# N=int(input("Введите количество монет: "))
# count1=count2=0
# temp=0
# for i in range (N):
#     temp=randint(0,1)
#     print(temp, end=' ')
#     if temp==0:
#         count1+=1
#     else:
#         count2+=1
# print(end=' \n')
# if count1>count2:
#     print(f'Минимальное количесвто поворотов {count2} раз')
# else:
#     print(f'Минимальное количесвто поворотов {count1} раз')


#Задача 12
# S=int(input("Введите сумму чисел X и Y: "))
# P=int(input("Введите произведение чисел X и Y: "))
# X,Y=1, 1
# for X in range (1000):
#     for Y in range (1000):
#         if (Y+X==S and Y*X==P):
#             print(X, Y)
#             exit() # если не добавить то будет выводиться комбинация 2 3 и 3 2

#Задача 14
# N=int(input("Введите число N: "))
# n=2
# for i in range (0, N, 1):
#     if (n**i<N):
#         print (n**i, end=' ')