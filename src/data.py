# Functions for loading and merging data from CSV files.

import pandas as pd

def load_data(features="raw_data/elliptic_txs_features.csv",
              classes="raw_data/elliptic_txs_classes.csv"):
    features = pd.read_csv(features)
    classes = pd.read_csv(classes)
    return features, classes

def merge_data(features, classes, on="txId"):
    return pd.merge(features, classes, on=on)
