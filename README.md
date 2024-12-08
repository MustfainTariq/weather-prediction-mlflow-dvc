# Project README

## Overview

This project integrates multiple tools and technologies, including Apache Airflow for workflow orchestration, MLflow for managing machine learning models, and a web application with both backend and frontend components. It is designed to automate and manage data pipelines, track machine learning experiments, and serve the application via a web interface.

## Setup and Installation

Follow the instructions below to set up and run the project.

### 1. Install Apache Airflow

Apache Airflow is used for orchestrating the data pipeline tasks. To install and set up Apache Airflow:

# Define the desired version of Airflow
AIRFLOW_VERSION=2.7.3  # Check the latest version on the official website

# Get the Python version and install Airflow with appropriate constraints
PYTHON_VERSION="$(python3 --version | cut -d ' ' -f 2 | cut -d '.' -f 1-2)"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
2. Initialize Airflow Database
Before starting the Airflow scheduler and web server, initialize the Airflow database:


airflow db init
3. Start Airflow Services
Run the Airflow scheduler and web server:

# Start the scheduler
airflow scheduler

# Start the web server on port 8080
airflow webserver --port 8080
4. Install MLflow
MLflow is used to track machine learning experiments, models, and results. To install MLflow, run:


pip install mlflow
5. Install Backend Dependencies
Ensure the backend application is ready by installing the necessary dependencies and running the server:


# Install any required dependencies (if needed, via requirements.txt)
pip install -r requirements.txt

# Start the backend application
python3 app.py
6. Install Frontend Dependencies
To set up and run the frontend application:


# Install frontend dependencies
npm install

# Start the frontend development server
npm start
Running the Project
Trigger Data Pipeline (Airflow)
To trigger the data pipeline via Airflow, use the following command:


airflow dags trigger data_pipeline
This will initiate the specified data pipeline within Airflow.

Run MLflow UI
To view and manage machine learning experiments and models, run the MLflow UI:


mlflow ui
The MLflow UI will be available at http://localhost:5000 by default.

Project Workflow
The project follows this general flow:

Data Pipeline Execution (Airflow): The data pipeline is orchestrated using Airflow. You can trigger the pipeline manually using the Airflow CLI (airflow dags trigger data_pipeline).
Model Training and Tracking (MLflow): As part of the pipeline, machine learning models are trained and tracked using MLflow. The MLflow UI provides a dashboard to view experiment details and model versions.
Backend and Frontend Interaction: The backend (app.py) serves as the core of the application, interacting with the data pipeline and MLflow. The frontend is responsible for displaying results and providing a user interface to interact with the system.
Troubleshooting
Airflow Web Server Not Starting: Ensure that the Airflow database is initialized with airflow db init. If errors persist, check the logs for additional details.
MLflow UI Not Accessible: Make sure the MLflow UI is running on the default port (5000). If necessary, change the port with the --port flag.
Conclusion
This README provides all the steps necessary to set up and run the project. If you encounter any issues during setup or execution, please check the logs and review the configuration settings for each component.
