# LifeNode Enhanced - Poprawiona implementacja z kontrolą ryzyka i optymalizacją
# Wersja dla QuantConnect

import numpy as np
from AlgorithmImports import *
from collections import deque

# --- Parametry kanoniczne ---
PHI = (1 + np.sqrt(5)) / 2
ASCALON_PURITY = 0.9315414
S5_CASCADE = np.array([1, 1, 2, 3, 5, 8, 13, 21])
PHASE_THRESHOLD = 0.05

# --- Ulepszony Hybrid Core ---
class HybridCoreEnhanced:
    """Poprawiona implementacja z obsługą szeregów czasowych"""
    
    @staticmethod
    def Delta(A_series, B_series):
        """Napięcie epistemiczne - obliczone na szeregach czasowych"""
        return np.abs(A_series - B_series)
    
    @staticmethod
    def E_s(Delta_series, M_series):
        """Energia zmysłowa: E_s(t) = Δ(t) * M(t)"""
        return Delta_series * M_series
    
    @staticmethod
    def Awareness(E_s_series):
        """Świadomość: C(t) = dE_s/dt"""
        if len(E_s_series) < 2:
            return np.array([0.0])
        return np.gradient(E_s_series)
    
    @staticmethod
    def Curvature(Awareness_series):
        """Krzywizna: Curv(t) = d²E_s/dt²"""
        if len(Awareness_series) < 2:
            return np.array([0.0])
        return np.gradient(Awareness_series)
    
    @staticmethod
    def Decision(Curvature_series):
        """Wektor decyzyjny z krzywizny"""
        return np.tanh(-Curvature_series)

# --- Zarządzanie ryzykiem ---
class RiskManager:
    def __init__(self, max_drawdown=0.15, volatility_target=0.12, max_leverage=1.0):
        self.max_drawdown = max_drawdown
        self.volatility_target = volatility_target
        self.max_leverage = max_leverage
        self.peak_portfolio_value = 0
        
    def UpdatePeak(self, current_value):
        """Aktualizuj szczyt wartości portfela"""
        self.peak_portfolio_value = max(self.peak_portfolio_value, current_value)
    
    def GetDrawdown(self, current_value):
        """Oblicz bieżący drawdown"""
        if self.peak_portfolio_value == 0:
            return 0
        return (self.peak_portfolio_value - current_value) / self.peak_portfolio_value
    
    def ShouldReduceRisk(self, current_value):
        """Czy należy zredukować ekspozycję?"""
        return self.GetDrawdown(current_value) > self.max_drawdown * 0.7
    
    def AdjustForVolatility(self, weights, realized_vol):
        """Dostosuj wagi do docelowej zmienności"""
        if realized_vol <= 0:
            return weights
        
        vol_scalar = min(self.volatility_target / realized_vol, self.max_leverage)
        adjusted = {k: v * vol_scalar for k, v in weights.items()}
        
        # Normalizuj do 100%
        total = sum(adjusted.values())
        if total > 0:
            adjusted = {k: v / total for k, v in adjusted.items()}
        
        return adjusted

# --- Główny algorytm ---
class LifeNodeEnhanced(QCAlgorithm):
    
    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2025, 12, 31)
        self.SetCash(100000)
        
        # Aktywa
        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.tlt = self.AddEquity("TLT", Resolution.Daily).Symbol
        
        # Parametry
        self.lookback_period = 60  # Zwiększone z 30 do 60 dni
        self.rebalance_days = 5    # Rebalans co 5 dni zamiast codziennie
        self.days_since_rebalance = 0
        
        # Komponenty
        self.hybrid_core = HybridCoreEnhanced()
        self.risk_manager = RiskManager(
            max_drawdown=0.15,
            volatility_target=0.12,
            max_leverage=1.0
        )
        
        # Historia metryk
        self.metrics_history = {
            'Delta': deque(maxlen=252),
            'E_s': deque(maxlen=252),
            'Awareness': deque(maxlen=252),
            'Curvature': deque(maxlen=252),
            'Decision': deque(maxlen=252),
            'equity_weight': deque(maxlen=252),
            'portfolio_value': deque(maxlen=252),
        }
        
        # Harmonogram
        self.Schedule.On(
            self.DateRules.EveryDay("SPY"),
            self.TimeRules.AfterMarketOpen("SPY", 30),
            self.DailyUpdate
        )
        
        # Warm-up
        self.SetWarmUp(self.lookback_period + 10)
    
    # --- Warstwy percepcji (ulepszone) ---
    def SAMI(self, closes):
        """SAMI: rytm, zmienność, napięcie (szereg czasowy)"""
        rhythm = np.gradient(closes)
        variability = np.std(rhythm)
        return rhythm, variability
    
    def LOGOS(self, closes):
        """LOGOS: struktura, ciągłość, stabilność (szereg czasowy)"""
        structure = closes - np.mean(closes)
        stability = np.std(closes)
        return structure, stability
    
    def META_direction(self, Delta_series):
        """META: kierunek zmysłu (gradient pola kognitywnego)"""
        if len(Delta_series) < 2:
            return np.array([0.0])
        return np.tanh(-np.gradient(Delta_series))
    
    # --- Logika codzienna ---
    def DailyUpdate(self):
        if self.IsWarmingUp:
            return
        
        # Aktualizuj metryki ryzyka
        portfolio_value = self.Portfolio.TotalPortfolioValue
        self.risk_manager.UpdatePeak(portfolio_value)
        self.metrics_history['portfolio_value'].append(portfolio_value)
        
        # Rebalansuj tylko co N dni
        self.days_since_rebalance += 1
        if self.days_since_rebalance >= self.rebalance_days:
            self.RebalancePortfolio()
            self.days_since_rebalance = 0
    
    # --- Rebalansowanie portfela ---
    def RebalancePortfolio(self):
        try:
            # Pobierz dane historyczne
            history_spy = self.History(self.spy, self.lookback_period, Resolution.Daily)
            history_tlt = self.History(self.tlt, self.lookback_period, Resolution.Daily)
            
            if len(history_spy) < self.lookback_period or len(history_tlt) < self.lookback_period:
                return
            
            closes_spy = history_spy['close'].values
            closes_tlt = history_tlt['close'].values
            
            # --- 1. Pole kognitywne (na szeregach czasowych) ---
            rhythm_spy, variability_spy = self.SAMI(closes_spy)
            structure_spy, stability_spy = self.LOGOS(closes_spy)
            
            # Delta jako szereg czasowy - porównanie zmienności vs stabilności
            Delta_series = self.hybrid_core.Delta(
                np.full(len(closes_spy), variability_spy),
                np.full(len(closes_spy), stability_spy)
            )
            
            # META kierunek
            M_series = self.META_direction(Delta_series)
            
            # Energia zmysłowa, świadomość, krzywizna
            E_s_series = self.hybrid_core.E_s(Delta_series, M_series)
            Awareness_series = self.hybrid_core.Awareness(E_s_series)
            Curvature_series = self.hybrid_core.Curvature(Awareness_series)
            Decision_series = self.hybrid_core.Decision(Curvature_series)
            
            # Użyj ostatnich wartości do decyzji
            current_decision = Decision_series[-1]
            
            # --- 2. Wagi portfela (bazowe) ---
            equity_weight = 0.5 + 0.3 * current_decision
            equity_weight = np.clip(equity_weight, 0.2, 0.8)  # Limity 20-80%
            bond_weight = 1.0 - equity_weight
            
            weights = {
                self.spy: equity_weight,
                self.tlt: bond_weight
            }
            
            # --- 3. Dostosowanie do zmienności ---
            returns_spy = np.diff(closes_spy) / closes_spy[:-1]
            realized_vol = np.std(returns_spy) * np.sqrt(252)
            weights = self.risk_manager.AdjustForVolatility(weights, realized_vol)
            
            # --- 4. Kontrola drawdownu ---
            portfolio_value = self.Portfolio.TotalPortfolioValue
            if self.risk_manager.ShouldReduceRisk(portfolio_value):
                # Zwiększ obligacje w czasie drawdownu
                weights[self.spy] *= 0.7
                weights[self.tlt] = 1.0 - weights[self.spy]
                self.Debug(f"[RISK] Drawdown detected: {self.risk_manager.GetDrawdown(portfolio_value):.2%}")
            
            # --- 5. Wykonaj transakcje ---
            self.SetHoldings(self.spy, weights[self.spy])
            self.SetHoldings(self.tlt, weights[self.tlt])
            
            # --- 6. Zapisz metryki ---
            self.metrics_history['Delta'].append(Delta_series[-1])
            self.metrics_history['E_s'].append(E_s_series[-1])
            self.metrics_history['Awareness'].append(Awareness_series[-1])
            self.metrics_history['Curvature'].append(Curvature_series[-1])
            self.metrics_history['Decision'].append(current_decision)
            self.metrics_history['equity_weight'].append(weights[self.spy])
            
            # Log
            self.Debug(
                f"[LifeNode] Δ={Delta_series[-1]:.4f} | E_s={E_s_series[-1]:.4f} | "
                f"C={Awareness_series[-1]:.4f} | Curv={Curvature_series[-1]:.4f} | "
                f"Dec={current_decision:.4f} | Weights=SPY:{weights[self.spy]:.2%} TLT:{weights[self.tlt]:.2%} | "
                f"Vol={realized_vol:.2%} | DD={self.risk_manager.GetDrawdown(portfolio_value):.2%}"
            )
            
        except Exception as e:
            self.Error(f"[LifeNode] ERROR: {str(e)}")
            # Awaryjne 60/40
            self.SetHoldings(self.spy, 0.6)
            self.SetHoldings(self.tlt, 0.4)
    
    # --- Koniec algorytmu ---
    def OnEndOfAlgorithm(self):
        """Podsumowanie wydajności"""
        if len(self.metrics_history['Decision']) == 0:
            self.Log("[LifeNode] Brak danych do analizy")
            return
        
        # Oblicz statystyki
        metrics = {
            "Delta_mean": np.mean(self.metrics_history['Delta']),
            "Delta_std": np.std(self.metrics_history['Delta']),
            "E_s_mean": np.mean(self.metrics_history['E_s']),
            "Awareness_mean": np.mean(self.metrics_history['Awareness']),
            "Curvature_mean": np.mean(self.metrics_history['Curvature']),
            "Decision_mean": np.mean(self.metrics_history['Decision']),
            "equity_weight_mean": np.mean(self.metrics_history['equity_weight']),
            "equity_weight_std": np.std(self.metrics_history['equity_weight']),
            "max_drawdown": max([self.risk_manager.GetDrawdown(v) 
                                 for v in self.metrics_history['portfolio_value']]),
            "final_value": self.Portfolio.TotalPortfolioValue,
            "total_return": (self.Portfolio.TotalPortfolioValue / 100000 - 1) * 100
        }
        
        self.Log("="*60)
        self.Log("[LifeNode Enhanced] METRYKI WYDAJNOŚCI")
        self.Log("="*60)
        for key, value in metrics.items():
            if isinstance(value, float):
                self.Log(f"{key}: {value:.4f}")
            else:
                self.Log(f"{key}: {value}")
        self.Log("="*60)
