# Geoparser

This script mines text for geographical place-names and plots their coordinates on a map. It is intended for use with historical documents and classical works so as to quickly visualize their "spatial footprint." For a comprehensive look at the inspiration, aims, and practical applications of this tool, please see [my post on Towards Data Science](https://towardsdatascience.com/geoparsing-with-python-c8f4c9f78940).

## How to Use this Repo

Clone the repo and run the following command into your terminal:

`python geoparser.py [argument]`

Pass the .txt you'd like to geoparse as an argument.

The jupyter notebook provides a sample to demonstrate each step taken by the script to get the final plot. Other world maps and coordinate systems may be used. Please note that in order to get coordinates, the script makes API calls to [OpenStreetMap](https://www.openstreetmap.org/); this process can take a long time if your text contains many city-names. 