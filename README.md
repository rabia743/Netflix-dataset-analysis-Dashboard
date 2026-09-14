
<h1 align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/Netflix-new-icon.png" alt="Netflix Logo" width="120"/> <br> Netflix Dataset Anlysis</h1><p align="center"> <em>📊 Data Analysis • 🎬 5,087 Titles • 🎥 3,759 Movies • 📺 2,058 TV Shows</em> </p><hr>

📌 Overview
An end-to-end Data Analysis, Machine Learning Preprocessing & Visualization Dashboard built on a Netflix Movies & TV Shows dataset containing 5,087 titles spanning from 1945 to 2022.

This project explores:

🎥 How Netflix's content library evolved over the years

🌍 Which countries produce the most content

📺 The balance between Movies and TV Shows

🎭 Popular genres, ratings, and directors

⏳ IMDb scores and runtime distributions

🛠️ Technologies Used
Category	Tools:

Language	: Python 3.x

Data Handling :	Pandas, NumPy

Visualization	: Matplotlib, Seaborn

Dashboard	: Streamlit / Plotly Dash

Machine Learning	: Scikit-learn (LabelEncoder, OneHotEncoder, StandardScaler)

Version Control :	Git & GitHub

📂 Project Features:

📥 Load raw Netflix dataset (before data.csv)

🧹 Clean missing values, duplicates, and inconsistent formats

🔍 Filter Movies and TV Shows into separate datasets

📊 Interactive dashboard with filters (Year, Country, Type, Rating)

📈 KPI cards: Total Titles, Movies, TV Shows, Countries

🌍 Country-wise content distribution

🎭 Top genres and directors

⏳ Content added over time (trend line)

🤖 Machine Learning preprocessing with LabelEncoder, OneHotEncoder, StandardScaler

🧹 Data Cleaning & Preprocessing
Steps performed on the dataset:

Handled missing values in director, cast, country, rating

Filled unknown IMDb data with default values

Split multi-value columns (genres, production_countries) into separate features

Created Genre_Count, Country_Count, Main_Genre, Main_Country columns

Removed duplicate records

Standardized column names (snake_case)

Added Index, Seasons, and Imdb_id fields

python
import pandas as pd

netfl = pd.read_csv("after data.csv")
netfl.drop(columns=["Index", "Id", "Title", "Imdb_id"], inplace=True)
Output Files:
after data.csv → Cleaned dataset (5,087 rows, 17 columns)

movies.csv → Movies-only dataset (3,759 rows)

web_series.csv → TV Shows-only dataset (2,058 rows)

📊 Data Analysis & EDA
Key analyses performed:

Content added per year (huge spike post-2015)

Top 10 countries producing content: US, India, UK, Japan, Egypt, France, GB

Movies vs TV Shows ratio

Most common ratings: TV-MA, R, TV-14, PG-13, Not Rated

Longest movies (e.g., The School of Mischief – 251 min)

Highest rated content (No Longer Kids – 9.0 IMDb)

Interactive elements:

🎚️ Dropdown filters (Type, Country, Genre)

📅 Year range slider

🗺️ Hover-enabled maps

📌 Dynamic KPI cards

📊 Bar / Pie / Line charts

📈 Movies vs TV Shows
Type	Count	Percentage
🎥 Movies	3,759	~73.9%
📺 TV Shows	2,058	~26.1%
📊 Total Titles	5,087	100%
Insight: Netflix's library is heavily dominated by Movies (~74%), but TV Shows (~26%) have grown significantly since 2015, especially K-Dramas and Anime.

ℹ️ Note: Total titles count is 5,087 (not 5,806 as in some versions of the dataset), because the raw dataset contains entries where Type is missing or duplicated and were dropped during cleaning. After removing such records and keeping only valid MOVIE and SHOW entries, we get:

Movies (MOVIE type): 3,759

TV Shows (SHOW type): 2,058

Total: 5,087

🤖 Machine Learning Preprocessing
Using machine learning.py, the dataset is prepared for ML models:

1️⃣ Label Encoding (Type column)
python
le = LabelEncoder()

netfl["Type_encoded"] = le.fit_transform(netfl["Type"])

2️⃣ One-Hot Encoding (Genres & Countries)

python

genres_onehot = netfl["Genres"].str.get_dummies(sep=',')

countries_onehot = netfl["Production_countries"].str.get_dummies(sep=',')

netfl = pd.concat([netfl, countries_onehot], axis=1)

3️⃣ Feature Scaling (StandardScaler)

python
numeric_cols = ["Release_Year", "Runtime", "Seasons", "Imdb_votes",
                "Genre_Count", "Country_Count"]
                
scaler = StandardScaler()

netfl[numeric_cols] = scaler.fit_transform(netfl[numeric_cols])

🚀 How to Run
bash
# 1. Clone the repository
git clone https://github.com/rabia743/netflix-dashboard.git

# 2. Navigate into project
cd netflix-dashboard

# 3. Install dependencies
pip install -r requirements.txt

# 4. Filter Movies & TV Shows
python "filter data.py"

# 5. Run ML preprocessing
python "machine learning.py"

# 6. Launch dashboard
streamlit run dashboard/app.py
Then open http://localhost:8501 in your browser.

💡 Key Learnings
Practical data cleaning on messy real-world data (missing IMDb scores, unknown countries)

Using explode() and str.get_dummies() for multi-value columns

Handling LabelEncoder, OneHotEncoder, and StandardScaler for ML pipelines

Building interactive dashboards with Streamlit/Plotly

Storytelling with data through visual hierarchy

Deploying dashboards to the cloud (Streamlit Cloud / Heroku)

📌 Dataset Summary
Metric	Value
📊 Total Titles	5,087
🎥 Total Movies	3,759
📺 Total TV Shows	2,058
🌍 Countries	90+
🎭 Genres	20+
📅 Years Covered	1945 – 2022

