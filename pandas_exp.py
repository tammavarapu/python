
import numpy as np
import pandas as pd

files_path='/home/orienit/samba/python/input_files/weather.csv'
df = pd.read_csv(files_path)

print(df.head())
