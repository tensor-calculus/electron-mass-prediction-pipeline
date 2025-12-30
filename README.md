# Electron Mass Prediction Pipeline
This project is a demonstration of an end to end ML pipeline that loads data from local disk using Apache Airflow, processes that data in Apache Spark and then writes the data to PostgreSQL database, all of which are
running in docker containers.

## Data
The dataset is taken from kaggle.

## Training
GBTRegressor (ensemble learning) from Spark's MLlib is used for performing the regression task. Spark divides the data into chunks that are distributed to different cores of the CPU. Instead of looking at every single value spark converts the continuous data into bins and uses that for splitting a tree branch. Since GBTRegressor passes through the data, it only needs a part of data at a time not the whole dataset. It is not exactly an online algorithm but its a batch algorithm that is sequential, hence a good fit for when data doesnt fit in memory.

## Results
RMSE 1.24, MAE: 0.74, R2: 0.99
