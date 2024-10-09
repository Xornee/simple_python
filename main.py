# main.py

# 1. input() – Pobieranie danych od użytkownika
# Funkcja input() umożliwia pobranie danych od użytkownika. Domyślnie zwracana jest wartość w
# postaci napisu (czyli typu string).
#
# Przykład:
imie = input("Jak masz na imię? ")
print("Cześć,", imie)

# 2. Konwersja typu: str na int
# Aby przekonwertować napis (string) na liczbę całkowitą (int), można użyć funkcji int().
# Pamiętaj, że string musi być liczbą, w przeciwnym razie pojawi się błąd.
#
# Przykład:
wiek_str = input("Ile masz lat? ")  # Wprowadzenie wieku jako string
wiek_int = int(wiek_str)  # Konwersja na int
print("Masz", wiek_int, "lat.")

# 3. Konwersja typu: str na float
# Aby przekonwertować napis (string) na liczbę zmiennoprzecinkową (float), można użyć funkcji float().
# Podobnie jak w przypadku int(), string musi być poprawnym formatem liczby zmiennoprzecinkowej.
#
# Przykład:
cena_str = input("Podaj cenę: ")
cena_float = float(cena_str)  # Konwersja na float
print("Cena to:", cena_float)

# 4. if, elif, else – Instrukcje warunkowe
# Instrukcje warunkowe pozwalają na wykonanie różnych bloków kodu w zależności od spełnienia warunków.
# Używamy ich do podejmowania decyzji w programie.
#
# Przykład:
liczba = int(input("Podaj liczbę: "))
if liczba > 0:
    print("Liczba jest dodatnia.")
elif liczba < 0:
    print("Liczba jest ujemna.")
else:
    print("Liczba jest zerem.")

# 5. Pętle: for
# Pętla for służy do iteracji przez elementy sekwencji (np. listy, krotki, stringi).
# Przykład:
liczby = [1, 2, 3, 4, 5]
for liczba in liczby:
    print("Liczba:", liczba)

# 6. Pętle: while
# Pętla while wykonuje blok kodu tak długo, jak długo warunek jest prawdziwy.
# Przykład:
i = 0
while i < 5:
    print("Wartość i:", i)
    i += 1  # Zwiększamy i o 1

# 7. Listy
# Listy w Pythonie to kolekcje, które mogą zawierać różne typy danych.
# Możemy dodawać, usuwać i modyfikować elementy w liście.
#
# Przykład:
liczby = [10, 20, 30]
liczby.append(40)  # Dodajemy 40 do listy
print("Lista po dodaniu:", liczby)

# 8. Listy - dostęp do elementów
# Możemy uzyskać dostęp do elementów listy za pomocą indeksu (indeksy zaczynają się od 0).
#
# Przykład:
pierwsza_liczba = liczby[0]  # Dostęp do pierwszego elementu
print("Pierwsza liczba:", pierwsza_liczba)

# 9. Listy - pętla for w kontekście list
# Używamy pętli for, aby przejść przez wszystkie elementy listy.
#
# Przykład:
for liczba in liczby:
    print("Element w liście:", liczba)

# 10. Funkcje
# Funkcje pozwalają na zorganizowanie kodu w mniejsze, bardziej zrozumiałe fragmenty.
# Możemy zdefiniować własne funkcje, aby wykonać konkretne zadania.
#
# Przykład:
def dodaj(a, b):
    return a + b

wynik = dodaj(5, 3)
print("Wynik dodawania:", wynik)

# 11. Modulo (%)
# Operator modulo zwraca resztę z dzielenia. Jest użyteczny do sprawdzania parzystości liczb.
#
# Przykład:
liczba = int(input("Podaj liczbę, aby sprawdzić, czy jest parzysta: "))
if liczba % 2 == 0:
    print("Liczba jest parzysta.")
else:
    print("Liczba jest nieparzysta.")

# 12. Zagnieżdżone instrukcje warunkowe
# Możemy używać instrukcji warunkowych wewnątrz innych instrukcji warunkowych.
#
# Przykład:
wiek = int(input("Ile masz lat? "))
if wiek < 18:
    print("Jesteś niepełnoletni.")
else:
    if wiek >= 65:
        print("Jesteś seniorem.")
    else:
        print("Jesteś dorosły.")

# 13. Wartości domyślne dla input()
# Możemy podać wartości domyślne, które będą używane, gdy użytkownik nie poda żadnej wartości.
#
# Przykład:
imie = input("Jak masz na imię? (naciśnij Enter, aby pominąć): ") or "Nieznany"
print("Cześć,", imie)

# 14. Łączenie stringów
# Możemy łączyć (konkatenować) stringi za pomocą operatora +.
#
# Przykład:
imie = "Jan"
nazwisko = "Kowalski"
pelne_imie = imie + " " + nazwisko
print("Pełne imię i nazwisko:", pelne_imie)

# 15. Wydrukuj wszystkie elementy listy w formie stringu
# Możemy połączyć elementy listy w jeden string za pomocą metody join().
#
# Przykład:
owoce = ["jabłko", "banan", "czereśnia"]
owoce_string = ", ".join(owoce)
print("Owoce:", owoce_string)
