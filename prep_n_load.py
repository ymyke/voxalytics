__all__ = ["parcels", "sns", "plt"]

import requests
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

url = "https://www.cryptovoxels.com/api/parcels.json"
response = requests.request("GET", url)
parcels = response.json()["parcels"]
print("{} parcels loaded.".format(len(parcels)))
