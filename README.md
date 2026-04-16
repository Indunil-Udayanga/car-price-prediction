🚗 Car Price Prediction System (ML + Flask Web App)

A Machine Learning web application that predicts car prices using features like engine size, year, mileage, manufacturer, and fuel type.

This project combines:

🧠 ML model (trained & optimized)
⚙️ Flask backend
🎨 HTML/CSS frontend
📌 Project Overview

This system predicts the price of a car based on historical car sales data.
Multiple models were tested, and the best-performing model (Random Forest Regressor) was selected.

📊 Dataset Details
Dataset: car_sales_data.csv
Target Variable: Price
🔑 Input Features
Engine size
Year of manufacture
Mileage
Manufacturer (encoded)
Fuel type (encoded)
❌ Removed Feature
Model (dropped due to high cardinality / low importance)
🔧 Data Preprocessing
Renamed columns:
Fuel type → Fuel_type
Year of manufacture → Year_of_manufacture
Removed unnecessary column: Model
Converted categorical variables using:
One-Hot Encoding (pd.get_dummies)
Checked for:
Missing values
Feature correlation
🧠 Models Tested
Linear Regression
Decision Tree Regressor
Random Forest Regressor ✅ (Best)
XGBoost Regressor
📈 Evaluation Metrics
MAE (Mean Absolute Error)
RMSE (Root Mean Squared Error)
R² Score
Cross-validation score
🏆 Final Model

Random Forest Regressor

RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    random_state=42
)

✔ Selected due to:

Higher prediction accuracy
Lower error values
Better generalization
📂 Project Structure
car-price-prediction/
│
├── dataset/
│   └── car_sales_data.csv
│
├── model/
│   └── car_price_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── app.py
├── car_price_predictin.ipynb
├── requirements.txt
└── README.md
⚙️ System Workflow
User inputs car details via web interface
Flask backend processes input data
Data is transformed using same preprocessing steps
Trained ML model predicts price
Prediction result is displayed to the user
🔮 Example Prediction Input
new_car = {
    "Engine size": 3.5,
    "Year_of_manufacture": 1999,
    "Mileage": 93695,
    "Manufacturer_Porsche": 1,
    "Fuel_type_Petrol": 1
}

➡️ Model outputs predicted car price

📊 Visualizations
Correlation heatmap
Model comparison graphs (R², RMSE, MAE)
🌟 Key Insights
Year, Mileage, and Engine Size are the most important features
Manufacturer significantly affects pricing
Random Forest performs better than linear models for this dataset
📈 Future Improvements
Expand dataset with more car records
Feature engineering (car age, depreciation rate)
Hyperparameter tuning
Deploy as a live web application
Enhance frontend UI/UX
🤝 Contributing

Contributions are welcome! Feel free to fork and improve the project.

📜 License

MIT License

👨‍💻 Author

Indunil Udayanga
GitHub: https://github.com/Indunil-Udayanga
