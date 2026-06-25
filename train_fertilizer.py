import pandas as pd

import joblib

from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

df = pd.read_csv("data_core.csv")

soil_encoder = LabelEncoder()

crop_encoder = LabelEncoder()

fert_encoder = LabelEncoder()

df["Soil Type"] = soil_encoder.fit_transform(df["Soil Type"])

df["Crop Type"] = crop_encoder.fit_transform(df["Crop Type"])

df["Fertilizer Name"] = fert_encoder.fit_transform(df["Fertilizer Name"])

X = df.drop("Fertilizer Name", axis=1)

y = df["Fertilizer Name"]

X_train, X_test, y_train, y_test = train_test_split(

X, y, test_size=0.2, random_state=42

)

model = RandomForestClassifier(n_estimators=200, random_state=42)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Fertilizer Accuracy:", accuracy_score(y_test, pred))

joblib.dump(model, "fertilizer_model.pkl")

joblib.dump(soil_encoder, "soil_encoder.pkl")

joblib.dump(crop_encoder, "crop_encoder.pkl")

joblib.dump(fert_encoder, "fert_encoder.pkl")

print("Fertilizer model saved")