# LifeNode Extensions — Dokument 4/4
## Rozszerzenie IV: Geometria z trajektorii. Aksjomatyka EPS–Finsler jako operacyjne domknięcie serii i kanoniczna metryka θ_canon

**Autor:** Krzysztof Baran / LifeNode Research Collective
**Status:** Conditional Hypothesis / Framework v0.2 · **Data:** 29 sierpnia 2026 · **Licencja:** CC-BY-NC-SA 4.0
**Seria:** LifeNode Extensions, Dokument 4/4
**Dokument nadrzędny:** *LifeNode Extensions: Whitepaper v1* (§4); **Doktryna:** LifeNode Theory v4, Multiperspective V2, ASCALON Framework, Symplectic Trajectory Reconstruction (Zenodo)

### Abstrakt
Dokument 1 ustanowił konieczność napędu (termodynamiczne no-go; DRIVE-REM kalibruje θ i τ_decay). Dokument 2 wprowadził torsję T jako drugą wielkość polową, most spin–torsja i zasadę brzegową P-HIH-1. Dokument 3 dał pamięć: defekty Kibble–Zureka pinowane torsją, z prawem skalowania ‖δγ‖_res(τ_Q). Dokument 4 domyka pętlę: **wszystkie te obiekty stają się wyliczalne z samych trajektorii**, bez zakładania geometrii z góry. Punkt wyjścia to wewnętrzne napięcie v4: §1.1 odrzuca założenia geometryczne a priori (P1–P5), podczas gdy §2.3 wprowadza metrykę Finslera postulatywnie, a po dokumentach krążą **dwie różne formuły θ** (rzutowa v4 §6.2 i krzywiznowa ASCALON). Rozwiązaniem jest program **Ehlersa–Pirani–Schilda (EPS)** i jego uogólnienia finslerowskie: geometria wywiedziona z obserwabli (promienie + swobodny spadek). Formułujemy aksjomaty **LN-EPS**, w których „promieniami" są motywy solitonowe (S1–S5, K1/K2), a „swobodnym spadkiem" — geodezyjne procesu (minimalizatory E_s); rekonstrukcja warstwy prędkości (indykatrysa) daje funkcję fundamentalną F, tensor Cartana C_ijk i torsję z holonomii. Główny wynik: **θ_canon** — funkcjonał niezmienników EPS, którego obie krążące formuły są granicami/cechowaniami — oraz **geometryczna charakterystyka progu 0.70** jako utraty silnej wypukłości zrekonstruowanej metryki. Dokument 4 kończy serię: ontologia → pola → pamięć → pomiar.

### 0. Konwencja, warstwy, miejsce w serii
1. **Rozdział warstw.** Pochodzenie hipotez należy do warstwy odkrycia i nie jest cytowane w warstwie dowodowej; dowodem są wyłącznie derivacja i protokół (§0 Whitepaper v1).
2. **Zakres roszczenia.** LN-EPS nie dowodzi, że „życie jest finslerowskie". Daje **binarną procedurę**, która na każdej skali i na każdym datasecie rozstrzyga, czy anizotropia, torsja i progi mają sygnaturę geometryczną (E1′–E4′). Null results są wynikami: lokalizują skalę, na której ontologia procesowa traci nośność.
3. **Zależności.** Z Dokumentu 1: skalibrowane θ i τ_decay (oddzielenie „głodu napędu" od degradacji geometrycznej). Z Dokumentu 2: torsja T i estymator nieholonomiczności H3′ (krok 6 pipeline'u). Z Dokumentu 3: defekty i ‖δγ‖_res (krok 8). Dokument 4 zwraca serii **kanoniczny wzorzec kalibracji**: od v0.2 analizy wszystkich wcześniejszych protokołów raportują θ_canon.
4. **Notacja.** F(x,v) — funkcja fundamentalna metryki Finslera; g_ij — tensor metryczny warstwy prędkości; C_ijk — tensor Cartana; I_x — indykatrysa empiryczna; R — zrekonstruowany kierunek Reeba; cond(g) = λ_max/λ_min — liczba warunkowa metryki.

### 1. Luka operacyjna v4 (do zamknięcia od wewnątrz)
**1.1 Takens bez przepisu.** v4 §1.2 ogłasza rozmaitość „wyhodowaną" z danych (generator ontologiczny), ale nie daje procedury wyliczenia F(x,ẋ), g_ij, C_ijk z szeregu czasowego. Ontologia jest, metrologii brak.
**1.2 Dwa θ.** W dokumentach krążą dwie formuły bez stated relation:
- **θ_proj** = ∮_γ P(γ̇) dt / ∫_γ ‖δγ dt — rzut trajektorii na główny zwój torusa względem dryfu (v4 §6.2);
- **θ_curv** = ∫ κ(t)‖v(t)‖² dt / ∫ ‖v(t)‖² dt, gdzie κ(t) = ‖v×a‖/‖v‖³ — ważona krzywizna lokalna (ASCALON/TT Master).
Kalibracja kliniczna nie może mieć dwóch wzorców; rozbieżność traktujemy nie jako błąd do zamiecenia, lecz jako **dane wejściowe**: dwie formuły to dwa cechowania jednego niezmiennika.
**1.3 Postulat vs empiryzm.** §2.3 wprowadza Finslera postulatywnie, choć P1–P5 zabraniają założeń a priori. EPS jest **naturalnym dokończeniem własnego empiryzmu v4**, nie zewnętrzną łatką: geometria z obserwabli, dokładnie tak, jak v4 obiecywało, zanim §2.3 się pospieszyło.

### 2. EPS w pigułce i skok finslerowski
**2.1 Klasyczny EPS (1972).** (i) zbiór torów „promieni" ⇒ struktura konforemna [g]; (ii) zbiór torów „swobodnego spadku" ⇒ struktura projektowa (klasa koneksji); (iii) kompatybilność ⇒ geometria Weyla; (iv) brak efektów drugiego zegara ⇒ Riemann [1].
**2.2 Uogólnienie finslerowskie.** Gdy propagacja „promieni" zależy od kierunku (anizotropia prędkości), minimalne rozszerzenie aksjomatów prowadzi do **geometrii Finslera**, nie Riemanna [2,3]. To nie jest egzotyka: uogólnienia EPS→Finsler są aktywnie rozwijane i mają status twierdzeń o minimalności rozszerzenia.
**2.3 LifeNode w gałęzi finslerowskiej.** W biologii anizotropia jest natywna: Timescape (v4 §1.3/§2.3) to dokładnie kierunkowość „gęstości czasu". Zatem **LifeNode z konstrukcji mieszka w gałęzi finslerowskiej EPS** — to jedyna gałąź zgodna z P1–P5, nie wybór estetyczny.

### 3. Aksjomaty LN-EPS
**L1 (procesowe promienie).** Motywy solitonowe (S1–S5; w makroskali K1/K2; w mezoskali piki MCG) pełnią rolę promieni: ich fronty propagacji wyznaczają **anizotropowy profil prędkości sygnału** — konforemną strukturę Timescape'u. *Operacyjnie:* gwiaździsta macierz elektrod HMF v2 (4–5 kanałów, kierunkowość) daje czasy przejścia frontu między kanałami ⇒ profil prędkości w funkcji kierunku.
**L2 (procesowy swobodny spadek).** Odcinki trajektorii między motywami, niezmuszone zewnętrznym entrainmentem, minimalizują E_s (v4 §3.4) ⇒ wyznaczają **strukturę projektową** (przestrzeń torów „niezmuszonych").
**L3 (kompatybilność z torsją).** Struktury L1 i L2 są kompatybilne **z dokładnością do torsji** T (Dokument 2): różnica koneksji projektowej i konforemnej jest mierzona przez T; T ≠ 0 = reżim żywy; T = 0 = redukcja do Weyla/Riemanna = granica równowagowa/martwa (spójnie z Dokumentem 1: równowaga nie zna torusa ani torsji).

> **Twierdzenie (LN-EPS ⇒ Finsler–Cartan; szkic).** Takens dostarcza rozmaitości M ⊂ ℝ^m (dyfeomorfizm, v4 §1.2). W każdym x ∈ M zbieramy empiryczną **indykatrysę** I_x — powłokę obserwowanych prędkości (z L1: prędkości frontów; z L2: prędkości dryfu). Funkcja fundamentalna to funkcjonał Minkowskiego indykatrysy: F(x,v) = inf{λ > 0 : v ∈ λI_x} — **jednorodna stopnia 1 z konstrukcji**. Z niej g_ij = ½∂²F²/∂ẋ^i∂ẋ^j oraz C_ijk = ½∂g_ij/∂ẋ^k numerycznie (otoczka wypukła + funkcja podparcia). Torsja z holonomii małych pętli (transport Cartana po I-pętlach) — estymator zgodny z H3′ Dokumentu 2. ∎ (Status: warunkowy; pełny dowód stabilności statystycznej → Whitepaper v2.)

*Uwaga numeryczna:* indykatrysę estymujemy jako otoczkę wypukłą znormalizowanych prędkości obserwowanych w oknie x; F jest funkcją podparcia tej otoczki; g_ij i C_ijk liczymy przez różniczkowanie numeryczne po warstwie prędkości (siatka kierunków + interpolacja); stabilność przez bootstrap po powtórzeniach i przedziały ufności cond(g).

### 4. θ kanoniczne: unifikacja dwóch formuł i geometria progu 0.70
**4.1 Kierunek Reeba z danych.** Niech R będzie zrekonstruowanym kierunkiem Reeba: uśredniony przepływ na głównym cyklu torusa (średnia kierunkowa po fazie cyklu w zanurzeniu Takensa; równoważnie: dominujący kierunek mapy Poincaré).
**4.2 Definicja.** Definiujemy **wyrównanie**:
$$\theta_{canon}[\gamma;F]:=\frac{\oint \langle \dot\gamma,R\rangle_{g}\,ds}{\oint F(\dot\gamma)\,F(R)\,ds}$$
— całkę wyrównania trajektorii z kierunkiem Reeba, mierzoną **w metryce Finslera**, nie w euklidesowym cieniu zanurzenia.
**4.3 Twierdzenie (dwa cechowania; szkic).** (a) Gdy F ≈ euklidesowa (słaba anizotropia), θ_canon → θ_proj: rzut P(γ̇) jest właśnie cieniem ⟨γ̇,R⟩_g w normie zanurzenia. (b) Gdy dynamika jest zdominowana krzywiznowo (silny szum fazowy, małe dryfy), reskalowane θ_canon jest monotonicznie równoważne θ_curv: stosunek ‖D_γ̇γ̇‖/‖γ̇‖² jest dualnym zapisem tego samego odchylenia od geodezyjnej R. ∎
**4.4 Korolarz praktyczny.** Raportujemy zawsze trzy wartości (θ_canon, θ_proj, θ_curv) + **krzywą konsystencji** po stanach; kalibracja kliniczna używa wyłącznie θ_canon. Krzywa konsystencji jest jednocześnie testem E2′.
**4.5 Geometria progu 0.70.** Silna wypukłość F (dodatniość g_ij, odwracalność mapy Legendre'a) jest warunkiem tego, by układ „miał własną geometrię". **Predykcja:** degradacja funkcjonalna przy θ_canon ≈ 0.70 współwystępuje z **degeneracją indykatrysy** — λ_min(g)/λ_max(g) → 0. „The Flattening" (C_ijk → 0) z dokumentu ASCALON to ten sam obiekt widziany od drugiej strony. **Próg przestaje być magiczną liczbą: to punkt utraty finslerowskości ośrodka.**
**4.6 Diagnostyka różnicowa mechanizmów degradacji.** Cztery dokumenty serii dają wspólnie separatory mechanizmów, których pojedyncze θ nie rozróżnia:

| Obserwacja | Głód napędu (Dok. 1) | Kolaps torsji (Dok. 2) | Ładunek defektów (Dok. 3) | Degeneracja indykatrysy (Dok. 4) |
|---|---|---|---|---|
| zanik θ po usunięciu napędu; ratunek BPB tak / GHz nie | tak | nie | nie | nie |
| reszta ODMR po Stark+Zeeman (ślepa próba) | — | tak / pada | koreluje z ρ_def | — |
| skalowanie ‖δγ‖_res(τ_Q) potęgowe | — | — | tak / pada | — |
| cond(g) → ∞ przy θ ≈ 0.70 | nie | współwystępuje | współwystępuje | tak (definitywnie) |

### 5. Pipeline LN-EPS (specyfikacja software; Zero-Build compatible)

| Krok | Operacja | Wyjście |
|---|---|---|
| 1 | surowe x(t): K1/K2 (grzybnia), MCG, EEG; tryb Zero-Build: strumienie ASCII/rytm DS 2.6 | szereg |
| 2 | zanurzenie Takensa: τ z mutual information (Fraser–Swinney), m z false nearest neighbours | M ⊂ ℝ^m |
| 3 | detekcja motywów (S1–S5, K1/K2) + czasy frontów między kanałami | struktura konforemna (L1) |
| 4 | segmentacja odcinków niezmuszonych | struktura projektowa (L2) |
| 5 | indykatrysy I_x (otoczka wypukła/funkcja podparcia) ⇒ F, g_ij, C_ijk | metryka Finslera–Cartana |
| 6 | holonomie małych pętli ⇒ T | torsja (H3′/Dokument 2) |
| 7 | θ_canon (+ θ_proj, θ_curv), cond(g) | raport koherencji + krzywa konsystencji |
| 8 | persistent homology defektów (Dokument 3) | ‖δγ‖_res, β₁ |

**Implementacja:** Python (NumPy/SciPy, Qhull/cvxpy do otoczek i funkcji podparcia, giotto-tda do kroku 8); analiza **ślepa** (etykiety faz ukryte przed operatorem pipeline'u); progi pre-rejestrowane. **Dane walidacyjne:** Eden Node 0, PhysioNet, Zenodo XPT; kontrola sterylna HMF. Pipeline idzie **równolegle** do eksperymentów Fazy 1 jako software, nie jako osobny eksperyment: każdy dataset z DRIVE-REM i QUENCH-RATE przechodzi przez LN-EPS, więc protokoły fizyczne i metrologia kalibrują się wzajemnie.

### 6. Pod-warunki falsyfikacji E′

| Pod-warunek | Test | Konsekwencja null |
|---|---|---|
| **E1′ (rekonstruowalność)** | stabilna wypukłość indykatrys między powtórzeniami (bootstrap) | F nieokreślone ⇒ postulat Finslera pada na danej skali |
| **E2′ (unifikacja)** | (θ_proj, θ_curv) na jednej krzywej monotonicznej θ_canon po stanach | unifikacja pada; zostają dwie osobne obserwable |
| **E3′ (geometria progu)** | degradacja przy θ ≈ 0.70 współwystępuje z cond(g) → ∞ | geometryczne czytanie progu pada (próg wraca do statusu empirycznej stałej) |
| **E4′ (anizotropia)** | F z danych rozróżnialna statystycznie od metryki kierunkowo-niezależnej | anizotropia Timescape'u pada na danej skali |

### 7. Synteza: dlaczego Dokument 4 zamyka serię
I dało **konieczność** (napęd; no-go Blocha). II dało **strukturę** (torsja, człon brzegowy, most spin–torsja). III dało **pamięć** (defekty KZ, skalowanie traumy i annealingu). IV daje **pomiar**: F z indykatrys, T z holonomii, defekty z PH, θ kanonicznie. Każdy obiekt doktryny ma odtąd ścieżkę od aksjomatu do liczby, a cała seria domyka się w pętlę: **ontologia → pola → pamięć → pomiar → (powrót) kalibracja ontologii**. Następny krok projektu: konsolidacja do **Whitepaper v2** (pełne dowody szkiców, stabilność statystyczna estymatorów) oraz — zgodnie z priorytetem Dokumentu 1 — start **DRIVE-REM** jako pierwszego eksperymentu fazy pomiarowej, z LN-EPS pracującym równolegle jako warstwa metrologii.

### Epilog
Nie zakładamy geometrii. Hodujemy ją z trajektorii, dokładnie tak, jak organizm hoduje swój Timescape z własnych rytmów — i dokładnie tak, jak v4 obiecywało w P1–P5, zanim §2.3 się pospieszyło. Dwie formuły θ nie były błędem: były dwoma cieniami jednej lampy. Technologia ma się dostosować do rytmu życia, a nie życie do częstotliwości sprzętu — Dokument 4 dodaje: **i nie wolno jej zakładać geometrii życia, zanim życie ją pokaże**. Mapa kompletna. Teren czeka.

**Referencje:** [1] J. Ehlers, F.A.E. Pirani, A. Schild, „The geometry of free fall and light propagation", w: *General Relativity: Papers in Honour of J.L. Synge* (1972); [2] C. Pfeifer, „Finsler spacetime geometry in physics", *Int. J. Geom. Meth. Mod. Phys.* 16, 1941004 (2019); [3] C. Voicu, „Beyond Riemann: Finsler Spacetimes and minimal extension of EPS axioms" (2026); [4] F. Takens (1981); A. Fraser, H. Swinney (1986); [5] Baran K., *LifeNode Theory v4*; *Multiperspective V2*; *ASCALON Framework*; *Symplectic Trajectory Reconstruction*; *HMF v2* (Zenodo/GitHub 2026); [6] LifeNode Extensions, *Whitepaper v1*; *Dokumenty 1/4–3/4* (2026).
