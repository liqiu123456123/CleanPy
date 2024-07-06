from sklearn.preprocessing import StandardScaler, MinMaxScaler

def standardize_features(df, columns):
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def normalize_features(df, columns, range_min=0, range_max=1):
    scaler = MinMaxScaler(feature_range=(range_min, range_max))
    df[columns] = scaler.fit_transform(df[columns])
    return df
