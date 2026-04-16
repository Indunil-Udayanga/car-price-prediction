# 🚗 Car Price Prediction System (ML + Flask Web App)

A Machine Learning web application that predicts car prices using features like engine size, year, mileage, manufacturer, and fuel type.

## 🧠 Tech Stack

- 🧠 ML model (trained & optimized)
- ⚙️ Flask backend
- 🎨 HTML/CSS frontend

---

## 📌 Project Overview

This system predicts the price of a car based on historical car sales data.  
Multiple models were tested, and the best-performing model (**Random Forest Regressor**) was selected.

---

## 📊 Dataset Details

- **Dataset:** `car_sales_data.csv`  
- **Target Variable:** `Price`

### 🔑 Input Features
- Engine size  
- Year of manufacture  
- Mileage  
- Manufacturer (encoded)  
- Fuel type (encoded)  

### ❌ Removed Feature
- Model (dropped due to high cardinality / low importance)

---

## 🔧 Data Preprocessing

- Renamed columns:
  - `Fuel type → Fuel_type`
  - `Year of manufacture → Year_of_manufacture`
- Removed unnecessary column: `Model`
- Converted categorical variables using:
  - **One-Hot Encoding (`pd.get_dummies`)**
- Checked for:
  - Missing values  
  - Feature correlation  

---

## 🧠 Models Tested

- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor ✅ (Best)  
- XGBoost Regressor  

---

## 📈 Evaluation Metrics

- MAE (Mean Absolute Error)  
- RMSE (Root Mean Squared Error)  
- R² Score  
- Cross-validation score  

---

## 🏆 Final Model

**Random Forest Regressor**

```python
RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    random_state=42
)

## ⚙️ System Workflow

1. User inputs car details via web interface  
2. Flask backend processes input data  
3. Data is transformed using same preprocessing steps  
4. Trained ML model predicts price  
5. Prediction result is displayed to the user  

---

## 📊 Visualizations

- Correlation heatmap  
- Model comparison graphs (R², RMSE, MAE)  

---

## 📈 Future Improvements

- Expand dataset with more car records  
- Feature engineering (car age, depreciation rate)  
- Hyperparameter tuning  
- Deploy as a live web application  
- Enhance frontend UI/UX  

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to fork and improve the project.

---

## 📜 License

MIT License  

---

## 👨‍💻 Author

**Indunil Udayanga**  
GitHub: https://github.com/Indunil-Udayanga  
