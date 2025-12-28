"""
clean_dropna.py

"""
from pathlib import Path
import pandas as pd

root = Path(r"C:\SHAN\python-data-clean_prep")
out_dir = root / "data_files"
out_dir.mkdir(parents=True, exist_ok=True)

# Prefer CSV (created earlier); fall back to Excel if CSV missing
csv_path = out_dir / "sample_data.csv"
xlsx_path = out_dir / "sample_data.xlsx"

if csv_path.exists():
    df = pd.read_csv(csv_path)
    source = str(csv_path)
elif xlsx_path.exists():
    df = pd.read_excel(xlsx_path)
    source = str(xlsx_path)
else:
    raise FileNotFoundError("No sample_data.csv or sample_data.xlsx found in data_files/")

print(f"Loaded {source} — shape: {df.shape}")
print(df.head())

# 1) Drop rows with any missing value (default)
df_any = df.dropna()
print(f"After dropna() (any) — shape: {df_any.shape}")
(df_any).to_csv(out_dir / "sample_data_dropna_any.csv", index=False)
(df_any).to_excel(out_dir / "sample_data_dropna_any.xlsx", index=False)

# 2) Drop rows where all values are missing
# (useful if completely-empty rows are present)
df_all = df.dropna(how="all")
print(f"After dropna(how='all') — shape: {df_all.shape}")
(df_all).to_csv(out_dir / "sample_data_dropna_all.csv", index=False)

# 3) Drop rows missing specific critical columns (e.g., email)
df_subset = df.dropna(subset=["email"]) if "email" in df.columns else df.copy()
print(f"After dropna(subset=['email']) — shape: {df_subset.shape}")
(df_subset).to_csv(out_dir / "sample_data_dropna_subset_email.csv", index=False)

# 4) Drop columns that have any missing values (axis=1)
df_dropcols = df.dropna(axis=1)
print(f"After dropna(axis=1) — kept columns: {list(df_dropcols.columns)}")
(df_dropcols).to_csv(out_dir / "sample_data_dropna_axis1.csv", index=False)

# 5) Example of inplace usage
df_inplace = df.copy()
# This will modify df_inplace in place
# (note: this returns None)
df_inplace.dropna(inplace=True)
print(f"After df_inplace.dropna(inplace=True) — shape: {df_inplace.shape}")

# 6) Pick one cleaned result to save as the main cleaned file
# Here we choose to keep rows that have an email (common requirement)
cleaned = df.dropna(subset=["email"]) if "email" in df.columns else df.dropna()
cleaned.to_csv(out_dir / "sample_data_cleaned.csv", index=False)
cleaned.to_excel(out_dir / "sample_data_cleaned.xlsx", index=False)

print("Wrote cleaned files to data_files/")
