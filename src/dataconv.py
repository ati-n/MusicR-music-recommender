import pandas as pd

# Read the CSV file with raw data
artists = pd.read_csv("../util/data.csv")

# Dimension tightening, no need for empty values
# One column: Users and 500 rows: How many times a user played an artist
"""
              playcount                        ...                          
user_offset           0    1    2   3   4   5  ... 494  495 496 497  498 499
artist_offset                                  ...                          
0                     0    0  105   0   0   0  ...   0    0   0   0    0   0
1                   128  211    0   0   0   0  ...   0  105  97   0    0   0
2                     0    0    0   0   0   0  ...   0    0   0   0    0   0
3                     0    0    0   0   0   0  ...   0    0   0   0    0   0
...
"""
artists_pivot = artists.pivot_table(index="artist_offset", columns="user_offset", fill_value=0)



