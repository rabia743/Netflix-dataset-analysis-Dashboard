import ast
import pandas as pd

netfl = pd.read_csv("netflix.csv")
print(netfl.head(5))
print(netfl.tail(5))

# Rename columns first
netfl.rename(columns={
    "index": "Index",
    "id": "Id",
    "title": "Title",
    "type": "Type",
    "release_year": "Release_Year",
    "age_certification": "Age_certification",
    "runtime": "Runtime",
    "genres": "Genres",
    "production_countries": "Production_countries",
    "seasons": "Seasons",
    "imdb_id": "Imdb_id",
    "imdb_score": "Imdb_score",
    "imdb_votes": "Imdb_votes"}, inplace=True)
print(netfl.isnull().sum())
# # remove the missing value
# netfl.dropna(inplace=True)
# print(netfl)
netfl["Title"] = netfl["Title"].fillna('Unknown_' + netfl["Id"].astype(str))
print(netfl.columns.tolist())
netfl.fillna({
    "Age_certification": "Not Rated",
    "Seasons": 1,
    "Imdb_id": "Unknown",
    "Imdb_score": netfl["Imdb_score"].mean(),
    "Imdb_votes": netfl["Imdb_votes"].median()}, inplace=True)
# # data cleaning
print(netfl.duplicated().sum())
# netfl.drop_duplicates(inplace=True)
# print(netfl.duplicated().sum())
print(netfl.dtypes)
# #TEXT CLEANING 
# 1. Convert string lists to actual lists
def safe_literal_eval(x):
    if isinstance(x, str):
        try:
            return ast.literal_eval(x)
        except:
            return []
    return x if isinstance(x, list) else []

netfl["Genres"] = netfl["Genres"].apply(safe_literal_eval)
netfl["Production_countries"] = netfl["Production_countries"].apply(safe_literal_eval)
# 2. Clean Title - remove extra spaces
netfl["Title"] = netfl["Title"].str.strip()
# 3. Standardize Type - uppercase
netfl["Type"] = netfl["Type"].str.upper()
# 4. Standardize Age_certification - strip spaces
netfl["Age_certification"] = netfl["Age_certification"].str.strip()
# 5. Create new features
netfl["Genre_Count"] = netfl["Genres"].apply(lambda x: len(x) if isinstance(x, list) else 0)
netfl["Country_Count"] = netfl["Production_countries"].apply(lambda x: len(x) if isinstance(x, list) else 0)
netfl["Main_Genre"] = netfl["Genres"].apply(lambda x: x[0] if isinstance(x, list) and len(x) > 0 else 'Unknown')
netfl["Main_Country"] = netfl["Production_countries"].apply(lambda x: x[0] if isinstance(x, list) and len(x) > 0 else 'Unknown')

# # CHECK CLEANED DATA
print(netfl.head())
print(netfl.isnull().sum())
print(netfl.dtypes)
print(netfl.columns.tolist())
print(netfl.dtypes)

netfl.to_csv("netflix.csv", index=False)
print("Data cleaning completed and saved to netflix.csv")


