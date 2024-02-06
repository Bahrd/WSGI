from numpy.random import choice
import locale, datetime, pytz

_, x = locale.setlocale(locale.LC_ALL, 'pl_PL'), datetime.datetime.now(pytz.timezone('Europe/Warsaw'))
nazwa_egzaminu, data_i_godzina = 'Egzamin dyplomowy, EZI', f'{x.strftime("%A")}, {x.day} {x.strftime("%B")} {x.year}, godz. {x.strftime("%X")}'
## Lista zagadnień egzaminacyjnych
# https://wefim.pwr.edu.pl/fcp/HGBUKOQtTKlQhbx08SlkDUg1eUTgtCgg9ACFDC1RCTWFBWxslAxt1FSVcVnRKCkI8VQIDJCUODBYAKg8TXBEbIRBSBw/219/public/2021/docs/zagadnienia-egzaminacyjne/eka_i_2021_2022.pdf
zagadnienie_kierunkowe, zagadnienie_specjalnościowe = ([   
    '1. Fala elektromagnetyczna: typy, parametry, właściwości',
    '2. Metody pomiaru napięcia, natężenia prądu i impedancji elektrycznej',
    '3. Parametry, właściwości i zastosowania elementów RLC',
    '4. Tranzystory bipolarne i unipolarne: budowa, właściwości i zastosowania',
    '5. Wzmacniacze operacyjne: właściwości i zastosowania',
    '6. Kombinacyjne i sekwencyjne układy logiczne',
    '7. Mikroprocesory: budowa, zastosowania',
    '8. Metody probabilistyczne w elektronice',
    '9. Ciągła, dyskretna i szybka transformata Fouriera, widmo sygnału',
    '10. Zasady działania przetworników elektroakustycznych'], [   
    '1. Sterowniki mikroprocesorowe i zastosowania',
    '2. Sieci komputerowe, architektura i programowanie',
    '3. Bazy danych, administracja, bezpieczeństwo i programowanie',
    '4. Przetwarzanie obrazów, algorytmy i zastosowania', 
    '5. Struktury danych i złożoność obliczeniowa algorytmów', 
    '6. Systemy operacyjne komputerów, klasyfikacja i struktura',
    '7. Zadania optymalizacji i techniki ich rozwiązywania',
    '8. Systemy dynamiczne, opisy własności',
    '9. Programowanie w systemie operacyjnym Unix', 
    '10. Interfejsy komputerowe'])

zagadnienie_kierunkowe, zagadnienie_specjalnościowe = (choice(zagadnienie_kierunkowe), 
                                                       choice(zagadnienie_specjalnościowe))
print(f'{nazwa_egzaminu}\n{data_i_godzina}.\nWylosowane zagadnienia:\n') 
print(f'K: {zagadnienie_kierunkowe}')
print(f'S: {zagadnienie_specjalnościowe}\n')
