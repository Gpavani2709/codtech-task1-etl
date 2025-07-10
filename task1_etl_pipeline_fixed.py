import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# ✅ Confirm the correct script is running
print("✅ Running task1_etl_pipeline_fixed.py...")

# Load the dataset
df = pd.read_csv("android-games (1).csv")  # Make sure this file exists in the same folder

# Clean 'installs' column
def clean_installs(value):
    if isinstance(value, str):
        value = value.strip().upper()
        if 'M' in value:
            return float(value.replace('M', '')) * 1_000_000
        elif 'K' in value:
            return float(value.replace('K', '')) * 1_000
        elif 'B' in value:
            return float(value.replace('B', '')) * 1_000_000_000
        else:
            return np.nan
    return value

df['installs'] = df['installs'].apply(clean_installs)

# Drop unused columns
df_cleaned = df.drop(columns=['rank', 'title'])

# Define features
numerical_features = [
    'total ratings', 'installs', 'average rating', 'growth (30 days)',
    'growth (60 days)', 'price', '5 star ratings', '4 star ratings',
    '3 star ratings', '2 star ratings', '1 star ratings'
]
categorical_features = ['category', 'paid']

# Define transformers
numeric_transformer = Pipeline([
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline([
    ('onehot', OneHotEncoder(drop='first'))
])

# Combine transformers
preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numerical_features),
    ('cat', categorical_transformer, categorical_features)
])

# Transform the data
X_processed = preprocessor.fit_transform(df_cleaned)

# Convert sparse to dense
if hasattr(X_processed, "toarray"):
    X_processed = X_processed.toarray()

# ✅ Final fix: use get_feature_names_out
encoded_cat_columns = preprocessor.named_transformers_['cat'].named_steps['onehot'].get_feature_names_out(categorical_features)
all_columns = numerical_features + list(encoded_cat_columns)

# Create final DataFrame and save to CSV
df_final = pd.DataFrame(X_processed, columns=all_columns)
df_final.to_csv("android_games_cleaned.csv", index=False)

print("🎉 Done! Cleaned data saved to android_games_cleaned.csv")


