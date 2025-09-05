import pandas as pd # type: ignore

# -----------------------------
# Function to save cleaned data
# -----------------------------
def save_cleaned_data(df, filename="cleaned_sales_data.csv"):
    df.to_csv(filename, index=False)
    print(f"\n[INFO] Cleaned data saved to {filename}")

# -----------------------------
# Step 1: Load dataset
# -----------------------------
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

print("=== Initial Dataset Info ===")
print(df.shape)
print(df.dtypes)
print("\nMissing values before cleaning:\n", df.isnull().sum())

# -----------------------------
# Step 2: Handle Missing Data
# -----------------------------
df["STATE"] = df["STATE"].fillna("Unknown")
df["POSTALCODE"] = df["POSTALCODE"].fillna("Unknown")
df["TERRITORY"] = df["TERRITORY"].fillna("Not Assigned")

if "ADDRESSLINE2" in df.columns:
    if df["ADDRESSLINE2"].isnull().sum() / len(df) > 0.5:
        df = df.drop(columns=["ADDRESSLINE2"])
        print("\nADDRESSLINE2 dropped (too many missing values).")

# -----------------------------
# Step 3: Fix Data Formatting
# -----------------------------
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")

# -----------------------------
# Step 4: Detect Outliers in SALES
# -----------------------------
Q1 = df["SALES"].quantile(0.25)
Q3 = df["SALES"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Flag outliers
df["SALES_outlier"] = (df["SALES"] < lower_bound) | (df["SALES"] > upper_bound)
print("\nNumber of outliers in SALES (before handling):", df["SALES_outlier"].sum())

# --- OPTION A: Remove outliers ---
# df = df[~df["SALES_outlier"]]

# --- OPTION B: Cap outliers (Winsorization) ---
df.loc[df["SALES"] < lower_bound, "SALES"] = lower_bound
df.loc[df["SALES"] > upper_bound, "SALES"] = upper_bound

# Recalculate outliers after handling
df["SALES_outlier"] = (df["SALES"] < lower_bound) | (df["SALES"] > upper_bound)
print("Number of outliers in SALES (after handling):", df["SALES_outlier"].sum())

# -----------------------------
# Step 5: Proof of Cleaning
# -----------------------------
print("\n=== Cleaned Dataset Info ===")
print(df.shape)
print(df.dtypes)
print("\nMissing values after cleaning:\n", df.isnull().sum())

print("\n=== Sample Cleaned Data ===")
print(df.head(10))

# -----------------------------
# Step 6: Save cleaned dataset
# -----------------------------
save_cleaned_data(df, "cleaned_sales_data_V2.csv")
