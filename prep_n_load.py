__all__ = ["parcels", "sns", "plt", "show_leaderboard"]

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List
from IPython.core.display import display, HTML
from collections import Counter

# Generic setup:

sns.set_style("whitegrid")

url = "https://www.cryptovoxels.com/api/parcels.json"
response = requests.request("GET", url)
# parcels = response.json()["parcels"]
parcels = pd.DataFrame.from_records(response.json()["parcels"])
parcels["voxvolume"] = parcels.area * parcels.height * 8
print("{} parcels loaded.".format(parcels.shape[0]))


# Functions:


def show_leaderboard(
    address_counts: List[Counter], name: str, entries: int = 10
) -> None:
    i = 1
    for (address, count) in sorted(
        address_counts.items(), key=lambda x: x[1], reverse=True
    )[:entries]:
        display(
            HTML(
                f"{i:02d}. "
                f'<a href="https://www.cryptovoxels.com/avatar/{address}">{address}</a>'
                f" with {count:03d} {name}"
            )
        )
        i += 1
