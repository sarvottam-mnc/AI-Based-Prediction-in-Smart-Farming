import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# Load dataset
df = pd.read_csv("yield_df.csv")

# Drop unwanted column
if "Unnamed: 0" in df.columns:
    df.drop("Unnamed: 0", axis=1, inplace=True)

# Encode categorical columns
area_encoder = LabelEncoder()
item_encoder = LabelEncoder()

df["Area"] = area_encoder.fit_transform(df["Area"])
df["Item"] = item_encoder.fit_transform(df["Item"])

# Features and target
X = df.drop("hg/ha_yield", axis=1)
y = df["hg/ha_yield"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Evaluation
print("R2 Score:", r2_score(y_test, pred))
print("MAE:", mean_absolute_error(y_test, pred))

# Save model and encoders
joblib.dump(model, "yield_model.pkl")
joblib.dump(area_encoder, "area_encoder.pkl")
joblib.dump(item_encoder, "item_encoder.pkl")

print("Yield model saved successfully!")