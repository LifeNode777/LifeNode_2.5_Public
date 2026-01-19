import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# 1. Pobieramy realne dane (np. Bitcoin z ostatnich 2 lat)
# BTC-USD to Bitcoin, SPY to indeks giełdowy (S&P 500)
# Możesz zmienić 'BTC-USD' na 'SPY' lub inne ticker'y
data = yf.download('BTC-USD', period='2y', interval='1d')
prices = data['Close'].values.flatten() # FLATTEN naprawia błąd wymiaru

# Zabezpieczenie na wypadek brakujących danych
if len(prices) < 3:
    print("Brak wystarczających danych do analizy.")
    exit()

# 2. Silnik Q-CORE (Twoja Matematyka)
# Upewniamy się, że tablice mają odpowiednie długości
delta = np.abs(np.diff(prices, prepend=prices[0]))
awareness = np.gradient(delta)
curvature = np.gradient(awareness)

# Decyzje z większą czułością i wygładzeniem (dla lepszych wyników)
# Zwiększenie mnożnika (50) sprawia, że system jest bardziej wrażliwy na zmiany krzywizny
decisions = np.tanh(-curvature * 50)

# 3. Symulacja zysków (Prosty test - tylko LONG, brak shortów)
capital = 1000.0 # Kapitał początkowy
position = 0.0   # Ilość posiadanych aktywów
log_value = [capital] # Logowanie wartości portfela
buy_signals = []
sell_signals = []

for i in range(1, len(decisions)): # Zaczynamy od drugiego elementu, żeby porównywać z poprzednim
    current_price = prices[i]
    prev_decision = decisions[i-1] # Decyzja z poprzedniego dnia

    # Warunek KUPNA (Decyzja > 0.5 i nie jesteśmy w pozycji)
    if prev_decision > 0.5 and position == 0.0:
        position = capital / current_price # Kupujemy za cały kapitał
        capital = 0.0
        buy_signals.append(i) # Zapisujemy indeks dnia kupna

    # Warunek SPRZEDAŻY (Decyzja < -0.5 i jesteśmy w pozycji)
    elif prev_decision < -0.5 and position > 0.0:
        capital = position * current_price # Sprzedajemy wszystko
        position = 0.0
        sell_signals.append(i) # Zapisujemy indeks dnia sprzedaży

    # Aktualizujemy wartość portfela
    current_portfolio_value = capital if position == 0.0 else position * current_price
    log_value.append(current_portfolio_value)

# Jeśli na końcu mamy otwartą pozycję, zamknij ją po ostatniej cenie
if position > 0.0:
    final_value = position * prices[-1]
else:
    final_value = capital

# 4. WYNIK I DOWÓD (w formie tabelarycznej i graficznej)
start_capital = 1000.0
hold_final_value = start_capital * (prices[-1] / prices[0])
hold_return_percent = ((hold_final_value / start_capital) - 1) * 100

lifenode_return_percent = ((final_value / start_capital) - 1) * 100

print(f"\n--- RAPORT LIFENODE Q-CORE ---")
print(f"Aktywa: {'BTC-USD'}")
print(f"Okres: {data.index[0].strftime('%Y-%m-%d')} do {data.index[-1].strftime('%Y-%m-%d')}")
print(f"Kapitał początkowy: {start_capital:.2f}$")
print(f"----------------------------------------")
print(f"Portfel LifeNode końcowa wartość: {final_value:.2f}$")
print(f"Zwrot LifeNode: {lifenode_return_percent:.2f}%")
print(f"----------------------------------------")
print(f"Portfel 'Kup i Trzymaj' końcowa wartość: {hold_final_value:.2f}$")
print(f"Zwrot 'Kup i Trzymaj': {hold_return_percent:.2f}%")
print(f"----------------------------------------")

# 5. Wykres dla Twojego dowodu (z sygnałami)
plt.figure(figsize=(14, 8))
plt.plot(data.index[1:], np.array(log_value[1:]) / start_capital, label='Portfel LifeNode (Q-Core)', color='blue', linewidth=2)
plt.plot(data.index, prices / prices[0], label='Rynek (Benchmark)', color='gray', alpha=0.6, linestyle='--')

# Rysowanie sygnałów KUP/SPRZEDAJ na wykresie
for signal_idx in buy_signals:
    if signal_idx < len(data.index):
        plt.plot(data.index[signal_idx], prices[signal_idx] / prices[0], '^', markersize=10, color='green', alpha=0.7, label='Sygnał KUPNA' if signal_idx == buy_signals[0] else "")
for signal_idx in sell_signals:
    if signal_idx < len(data.index):
        plt.plot(data.index[signal_idx], prices[signal_idx] / prices[0], 'v', markersize=10, color='red', alpha=0.7, label='Sygnał SPRZEDAŻY' if signal_idx == sell_signals[0] else "")


plt.title('DOWÓD RYNKOWY: LifeNode Q-Core vs Rynek (BTC-USD)')
plt.xlabel('Data')
plt.ylabel('Wartość portfela (znormalizowana)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
