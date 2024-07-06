def identify_duplicates(df):
    return df[df.duplicated()]

def drop_duplicates(df):
    return df.drop_duplicates()

def merge_duplicates(df, by, method='mean'):
    return df.groupby(by).agg(method).reset_index()
