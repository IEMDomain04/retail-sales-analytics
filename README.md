# Retail Sales Data Cleaning

This project demonstrates data cleaning techniques on retail sales data. It is designed for the Elective Data Science course.

[Press me to see Dashboard sample..](visuals/retail-sale-img.png)

## Project Team

| Name                | Role                        |
|---------------------|---------------------------- |
| Bilan, Edrill       | **Descriptive Analyst**         |
| Deldoc, Rojo        | **Diagnostic Analyst**          |
| Lopez, Roman        | **Predictive Analyst**          |
| Manduriaga, Emman   | **Data Quality Analyst**        |

Our team carried out **prescriptive analytics** together.

The retail sales dataset consists of 2823 rows and 25 columns, but it also presents several common data quality issues:

- **Missing Values:** Some columns contain missing entries that require appropriate handling to ensure data integrity.
- **Outliers:** The dataset includes outliers that should be identified and addressed to prevent skewed analysis.
- **Incorrect Data Types:** Certain columns have incorrect data types, which may affect downstream modeling and visualization. These need to be corrected for accurate processing.

## Getting Started

Follow these steps to set up and run the project:

### 1. Clone the Repository

```bash
git clone https://github.com/IEMDomain04/retail-sales-analytics.git
```
```bash
cd retail-sales-analytics
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

On Windows:

```bash
.venv\Scripts\activate
```

If you encounter permission issues, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 4. Install Required Libraries

```bash
pip install -r requirements.txt
```

But.. you can install only pandas for the script instead of the whole .txt file:

```bash
pip install pandas
```

### 5. Run the Scripts

Explore and run the provided scripts to practice data cleaning.

---

## Resources
- **Retail Sales Dataset:** [Sample Sales Data on Kaggle](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)
- **Dataset Overview:** [Overview of the Retail Sales Kaggle Dataset](https://22.frenchintelligence.org/2024/06/28/overview-of-the-retail-sales-kaggle-dataset/?utm_source)
