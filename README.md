# 🏠 California House Price Predictor

This project predicts median house prices in California using data from the 1990 U.S. Census. It includes:

- Data preprocessing with `ColumnTransformer`
- Model training using `KNeighborsRegressor`
- Hyperparameter tuning with `GridSearchCV`
- Evaluation using R², MSE, RMSE
- Deployment via FastAPI with a `/predict` endpoint

## 🚀 Try It

1. Clone the repo
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the API:
   `uvicorn main:app --reload`

Then go to `http://127.0.0.1:8000/docs` to try it out.

## 📁 Files

- `main.py`: FastAPI app
- `house_price_predictor.ipynb`: Notebook workflow
- `requirements.txt`: Required packages
- `california_knn_regressor.pkl`: Trained model

## 📌 Author

- LinkedIn: [Naomi Jepkorir Kimaiyo](http://linkedin.com/in/naomi-jepkorir-kimaiyo/)

- GitHub: [@Kimaiyoo](https://github.com/Kimaiyoo)

- Email: naomijepkorir18@gmail.com
