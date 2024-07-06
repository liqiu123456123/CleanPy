import numpy as np
from sklearn.ensemble import IsolationForest

def detect_outliers(df, method='zscore', column=None):
    if method == 'zscore' and column:
        mean = np.mean(df[column])
        std = np.std(df[column])
        df['outlier'] = (np.abs(df[column] - mean) > 3 * std).astype(int)
    elif method == 'iqr' and column:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        df['outlier'] = ((df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR))).astype(int)
    elif method == 'isolation_forest':
        clf = IsolationForest(contamination=0.1)
        df['outlier'] = clf.fit_predict(df)
        df['outlier'] = df['outlier'].map({1: 0, -1: 1})
    return df

def handle_outliers(df, method='drop'):
    if method == 'drop':
        return df[df['outlier'] == 0].drop(columns=['outlier'])
    elif method == 'replace':
        df.loc[df['outlier'] == 1, df.columns] = np.nan
        return df.drop(columns=['outlier']).fillna(df.mean())
