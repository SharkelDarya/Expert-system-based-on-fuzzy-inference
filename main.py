import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt
import numpy as np

# Zakres temperatury
temperature = np.arange(-15, 40, 1)
# Definicja funkcji przynależności rozmytej dla temperatury
cold = np.maximum(0, 1 - np.abs((temperature - 0) / 15))
moderate = np.maximum(0, 1 - np.abs((temperature - 20) / 10))
hot = np.maximum(0, 1 - np.abs((temperature - 30) / 5))

# Wykresy funkcji przynależności rozmytej dla temperaturypip
plt.figure(figsize=(8, 4))
plt.plot(temperature, cold, label='Niska')
plt.plot(temperature, moderate, label='Średnia')
plt.plot(temperature, hot, label='Wysoka')
plt.title('Temperatura')
plt.xlabel('Temperature C')
plt.ylabel('Przynależność')
plt.legend()
plt.grid(True)
plt.show()

# Zakres prędkości wiatru
wind_speed = np.arange(0, 45, 1)
# Definicja funkcji przynależności rozmytej dla prędkości wiatru
low_wind = np.maximum(0, 1 - np.abs((wind_speed - 10) / 10))
moderate_wind = np.maximum(0, 1 - np.abs((wind_speed - 25) / 10))
high_wind = np.maximum(0, 1 - np.abs((wind_speed - 35) / 5))

# Wykresy funkcji przynależności rozmytej dla prędkości wiatru
plt.figure(figsize=(8, 4))
plt.plot(wind_speed, low_wind, label='Słaby')
plt.plot(wind_speed, moderate_wind, label='Umiarkowy')
plt.plot(wind_speed, high_wind, label='Silny')
plt.title('Waitr')
plt.xlabel('Prędkość km/h')
plt.ylabel('Przynależność')
plt.legend()
plt.grid(True)
plt.show()

# Zakres indeksu UV
uv_index = np.arange(0, 13, 1)

# Definicja funkcji przynależności rozmytej dla indeksu UV
low_uv = np.maximum(0, 1 - np.abs((uv_index - 2) / 2))
moderate_uv = np.maximum(0, 1 - np.abs((uv_index - 6) / 3))
high_uv = np.maximum(0, 1 - np.abs((uv_index - 10) / 2))

# Wykresy funkcji przynależności rozmytej dla indeksu UV
plt.figure(figsize=(8, 4))
plt.plot(uv_index, low_uv, label='Niski')
plt.plot(uv_index, moderate_uv, label='Umiarkowy')
plt.plot(uv_index, high_uv, label='Wysoki')
plt.title('UV index')
plt.xlabel('UV index')
plt.xlim(0, 12)
plt.ylabel('Przynależność')
plt.legend()
plt.grid(True)
plt.show()


# Zakres ciśnienia atmosferycznego
pressure = np.arange(970, 1040, 1)

# Definicja funkcji przynależności rozmytej dla ciśnienia atmosferycznego
low_pre = np.maximum(0, 1 - np.abs((pressure - 990) / 10))
medium_pre = np.maximum(0, 1 - np.abs((pressure - 1005) / 10))
high_pre = np.maximum(0, 1 - np.abs((pressure - 1020) / 10))

# Wykresy funkcji przynależności rozmytej dla ciśnienia atmosferycznego
plt.figure(figsize=(8, 4))
plt.plot(pressure, low_pre, label='Niskie')
plt.plot(pressure, medium_pre, label='Umiarkowe')
plt.plot(pressure, high_pre, label='Wysokie')
plt.title('Ciśnienie')
plt.xlabel('ciśnienie hPa')
plt.ylabel('Przynależność')
plt.legend()
plt.grid(True)
plt.show()

#Krok 3

# Define the linguistic variables
wind_speed = ctrl.Antecedent(np.arange(0, 41, 1), 'wind_speed')
pressure = ctrl.Antecedent(np.arange(970, 1040, 1), 'pressure')
uv_index = ctrl.Antecedent(np.arange(0, 13, 1), 'uv_index')
temperature = ctrl.Antecedent(np.arange(-10, 40, 1), 'temperature')

przydatnosc_pоgody = ctrl.Consequent(np.arange(0, 11, 1), 'przydatność_pогody')

przydatnosc_pоgody['niska'] = fuzz.trimf(przydatnosc_pоgody.universe, [0, 2, 5])
przydatnosc_pоgody['średnia'] = fuzz.trimf(przydatnosc_pоgody.universe, [3, 6, 8])
przydatnosc_pоgody['wysoka'] = fuzz.trimf(przydatnosc_pоgody.universe, [6, 8, 10])

plt.figure()

# niska
plt.plot(przydatnosc_pоgody.universe, fuzz.trimf(przydatnosc_pоgody.universe, [0, 2, 5]), 'b', label='niska')
# średnia
plt.plot(przydatnosc_pоgody.universe, fuzz.trimf(przydatnosc_pоgody.universe, [3, 6, 8]), 'orange', label='średnia')
# wysoka
plt.plot(przydatnosc_pоgody.universe, fuzz.trimf(przydatnosc_pоgody.universe, [6, 8, 10]), 'g', label='wysoka')

plt.title('Funkcje przynależności')
plt.ylabel('Stopień przynależności')
plt.xlabel('Wartość')
plt.grid(True)
plt.legend()

plt.show()

# Definiowanie funkcji przynależności dla poszczególnych zmiennych lingwistycznych

wind_speed['słaby'] = fuzz.gaussmf(wind_speed.universe, 10, 10)
wind_speed['umiarkowany'] = fuzz.gaussmf(wind_speed.universe, 25, 10)
wind_speed['silny'] = fuzz.gaussmf(wind_speed.universe, 35, 5)

pressure['niskie'] = fuzz.trimf(pressure.universe, [980, 990, 1000])
pressure['średnie'] = fuzz.trimf(pressure.universe, [995, 1005, 1015])
pressure['wysokie'] = fuzz.trimf(pressure.universe, [1010, 1020, 1030])

uv_index['niskie'] = fuzz.trimf(uv_index.universe, [0, 2, 4])
uv_index['średnie'] = fuzz.trimf(uv_index.universe, [3, 6, 9])
uv_index['wysokie'] = fuzz.trimf(uv_index.universe, [8, 10, 12])

temperature['niska'] = fuzz.trimf(temperature.universe, [-15, 0, 15])
temperature['średnia'] = fuzz.trimf(temperature.universe, [10, 20, 30])
temperature['wysoka'] = fuzz.trimf(temperature.universe, [25, 30, 35])

#Kiedy pogoda jest dobra:
rule1 = ctrl.Rule(wind_speed['słaby'] & pressure['średnie'], przydatnosc_pоgody['wysoka'])
rule2 = ctrl.Rule(wind_speed['słaby'] & pressure['niskie'], przydatnosc_pоgody['wysoka'])
rule3 = ctrl.Rule(wind_speed['umiarkowany'] & pressure['niskie'], przydatnosc_pоgody['wysoka'])
rule4 = ctrl.Rule(temperature['średnia'] & uv_index['niskie'], przydatnosc_pоgody['wysoka'])
rule5 = ctrl.Rule(temperature['wysoka'] & wind_speed['umiarkowany'], przydatnosc_pоgody['wysoka'])

#Kiedy pogoda jest średnia:
rule6 = ctrl.Rule(temperature['średnia'] & uv_index['średnie'], przydatnosc_pоgody['średnia'])
rule7 = ctrl.Rule(temperature['niska'] & wind_speed['słaby'], przydatnosc_pоgody['średnia'])
rule8 = ctrl.Rule(temperature['średnia'] & wind_speed['umiarkowany'], przydatnosc_pоgody['średnia'])
rule9 = ctrl.Rule(temperature['średnia'] & wind_speed['silny'], przydatnosc_pоgody['średnia'])
rule10 = ctrl.Rule(pressure['średnie'] & uv_index['niskie'], przydatnosc_pоgody['średnia'])

#Kiedy pogoda jest najgorsza:
rule11 = ctrl.Rule(temperature['niska'] & wind_speed['silny'], przydatnosc_pоgody['niska'])
rule12 = ctrl.Rule(pressure['wysokie'] & uv_index['wysokie'], przydatnosc_pоgody['niska'])

# Tworzenie systemu wnioskowania
usefulness_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12])
ocena_przydatnosci = ctrl.ControlSystemSimulation(usefulness_ctrl)

# Wprowadzanie danych pogodowych
ocena_przydatnosci.input['wind_speed'] = 42
ocena_przydatnosci.input['pressure'] = 1029
ocena_przydatnosci.input['uv_index'] = 11
ocena_przydatnosci.input['temperature'] = -9


# Obliczanie przydatności
ocena_przydatnosci.compute()

print("Ocena przydatności: ", ocena_przydatnosci.output['przydatność_pогody'])
przydatnosc_pоgody.view(sim=ocena_przydatnosci)

methods = ['centroid', 'bisector', 'mom', 'som', 'lom']

for method in methods:
    ocena_przydatnosci.defuzzify_method = method
    ocena_przydatnosci.compute()
    print(f"Metod: {method}, Wynik: {ocena_przydatnosci.output['przydatność_pогody']}")

#Krok 4

while True:
    wind_speed_input = float(input("Wprowadz predkosc wiatru (1 - 42 km/h): "))
    pressure_input = float(input("Wprowadz ciesnienie (981 - 1029 hPa): "))
    uv_index_input = float(input("Wprowadz index UV (1 - 11): "))
    temperature_input = float(input("Wprowadz temperature (-9 - 39 C): "))

    ocena_przydatnosci.input['wind_speed'] = wind_speed_input
    ocena_przydatnosci.input['pressure'] = pressure_input
    ocena_przydatnosci.input['uv_index'] = uv_index_input
    ocena_przydatnosci.input['temperature'] = temperature_input

    ocena_przydatnosci.compute()
    print("Ocena przydatności potrawы: ", ocena_przydatnosci.output['przydatność_pогody'])
    przydatnosc_pоgody.view(sim=ocena_przydatnosci)

    for method in methods:
        ocena_przydatnosci.defuzzify_method = method
        ocena_przydatnosci.compute()
        print(f"Metod: {method}, Wynik: {ocena_przydatnosci.output['przydatność_pогody']}")


    choice = input("Zadac nowe parametry? (tak/nie): ")
    if choice.lower() != 'tak':
        break

