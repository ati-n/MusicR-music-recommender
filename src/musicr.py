import numpy as np

from scipy.sparse import csr_matrix

from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline

import dataconv

artists = dataconv.artists_pivot






print(artists.head)