import sys
import pandas as pd
import dpre

if len(sys.argv) != 2:
    print("Usage: python load.py <path_to_dataset>")
else:
    dataset_path = sys.argv[1]
    df = pd.read_csv(dataset_path)
    dpre.trans(df)

    print(df.head())
