import pandas as pd

def auto_convert_types(df):
    for column in df.columns:
        if df[column].dtype == 'object':
            try:
                df[column] = pd.to_datetime(df[column])
            except ValueError:
                try:
                    df[column] = pd.to_numeric(df[column])
                except ValueError:
                    pass
    return df
