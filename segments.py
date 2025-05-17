import pandas as pd
from sklearn.cluster import KMeans

def segment_customers(df):
    features = df[["age", "purchase_count", "avg_spent", "last_purchase_days_ago"]]
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['segment'] = kmeans.fit_predict(features)
    
    return df, kmeans
