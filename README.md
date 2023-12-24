# Flask Advertising API
## Overview
Welcome to the Flask Advertising API! This API is designed to provide predictions, ingest new data, and retrain a machine learning model based on advertising data.

## Getting Started
### Prerequisites
Make sure you have the following installed:

+ Python 3.8-slim
+ Flask
+ SQLite3
+ Required Python packages (install them using pip install -r requirements.txt)

**Note**: If you run the app with Docker, the dockerfile will install it all for you.

### Installation
1. Clone the repository:

```git clone https://github.com/agui968/advertising_API.git ```

2. Change to the project directory:

```cd advertising_API```

### Usage

#### Using Docker
1. Pull the Docker image from the repository:

```docker pull agui968/my-advertising-app:v1```

2. Run the Docker container:

```docker run -p 5000:5000 agui968/my-advertising-app:v1```

The API will be accessible at http://localhost:5000/.

#### Using Python

1. Install dependencies:

```pip install -r requirements.txt```

2. Run the Flask application:

```python app_model.py```

The API will be accessible at http://0.0.0.0:5000/.

2. Endpoints:

+ **Predict Endpoint**: POST /predict

  + Provide input data in the request body: {"data": [[100, 100, 200]]}

+ **Ingest Endpoint**: POST /ingest

  + Ingest new data by providing an array of rows in the request body.
+ Retrain Endpoint: POST /retrain

  + Retrain the machine learning model using existing data in the SQLite database.

3. Visit the root endpoint:
+ GET /: Welcome to the Advertising API.

## Project Structure
+ create_database.py: script to create a SQL database from the original CSV advertising file (no need to run it, since it's already created)
+ app_model.py: The main Flask application including all endpoints.
+ data/: Directory containing the SQLite database (Advertising.db) and machine learning model files.
+ requirements.txt: List of Python dependencies.
+ Dockerfile: file to deploy the app on Docker.
+ test_api.py: file to run with pytest and check the correct functioning of the app.


Feel free to explore and enhance the API for your specific use case!
