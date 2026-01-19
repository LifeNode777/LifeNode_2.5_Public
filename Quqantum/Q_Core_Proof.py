import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# 1. Pobieramy realne dane (np. Bitcoin z ostatnich 2 lat)
data = yf.download('BTC-USD', period='2y', interval='1d')
prices = data['Close'].values.flatten()

# Zabezpieczenie
if len(prices) < 3:
    print("Brak wystarczających danych do analizy.")
    exit()

# 2. Silnik Q-CORE
delta = np.abs(np.diff(prices, prepend=prices[0]))
awareness = np.gradient(delta)
curvature = np.gradient(awareness)

# Zwiększona czułość
decisions = np.tanh(-curvature * 50)

# 3. Symulacja zysków (tylko LONG)
capital = 1000.0
position = 0.0
log_value = [capital]
buy_signals = []
sell_signals = []

for i in range(1, len(decisions)):
    current_price = prices[i]
    prev_decision = decisions[i-1]

    # KUPNO
    if prev_decision > 0.5 and position == 0.0:
        position = capital / current_price
        capital = 0.0
        buy_signals.append(i)

    # SPRZEDAŻ
    elif prev_decision < -0.5 and position > 0.0:
        capital = position * current_price
        position = 0.0
        sell_signals.append(i)

    # Wartość portfela
    current_portfolio_value = capital if position == 0.0 else position * current_price
    log_value.append(current_portfolio_value)

# Zamknięcie pozycji na końcu
if position > 0.0:
    final_value = position * prices[-1]
else:
    final_value = capital

# 4. Wyniki
start_capital = 1000.0
hold_final_value = start_capital * (prices[-1] / prices[0])
hold_return_percent = ((hold_final_value / start_capital) - 1) * 100
lifenode_return_percent = ((final_value / start_capital) - 1) * 100

print(f"\n--- RAPORT LIFENODE Q-CORE ---")
print(f"Aktywa: BTC-USD")
print(f"Okres: {data.index[0]} do {data.index[-1]}")
print(f"Portfel LifeNode końcowa wartość: {final_value:.2f}$ (zwrot: {lifenode_return_percent:.2f}%)")
print(f"Portfel 'Kup i Trzymaj': {hold_final_value:.2f}$ (zwrot: {hold_return_percent:.2f}%)")

# 5. Wykres
plt.figure(figsize=(14, 8))
plt.plot(data.index[1:], np.array(log_value[1:]) / start_capital, label='Portfel LifeNode (Q-Core)', color='blue')
plt.plot(data.index, prices / prices[0], label='Rynek (Benchmark)', color='gray', alpha=0.6, linestyle='--')

# Sygnały
for signal_idx in buy_signals:
    if signal_idx < len(data.index):
        plt.plot(data.index[signal_idx], prices[signal_idx] / prices[0], '^', markersize=10, color='green')
for signal_idx in sell_signals:
    if signal_idx < len(data.index):
        plt.plot(data.index[signal_idx], prices[signal_idx] / prices[0], 'v', markersize=10, color='red')

plt.title('DOWÓD RYNKOWY: LifeNode Q-Core vs Rynek (BTC-USD)')
plt.xlabel('Data')
plt.ylabel('Wartość znormalizowana')
plt.legend()
plt.grid(True)
plt.show()
