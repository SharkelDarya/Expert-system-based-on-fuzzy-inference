# Expert-system-based-on-fuzzy-inference
System wykorzystujący logikę rozmytą do oceniania pogody na zewnątrz.
<p align="center">
      <img src="https://i.ibb.co/2dW62Qj/wheather.jpg">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Engine-VS%20Code-2B7FB8" alt="Engine">
</p>

## About

Projekt wdraża system do oceny przydatności pogody dla różnych działań w oparciu o parametry takie jak prędkość wiatru, temperatura, indeks UV i ciśnienie atmosferyczne. Wykorzystując logikę rozmytą i zestaw reguł zdefiniowanych dla różnych warunków pogodowych, system zapewnia ocenę przydatności pogody dla aktywności na trzech poziomach: "niskim", "średnim" i "wysokim". Tak samo jest możliwość wprowadzić bieżące parametry pogodowe i uzyskać ocenę.
## Documentation

### Libraries
**-** **`skfuzzy`**, **`matplotlib`**, **`NumPy`**

### Wyznaczanie funkcji przynależności dla czynników pogodowych
- Przypisanie temperatury, prędkości wiatru, indeksu UV i ciśnienia atmosferycznego do funkcji przynależności (niska, średnia, wysoka).
  
### Tworzenie reguł rozmytych
- Korzystając z funkcji przynależności, tworzonie reguł rozmytych w celu określenia, które warunki pogodowe są uważane za "dobre", "średnie" i "złe" dla określonych działań.
  
### Tworzenie rozmytego systemu sterowania
- Tworzony jest system sterowania logiką rozmytą, który łączy reguły rozmyte.
  
### Ocena przydatności
- Korzystając z testowych parametrów pogodowych, system sterowania rozmytego ocenia przydatność pogody.
  
### Wizualizacja wyników
- Wizualizacje funkcji członkowskich i wyniki oceny przydatności za pomocą wykresów.
  
### Interakcja z użytkownikiem
- Nieskończona pętla, umożliwiającą użytkownikowi wprowadzenie parametrów pogodowych i uzyskanie oceny przydatności.
  
### Wizualizacja wyników
- Wyświetlanie niektórych obrazów testowych oraz odpowiadające im prawdziwe etykiety.
## Developers

- Darya Sharkel (https://github.com/SharkelDarya)
