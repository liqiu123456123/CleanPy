import pandas as pd

def fill_missing_values(df, method='mean', column=None):
    if column:
        if method == 'mean':
            df[column].fillna(df[column].mean(), inplace=True)
        elif method == 'median':
            df[column].fillna(df[column].median(), inplace=True)
        elif method == 'mode':
            df[column].fillna(df[column].mode()[0], inplace=True)
        elif method == 'ffill':
            df[column].fillna(method='ffill', inplace=True)
        elif method == 'bfill':
            df[column].fillna(method='bfill', inplace=True)
    return df

def drop_missing_values(df, axis=0):
    return df.dropna(axis=axis)

def mark_missing_values(df, column=None, marker='missing'):
    if column:
        df[column + '_is_missing'] = df[column].isnull().astype(int)
    else:
        for col in df.columns:
            df[col + '_is_missing'] = df[col].isnull().astype(int)
    return df
