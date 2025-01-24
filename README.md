Salary Prediction ML Deployment Project

Summary:
This project demonstrates the deployment of a simple machine learning model for predicting salaries based on years of experience. It showcases end-to-end implementation, from data preprocessing and model building to deployment using Flask. 

Problem Statement
The goal is to build a predictive model that estimates an employee's salary based on their years of experience using Simple Linear Regression. 

Tools & Technologies Used
IDE: Anaconda Spyder (for coding and experimentation)
Libraries:
Pandas: Data manipulation and preprocessing
NumPy: Numerical computations
Scikit-learn: Model building and evaluation
Pickle: Model serialization
Flask: Web framework for deployment
Programming Language: Python



Workflow Overview
Dataset Preparation:
Used a dataset with Years of Experience as input and Salary as the target variable.
Performed exploratory data analysis and ensured the data was clean.

Model Development:
Split the dataset into training and testing sets using train_test_split.
Built a Simple Linear Regression model using Scikit-learn's LinearRegression.
Evaluated the model’s accuracy with metrics such as Mean Squared Error (MSE).

Model Serialization:
Saved the trained model to a file using Pickle for easy deployment:

Flask Integration:
Developed a Flask app to serve predictions:
Created a user interface using HTML to input years of experience.
Loaded the saved Pickle model to handle real-time predictions.
Returned the predicted salary dynamically on the webpage.
Application Deployment:
Ran the Flask app locally (http://127.0.0.1:5000/) from Anaconda Spyder for demonstration purposes.

