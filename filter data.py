import pandas as pd
netfl = pd.read_csv("netflix.csv")
#  Analysis ke liye filter karo (without saving)
movies = netfl[netfl["Type"] == "MOVIE"]
web_series = netfl[netfl["Type"] == "SHOW"]

# Analysis 
print(f"Movies: {len(movies)}")
print(f"Web Series: {len(web_series)}")

# 4. Alag-alag CSV files mein save 
movies.to_csv("movies.csv", index=False)
web_series.to_csv("web_series.csv", index=False)