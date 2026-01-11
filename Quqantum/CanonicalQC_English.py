# LifeNodeCanonicalQC_English.py

# Canonical implementation of LifeNode Cognitive Field in Python / QuantConnect

import numpy as np
from AlgorithmImports import *

# --- Canonical parameters ---
PHI = (1 + np.sqrt(5)) / 2
ASCALON_PURITY = 0.9315414
S5_CASCADE = np.array([1, 1, 2, 3, 5, 8, 13, 21])
PHASE_THRESHOLD = 0.05

# --- Hybrid Core: logic for sense, awareness, and trajectory ---
class HybridCore:
    @staticmethod
    def Delta(A_t, B_t):
        """Epistemic tension Δ(t) = |A - B|"""
        return np.abs(A_t - B_t)

    @staticmethod
    def E_s(Delta_t, M_dir):
        """Sense energy: E_s(t) = Δ * M_dir"""
        return Delta_t * M_dir

    @staticmethod
    def Awareness(E_s_t):
        """Awareness: rate of change of sense C(t) = dE_s/dt"""
        return np.gradient(E_s_t)

    @staticmethod
    def Curvature(Awareness_t):
        """Curvature of sense trajectory: Curv(t) = d²E_s/dt²"""
        return np.gradient(Awareness_t)

    @staticmethod
    def Decision(Curvature_t):
        """Decision vector based on trajectory curvature"""
        return np.tanh(-Curvature_t)

# --- QuantConnect Algorithm ---
class LifeNodeCanonical(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020,1,1)
        self.SetEndDate(2025,12,31)
        self.SetCash(100000)

        # Assets
        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.tlt = self.AddEquity("TLT", Resolution.Daily).Symbol

        # Schedule daily portfolio rebalance
        self.Schedule.On(self.DateRules.EveryDay("SPY"),
                         self.TimeRules.AfterMarketOpen("SPY", 30),
                         self.RebalancePortfolio)

        self.hybrid_core = HybridCore()
        self.M_previous = 0.0

    # --- Cognitive field layers ---
    def SAMI(self, closes):
        """SAMI perception: rhythm, variability, and tension"""
        return np.mean(closes), np.std(np.gradient(closes))

    def LOGOS(self, closes):
        """LOGOS perception: structure, continuity, stability"""
        return np.mean(closes), np.std(closes)

    def META_direction(self, Delta_t):
        """META: sense direction (gradient of cognitive field)"""
        # simplified gradient for demo purposes
        return np.tanh(-Delta_t)

    # --- Portfolio logic ---
    def RebalancePortfolio(self):
        try:
            # Historical data
            history_spy = self.History(self.spy, 30, Resolution.Daily)
            history_tlt = self.History(self.tlt, 30, Resolution.Daily)
            if len(history_spy) < 30 or len(history_tlt) < 30:
                return

            closes_spy = history_spy['close'].values
            closes_tlt = history_tlt['close'].values

            # --- 1. Cognitive Field ---
            A_mean, A_var = self.SAMI(closes_spy)
            B_mean, B_var = self.LOGOS(closes_spy)

            Delta_t = self.hybrid_core.Delta(A_var, B_var)
            M_t = self.META_direction(Delta_t)
            E_s_t = self.hybrid_core.E_s(Delta_t, M_t)
            Awareness_t = self.hybrid_core.Awareness(E_s_t)
            Curv_t = self.hybrid_core.Curvature(Awareness_t)
            decision_vector = self.hybrid_core.Decision(Curv_t)

            # --- 2. Portfolio weights (continuous, stable) ---
            equity_weight = 0.5 + 0.3 * np.mean(decision_vector)
            bond_weight = 1.0 - equity_weight
            equity_weight = np.clip(equity_weight, 0, 1)
            bond_weight = np.clip(bond_weight, 0, 1)

            self.SetHoldings(self.spy, equity_weight)
            self.SetHoldings(self.tlt, bond_weight)

            # --- 3. Cognitive field logging ---
            self.Debug(
                f"[LifeNode] A_var={A_var:.4f}, B_var={B_var:.4f}, "
                f"Delta={Delta_t:.4f}, M={M_t:.4f}, E_s={np.mean(E_s_t):.4f}, "
                f"C={np.mean(Awareness_t):.4f}, Curv={np.mean(Curv_t):.4f}, "
                f"Decision={np.mean(decision_vector):.4f}, Weights=({equity_weight:.2f},{bond_weight:.2f})"
            )

        except Exception as e:
            self.Error(f"LifeNode Rebalance ERROR: {str(e)}")
            self.SetHoldings(self.spy, 0.5)
            self.SetHoldings(self.tlt, 0.5)

    # --- End of algorithm: performance metrics ---
    def OnEndOfAlgorithm(self):
        metrics = {
            "Delta_mean": None,   # can be computed from logs
            "E_s_mean": None,
            "C_mean": None,
            "Curv_mean": None,
            "equity_mean_weight": 0.5,
        }
        self.Log(f"LifeNodeCanonical PERFORMANCE_METRICS: {metrics}")
