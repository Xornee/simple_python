# Zadanie 1: Wydrukuj liczby od 1 do 10

# Opis zadania: Napisz funkcję, która wypisze liczby od 1 do 10, korzystając z pętli.

# Zadanie 2: Wydrukuj tablicę liczb z podwojonymi wartościami

# Opis zadania: Napisz funkcję, która zwróci nową tablicę, gdzie każda liczba jest podwojona.

# Zadanie 3: Odwróć słowo

# Opis zadania: Napisz funkcję, która odwróci dane słowo

# Zadanie 4: Filtruj tablicę według warunku

# Opis zadania: Napisz funkcję, która przyjmie tablicę liczb i zwróci nową tablicę, która zawiera tylko te liczby, które są większe niż dana wartość.

# Zadanie 5: Znajdź najdłuższy ciąg znaków w tablicy

# Opis zadania: Napisz funkcję, która znajdzie najdłuższy ciąg znaków w tablicy napisów.

# Zadanie 6: Usuń duplikaty z tablicy

# Opis zadania: Napisz funkcję, która usunie duplikaty z tablicy i zwróci nową tablicę z unikalnymi wartościami.

#ZAD.1

# def liczby():
#     for cyfry in range(1, 11):
#         print(f'{cyfry}')

# liczby()

#ZAD.2
# lista = [12, 12, 2, 2, 4, 5, 6]

# def podwoic():
#     lista2 = []
#     for cyfry in lista:
#         lista2.append(cyfry * 2)
#     return lista2

# print(podwoic())

#ZAD.3 
# tab = [1,2,3,4]
# slowo = input("Enter word: ") 

# def odwrocic():
#     odwrocone = "" # pojemnij 

#     for litera in slowo: # ab
#         odwrocone = litera + odwrocone # operacje gdzies zapisujesz 

#     return odwrocone # 4 zwracamy 

# print(odwrocic()
### wykonac działanie 

#ZAD.4
# tab = []

# def generator():
#     for cyfry in range(1,11):
#         tab.append(cyfry)

# generator()

# tablice = [12,14,55,5555,45]
# tablica2 = [34,6785,42,1]

# wiekszeOd = int(input("Od jakiej liczby maja byc wieksze: "))

# def cyfry(tablicaPrzekazana):
#     liczbywieksze = []
#     for x in tablicaPrzekazana:
#         if x > wiekszeOd:
#             liczbywieksze.append(x)
#     return liczbywieksze

# print(cyfry(tab))
# print(cyfry(tablice))
# print(cyfry(tablica2))

#ZAD.5

# tablice = ["asd","asdf","as", "a", "asdfg", "a"] # 


# def znajdzNajdluzszy(przekazanaTab):
#     najdluzszy = ""
#     for x in przekazanaTab:
#         if len(x) > len(najdluzszy):
#             najdluzszy = x
#     print(najdluzszy)
    
# znajdzNajdluzszy(tablice)
# tablice = ["asd","asdf","as", "a", "asdfg", "a"] # 

# tablice = ["oisdnffdison", "ijodadasjio", "kodskosdkodskosd"]
# def znajdz_najdluzszy_wyraz(przekazanatab):
#     najdluzszywyraz = "" 
#     for pojedynczy_element in przekazanatab: 
#         if len(pojedynczy_element) > len(najdluzszy


#             najdluzszywyraz = pojedynczy_element 
#     print(najdluzszywyraz)


# znajdz_najdluzszy_wyraz(tablice)


# Zadanie 6: Usuń duplikaty z tablicy

# Opis zadania: Napisz funkcję, która usunie duplikaty z tablicy i zwróci nową tablicę z unikalnymi wartościami.

######################

#1. pisze tablice, pozniej druga tablica ktora bedzie bez duplikatow w def, 

# sprawdz czy sie powtarza 
# if element in przekazanaTab - to znaczy czy element juz jest w talibcy 
# liste unikatow 
# 

# tablice = [12,12,14,14,15,16,5,5,80]

# def zanajdz_duplikaty(przekazanaTab):
#     tablice2 = []
#     print(f' przed wykonaniem petli {tablice2}')
#     for elementWprzekazanaTab in przekazanaTab:
#         print(f' pojedyczy lement tablicy to {elementWprzekazanaTab}')
#         if elementWprzekazanaTab in tablice2:
#             print(f'{elementWprzekazanaTab} jest juz zduplikowany')
#         else: 
#             tablice2.append(elementWprzekazanaTab)
#             print(f'tak wyglada nasza tablica jesli element jest unikalny {elementWprzekazanaTab}')

# zanajdz_duplikaty(tablice)


