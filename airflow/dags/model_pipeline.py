from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your custom modules
from weather_import import fetch_data
from data_preprocessing import process_data

# Model training function
def train_model():
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    import mlflow
    import mlflow.sklearn
    from mlflow.models.signature import infer_signature

    # Load the preprocessed data
    data = pd.read_csv('/home/mustfain/Desktop/MLOPS-Project/weather-prediction-mlflow-dvc/data/processed_data.csv')

    # Define features (independent variables) and target (dependent variable)
    X = data[['Humidity', 'Wind Speed', 'Weather Condition']]  # Replace with actual column names
    y = data['Temperature']  # Replace with the column name for temperature

    # One-Hot Encode the 'Weather Condition' column
    X_encoded = pd.get_dummies(X, columns=['Weather Condition'], drop_first=True)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

    # Set MLflow tracking URI (optional, adjust based on your setup)
    mlflow.set_tracking_uri('http://localhost:5000')  # Uncomment if using a remote MLflow server

    # Start an MLflow run
    with mlflow.start_run():
        # Train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Log parameters (example)
        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_param("test_size", 0.2)

        # Log metrics (example)
        score = model.score(X_test, y_test)
        mlflow.log_metric("r2_score", score)

        # Log the model with an input example and signature
        input_example = X_train.iloc[0].to_dict()  # Use the first row of X_train as an example
        signature = infer_signature(X_train, model.predict(X_train))  # Infer the signature based on the input/output

        mlflow.sklearn.log_model(model, "model", input_example=input_example, signature=signature)

        # Register the model in the MLflow Model Registry (optional, manage stages)
        model_uri = f"runs:/{mlflow.active_run().info.run_id}/model"
        mlflow.register_model(model_uri, "weather_model")

        # Transition the model to the "Staging" stage (example)
        client = mlflow.tracking.MlflowClient()
        client.transition_model_version_stage(
            name="weather_model", version=1, stage="Staging"
        )

        print(f"Model trained with R² score: {score}")
        print("Model saved in MLflow tracking server.")
        print(f"Model registered and transitioned to Staging stage.")

# Define the DAG
default_args = {
    'start_date': datetime(2024, 11, 26),
    'retries': 1,
}

with DAG(
    dag_id="model_pipeline",
    default_args=default_args,
    schedule_interval=None,  # Set None for manual triggering
    catchup=False,
    description="Pipeline to fetch, process, and train a model with weather data",
) as dag:

    # Task 1: Fetch Data
    task_fetch_data = PythonOperator(
        task_id="fetch_data",
        python_callable=fetch_data
    )

    # Task 2: Process Data
    task_process_data = PythonOperator(
        task_id="process_data",
        python_callable=process_data
    )

    # Task 3: Train Model
    task_train_model = PythonOperator(
        task_id="train_model",
        python_callable=train_model
    )

    # Define task dependencies
    task_fetch_data >> task_process_data >> task_train_model
