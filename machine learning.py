import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler

netfl = pd.read_csv("after data.csv")
# # machine leanrning
# for text cleaning using label and onehot encoder
netfl.drop(columns=["Index", "Id", "Title", "Imdb_id"], inplace=True)
print(netfl.columns)

le = LabelEncoder()
netfl["Type_encoded"] = le.fit_transform(netfl["Type"])
print("\n Type Encoded:")
print(netfl["Type_encoded"].head(5))
# when you convert all dataset using to_string()
# print(netfl["Type_encoded"].to_string(index=False))

# # onehotencoder RATING COLUMN
genres_onehot = netfl["Genres"].str.get_dummies(sep=',')
print("\n Genres One-Hot Encoded:")
print(genres_onehot.head(5))
# when you convert all dataset using to_string()
# print(genres_onehot.to_string(index=False))
countries_onehot = netfl["Production_countries"].str.get_dummies(sep=',')
netfl = pd.concat([netfl, countries_onehot], axis=1)
print(countries_onehot.head(5))


# numerices machine learning using standarad and minmax scaler
numeric_cols = ["Release_Year", "Runtime", "Seasons", "Imdb_votes", "Genre_Count", "Country_Count"]
scaler = StandardScaler()
netfl[numeric_cols] = scaler.fit_transform(netfl[numeric_cols])
print(netfl[numeric_cols].head(5))
# print(netfl[numeric_cols].to_string(index=False))
