import numpy as np

# 1. Utworzyć tablicę zawierającą 50 piątek

zad1 = np.linspace(5, 5, 50)

# 2. Utworzyć tablicę o rozmiarze 5x5 z wartościami od 1 do 25

zad2 = np.linspace(1, 25, 25).reshape(5, 5)

# 3. Utworzyć tablicę liczb parzystych od 10 do 50

zad3 = np.arange(10, 51, 2)

# 4. Utworzyć macierz, w której na przekątnej znajdą się wartości równe 8, a pozostałe będą wynosiły 0

zad4 = np.eye(5)*8

# 5. Utworzyć tablicę o rozmiarze 10x10 z wartościami zwiększającymi się o 0.01

zad5 = np.arange(0, 1, 0.01).reshape(10, 10)

# 6. Utworzyć przestrzeń liniową 50 wartości z zakresu 0-1

zad6 = np.linspace(0, 1, 50)

# 7. Wybrać podtablicę 12-elementową, z tablicy utworzonej w zadaniu 2, z wartościami w zakresie 12-25

zad7 = zad2.flatten()[12:24]

# 8. Wybrać 3 pierwsze elementy z ostatniej kolumny tablicy utworzonej w zadaniu 2, a następnie ułożyć z nich kolumnę

zad8 = zad2[0:3, 4:5]

# 9. Wyznaczyć sumę wartości elementów znajdujących się w dwóch ostatnich wierszach macierzy utworzonej w zadaniu 2

zad9 = np.sum(zad2[3:5, 0:5])

# 10. Przygotować skrypt, który stworzy tensor zawierający losowe wartości całkowite, losowym wymiarze i losowym rozmiarze każdego z wymiarów

print(zad9)
