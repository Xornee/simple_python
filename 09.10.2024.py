#Zadanie 0: Sprawdź, czy liczba jest dodatnia, ujemna, czy zerem
#Opis:
#Napisz program w Pythonie, który sprawdza, czy podana liczba jest dodatnia, ujemna, czy zerem.
#Instrukcje:
#
#Poproś użytkownika o wprowadzenie liczby.
#Użyj instrukcji if, aby sprawdzić, czy liczba jest większa od zera, mniejsza od zera, czy równa zero.
#Wypisz odpowiednią informację: "Liczba jest dodatnia", "Liczba jest ujemna" lub "Liczba jest zerem".

num1 = int(input("Enter first number: "))

if num1 > 0:
    print(" num1 is positive")
elif num1 < 0:
    print("num1 is negative")
else:
    print("num1 equals 0")
#------------------------

#Zadanie 1: Suma elementów w liście
#Opis:
#Napisz program w Pythonie, który oblicza sumę wszystkich elementów w liście.
#Instrukcje:

#Utwórz listę z co najmniej 5 liczbami.
#Użyj pętli for, aby przejść przez wszystkie elementy listy i dodać je do siebie.
#Wypisz sumę wszystkich liczb.

lista = [1, 2, 3, 4, 5]
suma_elementow = 0

for number in lista:
    suma_elementow += number
    
print(f'suma_elementow equals {suma_elementow}')


# suma_elementow = suma_elementow + number
#--------------------------

#Zadanie 2: Policz liczby parzyste i nieparzyste w liście
#Opis:
#Napisz program w Pythonie, który zlicza ile liczb w liście jest parzystych, a ile nieparzystych.
#Instrukcje:
#
#Utwórz listę z co najmniej 7 liczbami.
#Użyj pętli for, aby przejść przez wszystkie liczby w liście.
#Sprawdź, czy każda liczba jest parzysta lub nieparzysta za pomocą operatora modulo (%).
#Zliczaj liczby parzyste i nieparzyste.
#Wypisz wynik.
lista = [1,2,3,4,5,6,7] 

iloscparzystych = 0
iloscnieparzystych = 0

for number in lista:
    if number % 2 == 0: 
        liczbaparzysta += 1
    if number % 2 == 1:
        liczbanieparzysta += 1

print(f'liczbaprzysta {liczbaparzysta}, liczbanieparzysta {liczbanieparzysta}')


#---------------------------

#Zadanie 3: Znajdź największy element w liście
#Opis:
#Napisz program w Pythonie, który znajduje największą liczbę w liście.
#Instrukcje:
#
#Utwórz listę z co najmniej 6 liczbami.
#Użyj pętli, aby znaleźć największą liczbę w liście.
#Wypisz największą liczbę.

liczby = [10, 20, 5, 30]

najwieksza = liczby[0] # zakladamy ze najwiekszy element to pierwszy element

for liczba in liczby: 
    if liczba > najwieksza: # sprawdzamy czy sie pomylilismy porowonojac elementy liczby do zalozenia 
        najwieksza  = liczba # jezeli tak to przypiosujemy nowa najwieksza liczba do zmiennej najwieksza 

-------------------------------

#Zadanie 4: Wydrukuj liczby podzielne przez 3
#Opis:
#Napisz program w Pythonie, który wypisze wszystkie liczby podzielne przez 3 z listy.
#Instrukcje:
#
#Utwórz listę z co najmniej 10 liczbami.
#Użyj pętli for, aby przejść przez listę.
#Sprawdź, które liczby są podzielne przez 3 (użyj operatora modulo %).
#Wypisz te liczby.

lista = [33, 3, 10, 2, 6, 123, 4, 5, 8, 9]
 
 for liczba in lista:
     if liczba % 3 == 0:
         print(f'liczba{liczba}')
         
------------------------------

#Zadanie 5: Zlicz wystąpienia elementu w liście
#Opis:
#Napisz program w Pythonie, który zlicza, ile razy dany element pojawia się w liście.
#Instrukcje:
#
#Utwórz listę z co najmniej 8 liczbami, gdzie niektóre liczby się powtarzają.
#Użyj pętli, aby zliczyć, ile razy wybrany przez Ciebie element pojawia się w liście.
#Wypisz wynik.

lista = [3, 3, 3, 4, 5, 6, 4, 8]
liczbaSprawdzna = 4
iloscPowtorzen = 0

for liczba in lista:
    if liczba == liczbaSprawdzna:
        iloscPowtorzen += 1
                    
print(f'iloscPowtorzen {iloscPowtorzen}')                          
     
    

-------------------------------

#Zadanie 6: Oblicz średnią arytmetyczną elementów listy
#Opis:
#Napisz program w Pythonie, który oblicza średnią arytmetyczną wszystkich elementów w liście.
#Instrukcje:
#
#Utwórz listę z co najmniej 5 liczbami.
#Użyj pętli, aby obliczyć sumę wszystkich elementów w liście.
#Oblicz średnią, dzieląc sumę przez liczbę elementów w liście.
#Wypisz średnią.

lista = [1,2,3,4,5]
suma = 0 

for liczba in lista:
    suma += liczba
    
srednia = suma / len(lista) ### lenght 

------------------------------

numerki = []

for liczby in range(0, 20):
    numerki.append(liczby) ### dodaje to tablicy lista 
    
    
    ############
numerki = [0,1,2,3,4,5,6... 19]
