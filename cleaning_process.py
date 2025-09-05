import pandas as pd # type: ignore

# ----------------------------- 
# Load dataset
# -----------------------------
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")


# ----------------------------- 
# Display initial info
# -----------------------------
print("=== Initial Dataset Info ===")
print(df.shape)
print(df.dtypes)


# ----------------------------- 
# Displaying missing values in each column
# -----------------------------
print("\n=== Missing values before cleaning: ===")
print(df.isnull().sum())


# -----------------------------
# Displaying missing values to those columns we will handle
# -----------------------------
print("\nMissing ADDRESSLINE2 values before filling:", df["ADDRESSLINE2"].isnull().sum())
print("\nMissing STATE values before filling:", df["STATE"].isnull().sum())
print("\nMissing POSTALCODE values before filling:", df["POSTALCODE"].isnull().sum())
print("\nMissing TERRITORY values before filling:", df["TERRITORY"].isnull().sum())


# -----------------------------
# Handle Missing Data for STATE, POSTALCODE, TERRITORY using IMPUTATION
# -----------------------------
df["STATE"] = df["STATE"].fillna("Unknown")
df["POSTALCODE"] = df["POSTALCODE"].fillna("Unknown")
df["TERRITORY"] = df["TERRITORY"].fillna("Not Assigned")

# --- Handle ADDRESSLINE2 ---
if "ADDRESSLINE2" in df.columns:
    if df["ADDRESSLINE2"].isnull().sum() / len(df) > 0.5:
        df = df.drop(columns=["ADDRESSLINE2"])
        print("\nADDRESSLINE2 dropped (too many missing values).")


# -----------------------------
# Fix Data Formatting: Order Date from String to Datetime
# -----------------------------
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")


# -----------------------------
# Detect & Manage Outliers in SALES: Skewed Distribution
# -----------------------------
Q1 = df["SALES"].quantile(0.25)
Q3 = df["SALES"].quantile(0.75)
IQR = Q3 - Q1 # Formula: Interquartile Range 
upper_bound = Q3 + 1.5 * IQR # 1.5 is the standard multiplier
lower_bound = Q1 - 1.5 * IQR # 1.5 is the standard multiplier


# --- Flag and display number of outliers ---
df["SALES_outlier"] = (df["SALES"] < lower_bound) | (df["SALES"] > upper_bound)
print("\nNumber of outliers in SALES (before Capping):", df["SALES_outlier"].sum())


# -----------------------------
# Display the max and min values of SALES before Capping outliers
# -----------------------------
print("\nUPPER BOUND", upper_bound)
print("LOWER BOUND", lower_bound)


# --- CAPPING ---
df.loc[df["SALES"] > upper_bound, "SALES"] = upper_bound
df.loc[df["SALES"] < lower_bound, "SALES"] = lower_bound


# --- Recalculate outliers after Capping ---
df["SALES_outlier"] = (df["SALES"] < lower_bound) | (df["SALES"] > upper_bound)
print("\nNumber of outliers in SALES (after Capping):", df["SALES_outlier"].sum())


# -----------------------------
# Proof of Cleaning
# -----------------------------
print("\n=== Cleaned Dataset Info ===")
print(df.shape)
print(df.dtypes)
print("\nMissing values after cleaning:")
print(df.isnull().sum())


# -----------------------------
# Displaying missing values after Data Cleaning
# -----------------------------
# print("\nMissing ADDRESSLINE2 values before filling:", df["ADDRESSLINE2"].isnull().sum())
print("\nMissing STATE values before filling:", df["STATE"].isnull().sum())
print("\nMissing POSTALCODE values before filling:", df["POSTALCODE"].isnull().sum())
print("\nMissing TERRITORY values before filling:", df["TERRITORY"].isnull().sum())


print("\n=== Sample Cleaned Data ===")
print(df.head(10))
