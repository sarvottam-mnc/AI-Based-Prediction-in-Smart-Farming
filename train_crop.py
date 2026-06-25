import pandas as pd

import joblib

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

df = pd.read_csv("Crop_recommendation.csv")

X = df.drop("label", axis=1)

y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(

X, y, test_size=0.2, random_state=42

)

model = RandomForestClassifier(n_estimators=200, random_state=42)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Crop Accuracy:", accuracy_score(y_test, pred))

joblib.dump(model, "crop_model.pkl")

print("Crop model saved")