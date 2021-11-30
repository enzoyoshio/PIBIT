import pandas as pd
import os

caminho = os.getcwd()
df = pd.read_json(r'output.json')
df.to_csv(f'{caminho}/parsed.csv', index=None)
