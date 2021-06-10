import numpy as np

from scipy.sparse import csr_matrix

from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline

import dataconv

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
artists_csr = csr_matrix(dataconv.artists_pivot)

# Feed the data into the pipeline
normalized_features = pipeline.fit_transform(artists_csr)


def printout():
    print("Normalized features' shape:", normalized_features.shape)
    print("Artists:", dataconv.artists_name_list)


