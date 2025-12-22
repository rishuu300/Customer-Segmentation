# Customer Personality Segmentation

## Problem statement

In this data science project, you will build a machine learning system which will be able predict the personality of the customer using machine learning algorithms. This project will be very usefull for malls, various stores and companies which are product based. Based on customer's personal details and purchase details, we can cluster them and we can predict the customer's cluster number using classification techniques.

## Solution Proposed

Now the question is how to dynamically predict the cluster of the customer ?. One of the approaches which we can use of machine learning approach, where we can cluster the customer based on the details we have and predict the cluster type based on the domain knowledge and leverage previous customer data to predict the cluster.

Dataset used

<html>
<a href="https://github.com/entbappy/Branching-tutorial/blob/master/marketing_campaign.zip"> Dataset Link</a>
</html>

## Tech Stack Used

1. Python
2. Flask
3. Machine learning algorithms
4. Docker
5. MongoDB

## Infrastructure required

1. HuggingFace Spaces

## How to run

Before you run this project make sure you have MongoDB Atlas account and you have the shipping dataset into it.

Step 1. Cloning the repository.

```

git clone https://github.com/rishuu300/Customer-Segmentation.git

```

Step 2. Create a conda environment.

```

conda create --prefix venv python=3.10 -y

```

```

conda activate venv/

```

Step 3. Install the requirements

```

pip install -r requirements.txt

```

Step 5. Run the application server

```

python app.py

```

## Run locally

1. Check if the Dockerfile is available in the project directory
2. Build the Docker image
3. Run the Docker image

```

docker run -d -p 5000:5000 <IMAGE_NAME>

```

## Models Used

* [K-Means](https://www.javatpoint.com/k-means-clustering-algorithm-in-machine-learning)
* [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)

From these above models after hyperparameter optimization we selected these two models which were K-Means for clustering and Logistic Regression for classification and used the following in Pipeline.

* GridSearchCV is used for Hyperparameter Optimization in the pipeline.

**Components** : Contains all components of Machine Learning Project

- Data Ingestion
- Data Validation
- Data Transformation
- Data Clustering
- Model Trainer
- Model Evaluation
- Model Pusher

## Conclusion

- This Project can be used in real-life by Users.
