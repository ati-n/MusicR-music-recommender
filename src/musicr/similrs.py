import pandas as pd

from scipy.sparse import csr_matrix

from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline

from src.musicr.dataconv import artists_pivot, artists_name_list


# Create MaxAbsScaler which scales each feature by max value (by column).
scaler = MaxAbsScaler()

# Dimension reduction
# Create 20 columns from the 500
nmf = NMF(n_components=20)

# Create normalizer
normalizer = Normalizer()

# Feed every created object to a pipeline for easier data handling
pipeline = make_pipeline(scaler, nmf, normalizer)

# Now we need the data as a csr_matrix
artists_csr = csr_matrix(artists_pivot)

# Feed the data into the pipeline
# All numbers normalized between 0 and 1
normalized_features = pipeline.fit_transform(artists_csr)

# Data frame with calculated features and inserted artist's names
#
"""                   0         1    2   ...        17   18        19
Massive Attack  0.000000  0.000000  0.0  ...  0.000000  0.0  0.028967
Sublime         0.000000  0.000000  0.0  ...  0.000000  0.0  0.999984
Beastie Boys    0.000000  0.000000  0.0  ...  0.000000  0.0  0.000000
Neil Young      0.274571  0.000000  0.0  ...  0.000000  0.0  0.018464
Dead Kennedys   0.000000  0.014149  0.0  ...  0.285971  0.0  0.000000
...
"""
df = pd.DataFrame(normalized_features, index=artists_name_list)


def select_artist(artist="Rage Against the Machine"):
    # Access the artist
    access = df.loc[artist]

    # Compute the matrix multiplication between the Data frame
    # and the selected artist.
    # Every artist gets a number (0-1) of how similiar
    # their row is compared to the selected artist.

    # Dot product formula is SUM(i=1..n) aibi
    similar_artists = df.dot(access)

    # The selected artist has the number 1 on the slace
    # The top similar artists have the closest numbers
    print(similar_artists.nlargest())
