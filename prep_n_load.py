"""Load libraries and data, prepare data, expose data, functions, and libraries."""

__all__ = [
    # Dataframes:
    "parcels",
    # Functions:
    "show_leaderboard",
    # Some libraries to be used in the notebooks:
    "sns",
    "plt",
    "pd",
]

from typing import List
from collections import Counter
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.display import display, HTML

# Generic setup:

sns.set_style("whitegrid")

PARCELS_URL = "https://www.cryptovoxels.com/api/parcels.json"
response = requests.request("GET", PARCELS_URL)
parcels = pd.DataFrame.from_records(response.json()["parcels"])
parcels["voxvolume"] = parcels.area * parcels.height * 8
print("{} parcels loaded.".format(parcels.shape[0]))


# Functions:


def show_leaderboard(
    address_counts: List[Counter], name: str, entries: int = 10
) -> None:
    """Show list of Counters as a leaderboard. Counter keys are expected to be ETH
    addresses and get linked to Cryptovoxels.
    """
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
