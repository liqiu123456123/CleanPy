import pandas as pd

def convert_time_format(df, column, format='%Y-%m-%d'):
    df[column] = pd.to_datetime(df[column], format=format)
    return df

def encode_categorical(df, column, method='onehot'):
    if method == 'onehot':
        return pd.get_dummies(df, columns=[column])
    elif method == 'label':
        df[column] = df[column].astype('category').cat.codes
    return df
