"""
sample data claen and prep

"""
from pathlib import Path
import pandas as pd

root = Path(r"C:\SHAN\python-data-clean_prep")
out_dir = root / "data_files"
out_dir.mkdir(parents=True, exist_ok=True)

data = {
    'id': [1, 2, 2, 3, 4, None],
    'name': [' Alice', 'bob ', 'CHARLIE', 'David', 'Eve', 'Frank'],
    'email': ['alice@example.com', 'BOB@EXAMPLE.COM', 'charlie@example.com', None, 'eve@example.com', 'frank@example.com'],
    'signup_date': ['2025-01-01', '01/02/2025', '2025-03-03T00:00:00', 'March 4, 2025', '2025-05-05', ''],
    'amount': ['100', '200.0', 'N/A', ' 400', '500.50', '600'],
    'notes': ['Good', 'good', 'GOOD', 'Needs follow-up', '', None]
}

df = pd.DataFrame(data)

# add a duplicate row to practice deduplication
df = pd.concat([df, df.iloc[[1]]], ignore_index=True)

out_path = out_dir / "sample_data.xlsx"

df.to_excel(out_path, index=False)

print(f"Wrote: {out_path}")
