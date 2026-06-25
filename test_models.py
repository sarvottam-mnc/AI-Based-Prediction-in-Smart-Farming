import joblib

crop_model = joblib.load("crop_model.pkl")
yield_model = joblib.load("yield_model.pkl")

print("All models loaded successfully")