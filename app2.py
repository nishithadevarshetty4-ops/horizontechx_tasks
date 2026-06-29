# ==========================================================
# TASK 4: DATA VISUALIZATION DASHBOARD (Netflix Dataset)
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

df = pd.read_csv(r"C:\Users\nivvi\Downloads\netfilx.data\netflix_titles.csv")
# Change the path above if your CSV is in a different location.

# ----------------------------------------------------------
# Dataset Information
# ----------------------------------------------------------

print("="*60)
print("First 5 Rows")
print("="*60)
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistics:")
print(df.describe(include='all'))

# ----------------------------------------------------------
# Data Cleaning
# ----------------------------------------------------------

df = df.drop_duplicates()

# Fill missing values
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")

# Convert date_added column safely
df["date_added"] = pd.to_datetime(
    df["date_added"].astype(str).str.strip(),
    errors="coerce"
)

# ----------------------------------------------------------
# 1. Movies vs TV Shows
# ----------------------------------------------------------

plt.figure(figsize=(6,5))

sns.countplot(data=df, x="type")

plt.title("Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# 2. Release Year Distribution
# ----------------------------------------------------------

plt.figure(figsize=(10,5))

sns.histplot(df["release_year"], bins=25, kde=True)

plt.title("Content Release Year Distribution")

plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# 3. Top 10 Countries
# ----------------------------------------------------------

top_countries = df["country"].value_counts().head(10)

plt.figure(figsize=(10,5))

sns.barplot(x=top_countries.values,
            y=top_countries.index)

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# 4. Top Ratings
# ----------------------------------------------------------

plt.figure(figsize=(10,5))

sns.countplot(
    data=df,
    y="rating",
    order=df["rating"].value_counts().index
)

plt.title("Content Rating Distribution")

plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# 5. Top Genres
# ----------------------------------------------------------

genres = (
    df["listed_in"]
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10,6))

sns.barplot(
    x=genres.values,
    y=genres.index
)

plt.title("Top 10 Genres on Netflix")

plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# 6. Movies Added Each Year
# ----------------------------------------------------------

added_year = df["date_added"].dt.year.value_counts().sort_index()

plt.figure(figsize=(10,5))

plt.plot(added_year.index,
         added_year.values,
         marker="o")

plt.title("Netflix Content Added Per Year")
plt.xlabel("Year")
plt.ylabel("Titles Added")

plt.grid(True)

plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# 7. Dashboard
# ----------------------------------------------------------

fig, axes = plt.subplots(2,2, figsize=(15,10))

# Movies vs TV Shows
sns.countplot(
    data=df,
    x="type",
    ax=axes[0,0]
)
axes[0,0].set_title("Movies vs TV Shows")

# Release Year
sns.histplot(
    df["release_year"],
    bins=20,
    ax=axes[0,1]
)
axes[0,1].set_title("Release Year Distribution")

# Ratings
sns.countplot(
    data=df,
    y="rating",
    order=df["rating"].value_counts().head(10).index,
    ax=axes[1,0]
)
axes[1,0].set_title("Top Ratings")

# Top Countries
sns.barplot(
    x=top_countries.values,
    y=top_countries.index,
    ax=axes[1,1]
)
axes[1,1].set_title("Top Countries")

plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# Insights
# ----------------------------------------------------------

print("\n" + "="*60)
print("INSIGHTS")
print("="*60)

print("\nMovies vs TV Shows")
print(df["type"].value_counts())

print("\nTop 5 Countries")
print(df["country"].value_counts().head())

print("\nTop 5 Ratings")
print(df["rating"].value_counts().head())

print("\nLatest Release Year:")
print(df["release_year"].max())

print("\nOldest Release Year:")
print(df["release_year"].min())

print("\nAverage Release Year:")
print(round(df["release_year"].mean(),2))

print("\nDashboard Generated Successfully!")