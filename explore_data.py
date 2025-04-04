import requests
import pandas as pd

url = "https://www.bankofcanada.ca/valet/observations/FXUSDCAD/json"
response = requests.get(url)
data = response.json()

observations = data['observations']
df = pd.DataFrame(observations)
print(df.head())
