# print("a.")
# for a in range(0,9):
#     if a % 2 == 0:
#         print(f'{a}')


# print("b.")
# for b in range(10,1, -2):
#     print(f'{b}')

# min() 

# tablica = []

# tablica.append("1")
    
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
 
# tablica = [num1, num2, num3]


# def pokazNajmniejsza():
#     if num1 <= num2 and num1 <= num3:
#         return num1
#     elif num2 <= num1 and num2 <= num3:
#         return num2
#     elif num3 <= num1 and num3 <= num2:
#         return  num3

# najmniejsza = pokazNajmniejsza("")
# print(najmniejsza)

#uzytkonik podaje 2 liczby funckja ma obliczyc pole prostokonta

# a = int(input("Enter first num: "))
# b = int(input("Enter second num: "))

# def obliczpole():
#     print(f'{a*b}')

# obliczpole()



# lista = []
# lista2 = [2, 3, 4, "test", [2, 4]]

# # for elementy in lista2:
# #     print(elementy)


# my_list = [1, 2, [3, 4, 'uowd', ['Spider', 7.2, -3]], [32, 'hi'], ['T-Rex', 'Olympus Mons', [-12.3, 'TON 618']]]

# # for elementy in my_list:
# #     print(elementy)

# print(my_list[4][2][0])

# # print(my_list[2][3][0])

# ### wypisuj nie zgadłes dopoki uzytkownik nie zgadnie liczby 


# nasza_liczba = 40 
# liczba_urzytkownia = int(input("Podjaj liczbe z zakresu od 0 - 100:"))

# while(nasza_liczba != liczba_urzytkownia):
#     print("Nie zgadłes")
#     liczba_urzytkownia = int(input("Podjaj liczbe z zakresu od 0 - 10"))

# print("Zgadłes")


### Podziel dwie liczby - uzytkownik ma byc pytany o zmiane licazbny jesli wpisze zero 

# num1 = int(input("Enter first num: "))
# num2 = int(input("Enter second num: "))

# def nazwaFunkcji():
#     while(num2 == 0):
#         print("Podaj jeszcze raz") 
#         num2 = int(input("Podaj liczbe")) 

# print("Correct")
# print(f'{num1 / num2}')
