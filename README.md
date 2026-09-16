# 🏠 California Housing Price Predictor

A machine learning web application that predicts the **median house value in California** based on housing, population, income, and geographical features.

The project uses an **XGBoost Regression model** and provides an interactive, professional interface built with **Streamlit**.

---

## 🌐 Live Demo

🔗 **Web Application:**  
https://xgboostproject-amqqgnffgmguovixeqkeot.streamlit.app/

> Replace the URL above with your deployed Streamlit application URL.

---

## 📌 Project Overview

The California Housing Price Predictor is an end-to-end machine learning project designed to estimate house prices using important characteristics of a housing area.

Users can enter values such as:

- Median Income
- House Age
- Average Rooms
- Average Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude

The trained XGBoost model processes these features and generates an estimated median house value.

---

## 🚀 Features

- 🏠 California house price prediction
- 🤖 XGBoost Regression model
- 🖥️ Professional Streamlit web interface
- 📊 8 housing and geographical input features
- ⚡ Fast predictions
- 🎨 Modern dark-themed UI
- 📱 Clean and responsive layout
- 🔮 Real-time prediction results
- ℹ️ Model information section

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| Pandas | Data processing |
| XGBoost | Machine learning model |
| Scikit-learn | Machine learning utilities |
| Streamlit | Web application |
| Pickle | Model serialization |

---

## 📊 Dataset

This project is based on the **California Housing dataset**.

The model uses the following features:

| Feature | Description |
|---------|-------------|
| `MedInc` | Median income of households |
| `HouseAge` | Median age of houses |
| `AveRooms` | Average number of rooms |
| `AveBedrms` | Average number of bedrooms |
| `Population` | Population of the area |
| `AveOccup` | Average household occupancy |
| `Latitude` | Geographical latitude |
| `Longitude` | Geographical longitude |

### Target

The model predicts:

```text
Median House Value
