### https://pl.wikipedia.org/wiki/Algorytm_Metropolisa-Hastingsa
# Metoda Metropolisa
# Rozkład próbkowany - to nieunormowany rozkład normalny. 
# Celem całkowania tego rozkładu jest wyznaczenie stałej normującej go do 1

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import choice

mean = 1     # Średnia próbkowanego rozkładu
std_dev = 1  # Odchylenie standardowe próbkowanego rozkładu

def rozkład(x):
    return np.exp(-0.5*((x - mean)/std_dev)**2)

# Rozkład docelowy - to rozkład normalny, unormowany do 1;
# jego wykres wykorzystamy do porównania go z rozkładem próbek (histogram),
# otrzymanych za pomocą metody Metropolisa
def rozkład_norm_miks(x):
    return np.exp(-0.5*((x - mean)/std_dev)**2)/(std_dev*np.sqrt(2*np.pi))

# Liczba próbek
n = 100000

# Punkt startowy - dowolnie wybramy z dziedziny próbkowanej funkcji rozkład(x)
x_aktualny = -2   

# Inicjalizacja licznika akceptowanych próbek
zakceptowane_probki = 0

# Lista do przechowywania próbek
probki = []

# Główna pętla algorytmu Metropolisa-Hastingsa
for _ in range(n):
    # Generowanie x_proponowany z rozkładu normalnego
    x_proponowany = x_aktualny + np.random.normal(0, 0.02)  
    wspolczynnik_akceptacji = rozkład(x_proponowany) / rozkład(x_aktualny)

    # Losowa decyzja o akceptacji lub odrzuceniu propozycji
    if np.random.uniform(0, 1) <= wspolczynnik_akceptacji:
         x_aktualny = x_proponowany
         zakceptowane_probki += 1
         probki.append(x_aktualny)

# Obliczenie przybliżone całki:
Calka =  zakceptowane_probki / n
print("Przybliżona wartość całki:", Calka)

# ---------------  DODATEK: WYKRESY ---------------
# Dzielenie listy próbek przez Całka, w celu unormowania:
# a) tworzę pustą listę na próbki unormowane przez całkę b) dzielę każdy element
# listy 'probki' przez 'Calka' c) dodaję do listy 'probki_unormowane'
probki_normowane = []
for element in probki:
    probki_normowane.append(element / Calka)

# Wykresy: histogram unormowany próbek i wykres rozkładu normalnego
plt.figure(figsize=(8, 6))
plt.hist(probki_normowane, bins=150, density=True, alpha=0.6, color='blue', label='Próbki')
x_zakres = np.linspace(-5, 5, 1000)
plt.plot(x_zakres, rozkład_norm_miks(x_zakres), color='red', label='Rozkład docelowy')
plt.title('Unormowany histogram próbek z nieunormowanego rozkładu normalnego')
plt.xlabel('x')
plt.ylabel('Prawdopodobieństwo')
plt.legend()
plt.grid(True)
plt.show()
