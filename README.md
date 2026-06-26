📖 Project Overview

AI-Based Prediction in Smart Farming is an intelligent agriculture support system that leverages Artificial Intelligence (AI) and Machine Learning (ML) to assist farmers in making informed decisions.

The application analyzes soil nutrients, environmental conditions, and agricultural parameters to provide smart predictions and recommendations. The project integrates multiple machine learning models into a single interactive Streamlit dashboard.

The system includes three major modules:

🌾 Crop Recommendation
📈 Crop Yield Prediction
🧪 Fertilizer Recommendation

The objective is to improve agricultural productivity, reduce resource wastage, and support sustainable farming practices.

✨ Features

✅ Crop Recommendation based on soil nutrients and weather conditions

✅ Crop Yield Prediction using historical agricultural data

✅ Fertilizer Recommendation according to soil and crop type

✅ Interactive Streamlit Dashboard

✅ Machine Learning based prediction models

✅ User-friendly graphical interface

✅ Real-time prediction results

📊 Datasets

The project uses publicly available agricultural datasets from Kaggle.

🌾 Crop Recommendation Dataset

https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset

Features

Nitrogen (N)
Phosphorus (P)
Potassium (K)
Temperature
Humidity
pH
Rainfall

Target

Crop Label
📈 Crop Yield Prediction Dataset

https://www.kaggle.com/datasets/patelris/crop-yield-prediction-dataset

Features

Area
Crop Item
Year
Average Rainfall
Pesticides Used
Average Temperature

Target

Crop Yield (hg/ha)
🧪 Fertilizer Recommendation Dataset

https://www.kaggle.com/datasets/gdabhishek/fertilizer-prediction

Features

Temperature
Humidity
Moisture
Soil Type
Crop Type
Nitrogen
Potassium
Phosphorous

Target

Fertilizer Name
🤖 Machine Learning Models
Module	Algorithm
Crop Recommendation	Random Forest Classifier
Crop Yield Prediction	Random Forest Regressor
Fertilizer Recommendation	Random Forest Classifier
🛠 Technologies Used
Programming Language
Python
Libraries
Pandas
NumPy
Scikit-learn
Joblib
Framework
Streamlit
Development Tools
Visual Studio Code
Git
GitHub
📈 Model Evaluation
Module	Evaluation Metric	Result
Crop Recommendation	Accuracy	99.31%
Crop Yield Prediction	R² Score	98.57%
Crop Yield Prediction	MAE	3741.53
Fertilizer Recommendation	Accuracy	13.81%
🚀 Installation
Clone Repository
git clone https://github.com/sarvottam-mnc/AI-based-Prediction-in-Smart-Farming.git
Navigate to Project
cd AI-based-Prediction-in-Smart-Farming
Install Dependencies
pip install -r requirements.txt
Run Application
streamlit run app.py
📂 Project Structure
AI-Based-Prediction-in-Smart-Farming/
│
├── app.py
├── requirements.txt
├── README.md
│
├── crop_model.pkl
├── yield_model.pkl
├── fertilizer_model.pkl
│
├── area_encoder.pkl
├── crop_encoder.pkl
├── fert_encoder.pkl
├── item_encoder.pkl
├── soil_encoder.pkl
│
├── Crop_recommendation.csv
├── yield_df.csv
├── data_core.csv
│
├── images/
│   ├── crop.jpg
│   ├── yield.jpg
│   └── fertilizer.jpg
│
└── notebooks/
🔄 Workflow
User Input
      │
      ▼
Data Preprocessing
      │
      ▼
Machine Learning Model
      │
      ▼
Prediction
      │
      ▼
Streamlit Dashboard
      │
      ▼
Recommendation / Result
🎯 Future Improvements
Integration with real-time weather APIs
IoT sensor-based smart farming
Deep Learning models for higher accuracy
Plant disease detection using computer vision
Mobile application for farmers
Multilingual support
Market price prediction
Cloud deployment for public access
👨‍💻 Developer

Sarvottam Kumar

Entry No: 24BCN036

Branch: Mathematics & Computing

Internship Area: Artificial Intelligence & Machine Learning

🙏 Acknowledgement

I sincerely thank my project mentor for valuable guidance and continuous support throughout the development of this project. This project provided me with practical experience in Machine Learning, data preprocessing, model evaluation, Streamlit application development, Git, and GitHub.

⭐ If you found this project helpful, please consider giving it a Star on GitHub!
