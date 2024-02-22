import locale, datetime, pytz
from random import choice

_, x = locale.setlocale(locale.LC_ALL, 'pl_PL'), datetime.datetime.now(pytz.timezone('Europe/Warsaw'))
data_i_godzina = f'{x.strftime("%A")}, {x.day} {x.strftime("%B")} {x.year}, godz. {x.strftime("%X")}'
## Lista zagadnień egzaminacyjnych
# https://wit.pwr.edu.pl/fcp/DGBUKOQtTKlQhbx08SlkAWgReUTgtCgg9ACFDC1RDTGFBWxslAxt1FSVcViU/190/public/studenci/pnps/20202021/prg_tai_w04_iim_st.pdf
zagadnienia_obowiązkowe, zagadnienia_wybieralne = ([   
    '1. Uczenie nadzorowane, półnadzorowane i bez nadzoru',
    '2. Optymalizacja wydajności i zarządzanie sieciami teleinformatycznymi',
    '3. Analiza architektury i właściwości wybranych systemów satelitarnych',
    '4. Przedstawić metody analizy wielowymiarowych danych statystycznych',
    '5. Przedstawić podstawowe narzędzia liniowej i nieliniowej estymacji funkcji regresji',
    '6. Omówić przykładowe zastosowania algorytmów kwantowych',
    '7. Inspiracje kognitywistyczne w naukach technicznych i technice',
    '8. Metody uczenia sieci neuronowych',
    '9. Zastosowanie sieci neuronowych w rozpoznawaniu wzorców',
    '10. Współczesne metody optymalizacji' 
],[   
    # Moduł A
	('1.1. Obsługa incydentów i funkcjonowanie SOC', 
     '1.2. Metody i narzędzia audytu technicznego'),
    # Moduł B
	('2.1. Charakterystyka przetwarzania współbieżnego, równoległego oraz rozproszonego', 
     '2.2. Klasyfikacja, detekcja i segmentacja obrazów z wykorzystaniem głębokich sieci neuronowych'),
    # Moduł C
	('3.1. Techniki analizy i modelowania sygnałów wielowymiarowych', 
     '3.2. Podstawowe metody modelowania systemów wizualnych'),
    # Moduł D
	('4.1. Algorytmy sztucznej inteligencji w grach komputerowych', 
     '4.2. Zastosowanie i zasada działania przykładowych algorytmów uczenia maszynowego w obszarze grafiki i animacji komputerowej'),
    # Moduł E
	('5.1. Przetwarzanie języka naturalnego. Metody, techniki oraz zastosowanie', 
     '5.2. Roboty internetowe oraz inteligentne metody przeszukiwania informacji'),
    # Moduł F
	('6.1. Systemy i sieci IoT - architektury, technologie, protokoły komunikacyjne', 
     '6.2. Modelowanie struktury i ruchu w sieci z wykorzystaniem podejścia grafowego'),
    # Moduł G
	('7.1. Modelowanie ruchu w sieciach teleinformatycznych', 
     '7.2. Wykrywanie anomalii w systemach ICT. Obszary zastosowań i metody'),
])
##                   |1.1 1.2|2.1 2.2|3.1 3.2|4.1 4.2|5.1 5.2|6.1 6.2|7.1 7.2| 
#wybrane_przedmioty = ((1, 0), (1, 0), (1, 0), (0, 1), (0, 1), (1, 0), (1, 0)) # rok akademicki 2021/22  
wybrane_przedmioty = ((0, 1), (0, 1), (0, 1), (1, 0), (1, 0), (0, 1), (0, 1))  # rok akademicki 2022/23
zagadnienia_wybieralne = *(zw[wp[1]] for (zw, wp) in zip(zagadnienia_wybieralne, wybrane_przedmioty)),

zagadnienie_obowiązkowe, zagadnienie_wybieralne = (choice(zagadnienia_obowiązkowe), 
                                                   choice(zagadnienia_wybieralne))
## ¡Showtime!
print('⁜' * 0x44)
print(f'{data_i_godzina}. Wylosowane zagadnienia:\n') 
print(f'O: {zagadnienie_obowiązkowe}')
print(f'W: {zagadnienie_wybieralne}')
print('⁜' * 0x44)