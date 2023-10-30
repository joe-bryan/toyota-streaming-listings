import pandas as pd
from datetime import datetime
import numpy as np
from mimesis import Fieldset
from mimesis.locales import Locale

toyota_trucks = [
    "Land Cruiser",
    "Tacoma",
    "Tundra",
    "4Runner",
    "Rav4",
    "Highlander",
    "Grand Highlander",
    "Venza",
    "FJ Cruiser",
    "Sequoia",
]
toyota_probability = [0.01, 0.17, 0.23, 0.16, 0.19, 0.09, 0.01, 0.02, 0.05, 0.07]
year = [
    "2013",
    "2014",
    "2015",
    "2016",
    "2017",
    "2018",
    "2019",
    "2020",
    "2021",
    "2022",
    "2023",
]
year_probability = [0.07, 0.11, 0.14, 0.11, 0.10, 0.14, 0.07, 0.08, 0.06, 0.09, 0.03]

df = pd.DataFrame(
    [
        {
            "event_time": datetime.now().isoformat(),
            "event_name": np.random.choice(["New Listing", "Sold"], p=[0.81, 0.19]),
            "user": round(np.random.random() * 10000),
            "make": "Toyota",
            "name": np.random.choice(toyota_trucks, p=toyota_probability),
            "year": np.random.choice(year, p=year_probability),
            "mileage": np.random.randint(1530, 279000),
            "price": np.random.randint(9878, 77000),
            "dealer_rating": np.random.randint(1, 6),
        }
        for _ in range(100)
    ]
)

df = df.to_dict(orient="records")

df.to_parquet("toyota_listings_100.parquet.gzip", compression="gzip")
