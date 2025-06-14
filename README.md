# 🚗 TrafikkulykkeDataanalyse\_Norge

Analyse av trafikkulykker i Norge (1990 – 2024) basert på åpne data fra **Statens vegvesen**. Prosjektet avdekker mønstre i **tid 🕒, sted 📍, vær 🌦, kjønn 🢑 og vegtilstand 🚣** for å støtte bedre trafikksikkerhetstiltak.

---

## 🖥 Kom i gang på 3 minutter

```bash
# klon repoet
git clone https://github.com/USERNAME/TrafikkulykkeDataanalyse_Norge.git
cd TrafikkulykkeDataanalyse_Norge

# installer avhengigheter
pip install -r requirements.txt

# 1⃣  last ned CSV ene fra Google Drive (skriptet bruker gdown)
python scripts/download_data.py      # fyll inn fil ID er i scripts/download_data.py

# 2⃣  flytt datafilene til samme mappe som notebookene
mv data/*.csv notebooks/

# 3⃣  start analyser
jupyter notebook notebooks/
```

> Notebookene forventer at CSV ene ligger i **samme mappe**; da trengs ingen sti endringer.

---

## 📂 Prosjektstruktur

```
TrafikkulykkeDataanalyse_Norge/
│
├── notebooks/              # Jupyter notebooks + CSV data + PDF rapporter
│   ├── Ulykke_tidspunkt_analyse.ipynb
│   ├── Ulykke_tidspunkt_analyse.pdf
│   ├── Ulykker_temp_analyse.ipynb
│   ├── Ulykker_temp_analyse.pdf
│   └── …
│
├── scripts/                # ETL & nedlasting
│   └── download_data.py
│
├── requirements.txt
└── README.md               # denne filen
```

---

## 🔍 Notebook oversikt

| Tema                           | Notebook (.ipynb)                                  | PDF rapport                                               |
| ------------------------------ | -------------------------------------------------- | --------------------------------------------------------- |
| **Helhetlig risikomønster**    | `notebooks/risikomønster_ulykker_rapport.ipynb`    | [Vis PDF](notebooks/risikomønster_ulykker_rapport.pdf)    |
| Tidspunkt på døgnet / sesong   | `notebooks/Ulykke_tidspunkt_analyse.ipynb`         | [Vis PDF](notebooks/Ulykke_tidspunkt_analyse.pdf)         |
| Temperatur & risiko            | `notebooks/Ulykker_temp_analyse.ipynb`             | [Vis PDF](notebooks/Ulykker_temp_analyse.pdf)             |
| Vær & sikt                     | `notebooks/Ulykker_vaerforhold_analyse_full.ipynb` | [Vis PDF](notebooks/Ulykker_vaerforhold_analyse_full.pdf) |
| Skadegrad over tid             | `notebooks/skadegrad_analyse_med_kode.ipynb`       | [Vis PDF](notebooks/skadegrad_analyse_med_kode.pdf)       |
| Kjønn & trafikanttype          | `notebooks/skader_kjønn_analyse.ipynb`             | [Vis PDF](notebooks/skader_kjønn_analyse.pdf)             |
| Plassering i kjøretøy          | `notebooks/skade_plassering_analyse.ipynb`         | [Vis PDF](notebooks/skade_plassering_analyse.pdf)         |
| Ukedagstype (hverdag vs. helg) | `notebooks/skader_ukedagstype_analyse.ipynb`       | [Vis PDF](notebooks/skader_ukedagstype_analyse.pdf)       |
| Vegkategori & vegdekke         | `notebooks/vegtilstand_skader.ipynb`               | [Vis PDF](notebooks/vegtilstand_skader.pdf)               |
| Kommune × kjønn                | `notebooks/skadeanalyse_kommune_kjønn.ipynb`       | [Vis PDF](notebooks/skadeanalyse_kommune_kjønn.pdf)       |

> GitHub viser PDF ene direkte i nettleseren – klikk «Vis PDF» for å lese rapportene.

---

## ✨ Samlede hovedfunn

1. **Desember effekten:** Mørke, nullføre og juletrafikk gir flest alvorlige ulykker. Desember topper antall skader i flere analyser, og økt trafikk kombinert med vinterforhold skaper et tydelig risikobilde.
2. **“Gode” forhold ≠ trygge:** Flest ulykker skjer faktisk på dager med god sikt og tørr vei. Dette henger sammen med økt eksponering – flere biler og myke trafikanter er ute i godt vær.
3. **Kjønnsgap:** Menn er overrepresentert i nesten alle ulykkeskategorier, spesielt dødsulykker. Analysene viser at menn oftere kjører bil, har høyere fart og tar flere risikoer.
4. **Privat /skogsbilveg:** Disse vegene har få ulykker totalt, men en uforholdsmessig stor andel med hardt skadde eller drepte. Lav standard og lite sikring er trolig årsaken.
5. **Nullføre (−5 °C → +5 °C):** Temperaturintervallet mellom minus og pluss gir glatte, uforutsigbare forhold. Dette fremkommer som et gjennomgående risikoområde i flere analyser, og bør få egne tiltak.

---

## 🌟 Eksempel på anbefalte tiltak

| Tiltak                                     | Datagrunnlag                   | KPI                              |
| ------------------------------------------ | ------------------------------ | -------------------------------- |
| **Nullføre SMS** til sjåfører              | Temp  & vær analyse            | Tid fra varsel → strøing/grusing |
| **Farts  & beltekontroll uke 48 52**       | Tidspunkt  & skadegrad analyse | Drepte pr. 100 mill. k m (des)    |
| **Baksetebelte kampanje før fellesferien** | Plasserings analyse            | Beltebruk bak (%)                |
| **Nattkontroll i helger**                  | Ukedagstype analyse            | Hardt skadde (helg/uke)          |

---

## 📜 Lisens

- **Kode:** MIT lisens
- **Data & PDF rapporter:** © Statens vegvesen – delt under NLOD 2.0. Husk kildehenvisning ved videre bruk.

---

> Spørsmål eller forslag?\
> Åpne en **Issue** eller kontakt **@SushantSriv** på GitHub.

