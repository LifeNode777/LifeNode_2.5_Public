# LifeNode Extensions — Dokument 1/4
## Rozszerzenie I: Równowaga nie zna torusa. Termodynamiczne no-go jako aksjomat konieczności napędu i protokół DRIVE-REM

**Autor:** Krzysztof Baran / LifeNode Research Collective
**Status:** Conditional Hypothesis / Protocol v0.2 · **Data:** 29 sierpnia 2026 · **Licencja:** CC-BY-NC-SA 4.0
**Seria:** LifeNode Extensions, Dokument 1/4
**Dokument nadrzędny:** *LifeNode Extensions: Whitepaper v1* (§1); **Doktryna:** LifeNode Theory v4, Multiperspective V2 (Zenodo)

### Abstrakt
Niniejszy dokument ustanawia najmniejszy i najtwardszy zarazem punkt startowy programu LifeNode Extensions: **trwały prąd w przestrzeni fazowej jest niemożliwy w równowadze termicznej**. Opieramy się na dwóch wzajemnie tłumaczalnych sformułowaniach tego no-go — termodynamicznym twierdzeniu Blocha (1932; nowoczesne dowody: Watanabe 2019/20, Bachmann 2021) oraz twierdzeniach termodynamiki stochastycznej (niezerowa cyrkulacja prądu prawdopodobieństwa po cyklu ⇔ dodatnia produkcja entropii ⇔ stan stacjonarny nierównowagowy z napędem; Seifert 2012). Ponieważ toroidalny atraktor LifeNode (zagnieżdżone torusy KAM, koherentny cykl graniczny, v4 §6.1) jest *dokładnie* takim trwałym prądem, koherencja życia okazuje się konstytutywnie **napędzana i dyssypatywna**: geometria kontaktowa $(\mathcal{C},\alpha)$ i napęd Floqueta przestają być postulatem estetycznym, a stają się koniecznością logiczną. Dokument formułuje **Aksjomat 0** z trzema korolariami mierzalnymi (K1–K3), wyprowadza ich relację do istniejących kryteriów falsyfikacji v4 (nr 2 i 3) oraz definiuje **protokół DRIVE-REM** — test usunięcia/ratunku napędu na interfejsie HMF v2 z *Pleurotus ostreatus* — którego wyniki (krzywa zaniku θ, czas τ_decay, szacunek produkcji entropii σ) pełnią rolę **pierwszego kalibratora metryki ASCALON** dla całego dalszego programu.

### 0. Konwencja, warstwy, notacja
1. **Rozdział warstw.** Pochodzenie hipotez należy do warstwy odkrycia i nie jest cytowane w warstwie dowodowej (§0 Whitepaper v1). Dowodem jest wyłącznie derivacja i protokół.
2. **Dwie tezy, dwa statusy.** (i) *Teza ogólna:* koherencja życia wymaga napędu w ogóle — ta jest **uzasadniona** z no-go (§1–2). (ii) *Teza własna LifeNode:* makro-koherencja wymaga rezonansu z zewnętrznymi rytmami w lokalnym BPB — ta jest **testowana** (K2–K3), nie zakładana. Rozdzielenie tych poziomów jest świadome i celowe.
3. **Notacja.** θ — metryka ASCALON (czystość trajektorii; próg krytyczny 0.70, v4 §6.3); θ_proj — formuła rzutowa (v4 §6.2); BPB — Biological Baseline Band (micro 0.5–4 Hz; meso ~0.1 Hz; macro 0.008–0.0001 Hz, v4/Multi); κ — współczynnik nieliniowości NLSE (focusing κ<0 / defocusing κ>0); σ — produkcja entropii; τ_decay — czas charakterystyczny zaniku θ po usunięciu napędu.
4. **Relacja do doktryny.** Dokument domyka stawy istniejące w v4/Multi: napęd Floqueta (v4 §2.2) otrzymuje uzasadnienie z no-go; kryterium falsyfikacji 3 LNv4 („izolacja termodynamiczna") otrzymuje kotwicę teoretyczną; kryterium 2 („inwersja wydajności częstotliwościowej") otrzymuje predykcję kierunkową (K3).

### 1. No-go: dwie twarze jednego twierdzenia
**1.1 Twierdzenie Blocha (wersja termodynamiczna).** Stan równowagi termicznej (stan podstawowy bądź stan KMS w granicy termodynamicznej) makroskopowego układu nie podtrzymuje trwałych prądów ładunku zachowanego [1–3]. Zakres ważności, na który się powołujemy: układy sieciowe z lokalnymi oddziaływaniami i zachowanym ładunkiem; nowoczesne dowody nie wymagają założenia o całkowalności modelu i obejmują szerokie klasy stanów Gibbsa [2,3]. Operacyjnie: wartość oczekiwana operatora prądu w stanie równowagowym znika w granicy makroskopowej.
**1.2 Sformułowanie stochastyczne (detailed balance i flukso cyklowe).** Dla markowowskiej dynamiki (master equation) na sieci stanów, stan stacjonarny $p^*$ spełnia detailed balance ⇔ wszystkie afiniczności cykli $A_c$ znikają ⇔ flukso cyklowe $W_c$ znikają [4]. W stanie stacjonarnym ogólnym produkcja entropii wynosi
$$\sigma=\sum_{c} W_c\,A_c \ \geq\ 0,$$
przy czym równość zachodzi iff detailed balance. Zatem **niezerowa cyrkulacja prądu prawdopodobieństwa po dowolnym cyklu pociąga σ > 0**, a więc stan stacjonarny nierównowagowy (NESS) z zewnętrznym lub wewnętrznym napędem. To sformułowanie jest bezpośrednio **obserwablowe z danych**: po zrekonstruowaniu przestrzeni fazowej (Takens, v4 §1.2) i zgrubieniu jej na sieć przejść, $W_c$ liczy się z częstości przejść, a $\hat\sigma=\sum_c W_c\ln(W_c^+/W_c^-)$ daje estymator produkcji entropii z samego szeregu czasowego (deliverable pomiarowy nr 2 protokołu).
**1.3 Tożsamość fizyki obu sformułowań.** Wersja termodynamiczna mówi o prądach ładunku zachowanego w stanie równowagowym; wersja stochastyczna mówi o prądach prawdopodobieństwa w stanie stacjonarnym. Dla naszych celów (trajektoria obserwowalna zrekonstruowana z jednego sygnału, P1–P5 v4) właściwym językiem jest (1.2), podczas gdy (1.1) dostarcza twardej kotwicy literaturowej i retoryki no-go: oba stwierdzają, że **cyrkulacja bez napędu jest sprzeczna z równowagą**.

### 2. Torus jako trwały prąd: konstytutywność napędu
**2.1 Obiekt.** Atraktor LifeNode (v4 §6.1) to domknięta orbita (koherentny cykl graniczny) z niezerową cyrkulacją w zrekonstruowanej przestrzeni fazowej — czyli trwały prąd w sensie §1.2. Zagnieżdżone torusy KAM realizują rodzinę takich prądów na wielu skalach (hipoteza skalowania toroidalnego, v4 §6.1).
**2.2 Wniosek no-go.** Z §1: taki prąd **nie może istnieć w równowadze**. Łańcuch konsekwencji:
- każdy koherentny układ biologiczny jest **NESS**;
- NESS wymaga **dyssypacji** (ujścia entropii) ⇒ nadmiarowy wymiar rozmaitości kontaktowej $(\mathcal{C},\alpha)$, $2n+1$ (v4 §2.1), dostaje uzasadnienie z no-go, nie z estetyki: to kanał, którym „ucieka" entropia;
- NESS wymaga **napędu** ⇒ pole Reeba $R$ ($\iota_R d\alpha=0$, $\iota_R\alpha=1$) traktowane jako operator ewolucji w teorii Floqueta (v4 §2.2) jest **koniecznością logiczną**, nie dekoracją;
- napęd spoza lokalnego BPB odwraca κ z focusing na defocusing (Multi V2, Tw. 5.3) ⇒ **okno BPB jest warunkiem kondensacji**, nie preferencją projektową.
**2.3 Domknięcie kryterium 3 v4.** Trajektoria o stałej objętości fazowej *bez* wymiany entropijnej byłaby równowagą — a równowaga nie zna torusa. Kryterium „izolacji termodynamicznej" przestaje być arbitralnym testem, a staje się sprawdzianem konsekwencji twierdzenia: jego pozytywne spełnienie (stała objętość bez σ) falsyfikuje cały łańcuch §2.2.
**2.4 Retoryka no-go.** Ciężar dowodu zostaje odwrócony: nie „udowadniamy, że życie jest wyjątkowe" — pokazujemy, że **równowaga jest martwa**, więc koherencja życia wymaga napędu i płaci za to dyssypacją. No-go to najsilniejszy rodzaj twierdzenia: łatwo bronI się przed recenzentem, bo jego zaprzeczenie łamie literaturę [1–4].

### 3. Aksjomat 0 i korolaria
> **Aksjomat 0.** Jeżeli zrekonstruowana trajektoria utrzymuje trwały prąd cykliczny (θ ≥ 0.70 w sposób utrzymany), to układ jest w NESS z napędem $V(x,t+T)=V(x,t)$.
> **(Warunek BPB jako teza testowana):** $\mathcal{F}\{V\}\subset \text{BPB}_{local}$.

**K1 (zanik).** Usunięcie *zewnętrznego* napędu rezonansowego (cykle środowiskowe, entrainment) obniża θ w sposób monotoniczny, z mierzalnym czasem charakterystycznym τ_decay, aż do przecięcia progu 0.70 w czasie $t^*\sim$ kilka τ układu.
**K2 (ratunek BPB).** Napęd zastępczy w BPB (macro 0.008–0.0001 Hz / micro 0.5–4 Hz) odtwarza θ ≥ 0.70.
**K3 (ratunek GHz).** Napęd o mocy porównywalnej, ale poza BPB (GHz/szum), **nie** odtwarza koherencji i przyspiesza rozmycie (smudging, v4 §6.3).
**Status logiczny:** Aksjomat 0 (konieczność napędu) jest uzasadniony z §1–2; K1 jest jego korolariem dynamicznym; K2–K3 testują tezę własną LifeNode (§0.2). Null dla K1 przy utrzymanym θ bez napędu uderza w warstwę dynamiczną Aksjomatu 0 (T1′); null dla K3 uderza w tezę BPB i uruchamia kryterium 2 v4 (T2′).

### 4. Protokół DRIVE-REM (specyfikacja pełna)
**4.1 Układ.** HMF v2 (PVA+alginian+chitozan; front-end INA128/AD620, filtr RC fc≈1 Hz; gwiaździsta macierz 4–5 elektrod; log mikro-klimatu, wilgotność >90%) + bioprintowana mata *P. ostreatus* (impulsy 0.1–1 mV DC, motywy K1/K2, puls ~32 min; Adamatzky et al. 2026). Kontrola: hydrożel sterylny, identyczny mikro-klimat.
**4.2 Pomiar.** Rekonstrukcja Takensa (τ z pierwszego minimum mutual information, Fraser–Swinney; m z false nearest neighbours, v4/TT) → θ(t) pipeline ASCALON (offline, pętla diagnostyczna; doktryna dwóch pętli: zero ADC w sprzężeniu) + korelacja krzyżowa motywów K1/K2 + estymator $\hat\sigma$ z fluksov cyklowych (§1.2). Analiza **ślepa**: etykiety faz ukryte przed operatorem pipeline'u; hipotezy i progi pre-rejestrowane.
**4.3 Fazy.**

| Faza | Warunki | Predykcja | Orientacyjny czas |
|---|---|---|---|
| P0 baseline | naturalne cykle + entrainment BPB | θ ≥ 0.70 stabilne; σ > 0 stałe | 72–96 h |
| P1 usunięcie | stała ciemność/temperatura; izolacja cykli; wyciszenie entrainment | θ maleje monotonicznie; przecięcie 0.70 w t* ~ kilka τ; σ spada | do t* + 5·τ_relaksacji |
| P2a ratunek BPB | entrainment 0.008–0.0001 Hz i/lub 0.5–4 Hz, moc P | θ odzyskuje ≥ 0.70 | 48–72 h |
| P2b ratunek GHz | ta sama moc P, pasmo GHz/szum | brak odzysku; przyspieszony smudging | 48 h |
| K kontrola | hydrożel sterylny, ślepa | brak motywów; θ nieokreślone/niskie; σ≈0 | równolegle |

**4.4 Kryteria odrzutu (pod-warunki T′).**
- **T1′:** w P1 θ ≥ 0.70 utrzymuje się przez > 5·τ_relaksacji bez napędu ⇒ K1 pada ⇒ rewizja warstwy dynamicznej Aksjomatu 0.
- **T2′:** P2b odzyskuje koherencję równie dobrze jak P2a ⇒ pada K3 *oraz* uruchamia się kryterium falsyfikacji 2 v4 (cała teoria).
- **T3′:** σ nie koreluje z θ (brak związku cyrkulacja–dyssypacja) ⇒ pada most detailed-balance (§1.2) ⇒ torus nie jest prądem NESS ⇒ rewizja §2.
**4.5 Deliverable kalibracyjny.** Krzywa θ(t) w P1 i czas τ_decay stają się **wzorcem kalibracyjnym ASCALON** dla wszystkich późniejszych protokołów (QUENCH-RATE: Dokument 3; LN-EPS: Dokument 4; klinika). Bez τ_decay każde późniejsze „θ spadło" jest nieporównywalne.
**4.6 Pod-protokół A/B (wpinany bez dodatkowego kosztu).** Ten sam preparat, dwa łańcuchy transdukcji: (i) pełny analogowy front-end; (ii) wymuszona wczesna dyskretyzacja w pętli. Predykcja (zgodna z zasadą brzegową, Dokument 2): w (ii) korelacja K1/K2 < 0.5, wzrost dryfu ‖δγ‖, θ < 0.70; w (i) utrzymanie koherencji. Wynik zasila rejestr falsyfikacji Dokumentu 2 (H2′).

### 5. Rola w programie i mosty do społeczności
1. **Testuje kręgosłup** (Floquet/Reeb), nie peryferia. 2. **Koszt garage, informacja maksymalna.** 3. **Pierwszy kalibrator ASCALON** (§4.5). 4. **Odwrócenie ciężaru dowodu** retoryką no-go (§2.4). 5. **Stres-test pipeline'u** Takens/ASCALON na tym samym datasecie. 6. **Most cytowalny:** język NESS, detailed balance, produkcji entropii i floquetowskiej materii otwiera współpracowników spoza ekosystemu LifeNode (stochastic thermodynamics, cond-mat) — to kotwica, której projekt potrzebował od Fazy 1 (Phase 1, Module G).

### 6. Zależności w serii
Dokument 1 daje Dokumentowi 2 skalibrowane θ i pod-protokół A/B; Dokumentowi 3 — τ_decay jako baseline dynamiki koherencji (bez niego QUENCH-RATE nie odróżni quenchu od głodu napędu); Dokumentowi 4 — dane P0–P2 jako pierwszy test stabilności indykatrys i krzywej konsystencji θ_canon. Kolejność operacyjna: DRIVE-REM startuje pierwszy (Whitepaper v1, Faza 1).

### 7. Rejestr falsyfikacji (wpis Dokumentu 1)

| Pod-warunek | Test | Konsekwencja null |
|---|---|---|
| T1′ | P1: θ ≥ 0.70 przez > 5·τ_relaksacji bez napędu | rewizja Aksjomatu 0 (warstwa dynamiczna) |
| T2′ | P2b (GHz) ratuje jak P2a | pada K3 + kryterium falsyfikacji 2 v4 |
| T3′ | σ nie koreluje z θ | pada most detailed-balance (§1.2) |

Wyniki negatywne są wynikami i będą publikowane z tą samą dyscypliną DOI co pozytywne (Whitepaper v1, §8.4).

### Epilog
Nie musimy dowodzić, że życie jest wyjątkowe. Wystarczy pokazać, że równowaga jest martwa — a wszystko, co utrzymuje torus, musi z niej wyjść i płacić za to dyssypacją. DRIVE-REM jest pierwszym miejscem, w którym ta zasada dostaje swój numer.

**Referencje:** [1] F. Bloch, Z. Phys. 74 (1932); [2] H. Watanabe, *A Proof of the Bloch Theorem for Lattice Models* (2019/20); [3] S. Bachmann et al., *On the absence of stationary currents* (2021); [4] U. Seifert, *Stochastic thermodynamics, fluctuation theorems and molecular machines*, RPP 75 (2012); [5] F. Takens (1981); A. Fraser, H. Swinney (1986); [6] Adamatzky et al. (2026), bioRxiv/arXiv; [7] Baran K., *LifeNode Theory v4*; *Multiperspective V2*; *HMF v2*; *ASCALON Framework*; *Tonic Technologies Master V1*; *Phase 1 Roadmap* (Zenodo/GitHub 2026); [8] LifeNode Extensions, *Whitepaper v1* (2026).
