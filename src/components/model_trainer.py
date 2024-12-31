import os, sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error,accuracy_score
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor, BaggingRegressor, ExtraTreesRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from sklearn.model_selection import GridSearchCV
from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str=os.path.join('artifacts',"model.pkl")
    model_metrics_path: str=os.path.join('artifacts',"model_metrics.txt")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Model trainer initiated")
            x_train, y_train, x_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models = {
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "ElasticNet": ElasticNet(),
                "KNeighborsRegressor": KNeighborsRegressor(),
                "DecisionTreeRegressor": DecisionTreeRegressor(),
                "RandomForestRegressor": RandomForestRegressor(),
                "GradientBoostingRegressor": GradientBoostingRegressor(),
                "AdaBoostRegressor": AdaBoostRegressor(),
                "BaggingRegressor": BaggingRegressor(),
                "ExtraTreesRegressor": ExtraTreesRegressor()
            }

            params={
                "Linear Regression":{},
                "Lasso":{
                    'alpha': [0.1, 1.0, 10.0],
                },
                "Ridge":{
                    'alpha': [0.1, 1.0, 10.0],
                },
                "ElasticNet":{
                    'alpha': [0.1, 1.0],
                    'l1_ratio': [0.1, 0.5, 1],
                    'tol': [0.01, 0.1],
                },
                "KNeighborsRegressor":{
                    'n_neighbors': [3, 5, 7],
                    'weights': ['uniform', 'distance'], 
                    'p': [1, 2],
                },
                "DecisionTreeRegressor":{
                    'criterion': ['squared_error','absolute_error'],
                    'splitter': ['best', 'random'],
                    'max_depth': [None, 10, 20, 50, 100],
                    'min_samples_split': [2, 5],
                    'min_samples_leaf': [1, 2, 4],
                },
                "RandomForestRegressor":{
                    'n_estimators': [10, 50, 100],
                    'criterion': ['squared_error', 'absolute_error'],
                    'max_depth': [None, 10, 20, 50, 100],
                    'min_samples_split': [2, 5],
                    'min_samples_leaf': [1, 2, 4],
                },
                "GradientBoostingRegressor":{
                    'n_estimators': [10, 50, 100],
                    'learning_rate': [0.01, 0.1, 1],
                    'max_depth': [None, 10, 20, 50, 100],
                    'min_samples_split': [2, 5],
                    'min_samples_leaf': [1, 2, 4],
                },
                "AdaBoostRegressor":{
                    'n_estimators': [10, 50, 100], 
                    'learning_rate': [0.01, 0.1, 1],
                },
                "BaggingRegressor":{
                    'n_estimators': [10, 50, 100],
                    'max_samples': [0.1, 0.5, 1.0],
                    'max_features': [0.1, 0.5, 1.0],
                },
                "ExtraTreesRegressor":{
                    'n_estimators': [10, 50, 100],
                    'criterion': ['squared_error', 'absolute_error'],
                    'max_depth': [None, 10, 20, 50, 100],
                    'min_samples_split': [2, 5],
                    'min_samples_leaf': [1, 2, 4],
                }
                }
            model_metrics = {
                "Model": [],
                "R2 Score": [],
                "Mean Squared Error": [],
                "Mean Absolute Error": [],
            }

            for model_name, model in models.items():
                grid_search = GridSearchCV(model, params[model_name], cv=2, n_jobs=1, verbose=1, scoring='r2')
                logging.info(f"Training {model_name}")
                grid_search.fit(x_train, y_train)
                y_pred = grid_search.predict(x_test)
                logging.info(f"Prediction completed for {model_name}")
                r2 = r2_score(y_test, y_pred)
                mse = mean_squared_error(y_test, y_pred)
                mae = mean_absolute_error(y_test, y_pred)
                logging.info(f"Metrics calculated for {model_name}")
                logging.info(f"R2 Score: {r2}")
                logging.info(f"Mean Squared Error: {mse}")
                logging.info(f"Mean Absolute Error: {mae}")

                model_metrics["Model"].append(model_name)
                model_metrics["R2 Score"].append(r2)
                model_metrics["Mean Squared Error"].append(mse)
                model_metrics["Mean Absolute Error"].append(mae)

            logging.info("Saving model metrics")
            df_model_metrics = pd.DataFrame(model_metrics)
            df_model_metrics = df_model_metrics.sort_values(by="R2 Score", ascending=False)
            df_model_metrics.to_csv(self.model_trainer_config.model_metrics_path, index=False)
            logging.info("Model metrics saved")

            logging.info("Saving model")
            best_model = grid_search.best_estimator_
            save_object(file_path=self.model_trainer_config.trained_model_file_path, obj= best_model)
            logging.info("Model saved successfully")

            logging.info("Model trainer completed")
            return self.model_trainer_config.trained_model_file_path, self.model_trainer_config.model_metrics_path

        except Exception as e:
            raise CustomException(e,sys)
