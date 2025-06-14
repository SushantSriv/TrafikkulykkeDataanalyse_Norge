import pandas as pd

# CSV-filer
files = [
    "skader_skadegrad_1994_1990_ny.csv",
    "skader_skadegrad_2010_1995_ny.csv",
    "skader_skadegrad_2023_2011_ny.csv"
]

# Kolonnenavn fra rad 8
column_names = ["År","Måned","Kommune","Drept","Hardt skadd","Lettere skadd","Sum"]

# Funksjon for å lese fra rad 9 og tildele kolonnenavn
def load_and_clean(file):
    df = pd.read_csv(file, sep=";", header=None, encoding="ISO-8859-1")
    df = df.iloc[8:].copy()  # fra rad 9 og ned
    df.columns = column_names
    return df

# Kombiner alle filer
dataframes = [load_and_clean(f) for f in files]
combined_df = pd.concat(dataframes, ignore_index=True)

# Rens: fjern whitespaces og konverter År til tall
combined_df = combined_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
combined_df["År"] = pd.to_numeric(combined_df["År"], errors="coerce")

# Sorter etter År, Kommune, Måned
sorted_df = combined_df.sort_values(by=["År", "Kommune", "Måned"])

# Lagre resultat
sorted_df.to_csv("skader_skadegrad_ny.csv", index=False, sep=";")

print("✅ Ferdig! Fil lagret som 'svv_data_sortert_med_opprinnelige_kolonner.csv'")
