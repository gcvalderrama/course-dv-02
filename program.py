import json
import pandas as pd
import numpy as np
from pprint import pprint

df = pd.read_csv("ExcelFormattedGISTEMPData2CSV.csv")

countries = []
years = []
regions = []
temperatures = []

print(df)
#first case by global hemisphere
for index, row in df.iterrows():
    years.append(row[0])
    countries.append('North Hemisphere')
    regions.append('North Hemisphere')
    temperatures.append(row[2])
    years.append(row[0])
    countries.append('South Hemisphere')
    regions.append('South Hemisphere')
    temperatures.append(row[3])

raw_data = {
    "Country": countries,
    "Year" : years,
    "Region": regions,
    "Temperature": temperatures
}
ndf = pd.DataFrame(raw_data, columns=['Country', 'Year', 'Region', 'Temperature'])
ndf.to_csv("global_year_ds.csv", index=False)

countries = []
years = []
regions = []
temperatures = []

for index, row in df.iterrows():
    years.append(row[0])
    countries.append('24N-90N')
    regions.append('24N-90N')
    temperatures.append(row[4])

    years.append(row[0])
    countries.append('24S-24N')
    regions.append('24S-24N')
    temperatures.append(row[5])

    years.append(row[0])
    countries.append('90S-24S')
    regions.append('90S-24S')
    temperatures.append(row[6])

    years.append(row[0])
    countries.append('64N-90N')
    regions.append('64N-90N')
    temperatures.append(row[7])

    years.append(row[0])
    countries.append('44N-64N')
    regions.append('44N-64N')
    temperatures.append(row[8])

    years.append(row[0])
    countries.append('44N-64N')
    regions.append('44N-64N')
    temperatures.append(row[8])

    years.append(row[0])
    countries.append('24N-44N')
    regions.append('24N-44N')
    temperatures.append(row[9])

    years.append(row[0])
    countries.append('EQU-24N')
    regions.append('EQU-24N')
    temperatures.append(row[10])

    years.append(row[0])
    countries.append('24S-EQU')
    regions.append('24S-EQU')
    temperatures.append(row[11])

    years.append(row[0])
    countries.append('44S-24S')
    regions.append('44S-24S')
    temperatures.append(row[12])

    years.append(row[0])
    countries.append('64S-44S')
    regions.append('64S-44S')
    temperatures.append(row[13])

    years.append(row[0])
    countries.append('90S-64S')
    regions.append('90S-64S')
    temperatures.append(row[14])

raw_data = {
    "Country": countries,
    "Year": years,
    "Region": regions,
    "Temperature": temperatures
}

ndf = pd.DataFrame(raw_data, columns=['Country', 'Year', 'Region', 'Temperature'])
ndf.to_csv("regions_year_ds.csv", index=False)