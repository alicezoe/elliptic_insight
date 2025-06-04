# Functions for cleaning, transforming, splitting, and feature engineering.

from sklearn.model_selection import train_test_split

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def split_data(df, target_column="class", test_size=0.2, random_state=42):
    X = df.drop(columns=[target_column])
    y = df[target_column]

    return train_test_split(X, y, test_size=test_size, random_state=random_state)
