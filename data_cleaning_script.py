"""
Data Cleaning Script for Sales Data
- Handles missing values
- Fixes data formatting issues
- Detects and flags outliers
- Skew Distribution and Capping for outliers
- Saves cleaned dataset to CSV
"""

import pandas as pd # type: ignore

# -----------------------------
# Function to save cleaned data
# -----------------------------
def save_cleaned_data(df, filename="cleaned_sales_data.csv"):
    
    # --- Prints if saving the file is complete ---
    df.to_csv(filename, index=False)
    print(f"\n[INFO] Cleaned data saved to {filename}")


# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")


# -----------------------------
# Handle Missing Data
# -----------------------------
df["STATE"] = df["STATE"].fillna("Unknown")
df["POSTALCODE"] = df["POSTALCODE"].fillna("Unknown")
df["TERRITORY"] = df["TERRITORY"].fillna("Not Assigned")


# -----------------------------
# Drop AddressLine2 if >50% missing
# -----------------------------
if "ADDRESSLINE2" in df.columns:
    if df["ADDRESSLINE2"].isnull().sum() / len(df) > 0.5:
        df = df.drop(columns=["ADDRESSLINE2"])
        print("\nADDRESSLINE2 dropped (too many missing values).")


# -----------------------------
# Fix Order Date Data Formatting: String to Datetime
# -----------------------------
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")


# -----------------------------
# Detect Outliers in SALES
# -----------------------------
Q1 = df["SALES"].quantile(0.25)
Q3 = df["SALES"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR


# -----------------------------
# Capping Outliers based on lower and upper bounds
# -----------------------------
df.loc[df["SALES"] < lower_bound, "SALES"] = lower_bound
df.loc[df["SALES"] > upper_bound, "SALES"] = upper_bound


# -----------------------------
# Call the function: Save cleaned dataset
# -----------------------------
save_cleaned_data(df, "cleaned_sales_data_V3.csv")
