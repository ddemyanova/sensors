from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


class LNormalizer(BaseEstimator, TransformerMixin):
    def __init__(self, norm_ord=2):
        self.norm_ord = norm_ord
        self.row_norm_vals = None

    def fit(self, X, y=None):
        self.row_norm_vals = np.linalg.norm(X, ord=self.norm_ord, axis=0)

    def transform(self, X, y=None):
        return X / self.row_norm_vals

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X, y)

    def get_norm_vals(self):
        return self.row_norm_vals
