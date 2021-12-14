from random import *
s=pos=neg=null=[]
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    min=int(input("Введите минимальное число диапазона => "))
    max=int(input("Введите максимальное число диапазона => "))
    if max>=min:
       min,max=vahetus(min,max)#mini=100, maxi=5-> mini=5,maxi=100
       generaator(n,s,min,max)
       print()
       print("Результаты:")
       print("Полученный список от",min,"до",max,s)
       s.sort()
       print("Отсортированный список",s)
       jagamine(s,pos,neg,nol)
       print("Список положительных элементов",pos)
       print("Список отрицательных элементов",neg)
       print("Список нулевых элементов",null)
       kesk=keskmine(pos)
       lisamine(s,kesk)
       print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    print(s)

def vahetus(a:int,b:int):
    """kui min suurem kui max,siis vahetame neid omavahel
    :param: minimaalne arv, mis on suurem kui max
    :param: maximaale arv, mis on väiksem kui min
    :rtype:int,int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """ сортеруем список от мин до макс
    """
    for i in range(n):
     loend.append(randint(a,b))
    

def jagamine(loend:list,p:list,n:list,nol:list):
    """
    """
    for el in loend:
        if el>0:
            p(append(el))
        elif el<0:
            n(append(el))
        else:
            nol(append(el))

def keskmine(loend,):
    """вычесляем среднее число из списка
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend:list,el:float):
    """
    """
    loend.append(el)
    loend.sort()

arvud_loendis()
