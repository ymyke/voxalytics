"""Load libraries and data, prepare data, expose data, functions, and libraries."""

__all__ = [
    # Dataframes:
    "parcels",
    "island_sizes",
    # JSONs:
    "parcels_json",
    # Functions:
    "show_leaderboard",
    "counter_to_string",
    # Some libraries to be used in the notebooks:
    "sns",
    "plt",
    "pd",
]

from typing import List
from collections import Counter
from datetime import datetime
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.display import display, HTML

# Generic setup:

sns.set_style("whitegrid")

PARCELS_URL = "https://www.cryptovoxels.com/api/parcels.json"
response = requests.request("GET", PARCELS_URL)
parcels_json = response.json()["parcels"]
parcels = pd.DataFrame.from_records(parcels_json)
parcels["voxvolume"] = parcels.area * parcels.height * 8
print(datetime.utcnow().strftime("%c"), " UTC")
print("{} parcels loaded.".format(parcels.shape[0]))

island_sizes = (
    parcels.groupby("island")
    .agg({"id": "count", "area": "sum", "voxvolume": "sum"})
    .rename(columns={"id": "parcels"})
)
island_sizes["voxperparcel"] = island_sizes.voxvolume / island_sizes.parcels


# Functions:


def show_leaderboard(
    address_counts: List[Counter], name: str, howmany: int = 10
) -> None:
    """Show list of Counters as a leaderboard. Counter keys are expected to be ETH
    addresses and get linked to Cryptovoxels.
    """
    i = 1
    for (address, count) in sorted(
        address_counts.items(), key=lambda x: x[1], reverse=True
    )[:howmany]:
        display(
            HTML(
                f"{i:02d}. "
                f'<a href="https://www.cryptovoxels.com/avatar/{address}">{address}</a>'
                f" with {count:03d} {name}"
            )
        )
        i += 1


def counter_to_string(counter: Counter, howmany: int = 10) -> str:
    """Turn counter object into a string showing the top howmany items."""
    return "\n".join(
        [
            f"{cnt:5d}: {key}"
            for key, cnt in sorted(counter.items(), key=lambda x: x[1], reverse=True)[
                :howmany
            ]
        ]
    )
