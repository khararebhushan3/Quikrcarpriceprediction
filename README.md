# Quikrcarpriceprediction
### Boston House Pricing Prediction

### Software And Tools Requirements

1. [Github Account](https://github.com)
2. [VSCodeIDE](https://code.visualstudio.com/)
3. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)
 

Create a new environment

```
conda create -p venv python==3.8 -y
```

# Title: Quikr Car Price Prediction Project

## Description:
The Quikr Car Price Prediction Project is an end-to-end data science project aimed at predicting the price of used cars listed on the Quikr platform. The project utilizes raw data sourced from Kaggle, encompassing various features such as car make, model, year of manufacture, kilometers driven, fuel type, and more. 

### Project Components:
1. **Data Exploration and Preprocessing (Jupyter Notebook)**:
   - The project begins with exploratory data analysis (EDA) and preprocessing in a Jupyter Notebook environment. 
   - Data cleaning, handling missing values, feature engineering, and visualization techniques are employed to understand the dataset better and prepare it for model training.

2. **Model Training and Evaluation (Jupyter Notebook)**:
   - Various machine learning algorithms such as linear regression, random forest, and gradient boosting are trained and evaluated to predict car prices.
   - Model performance metrics such as RMSE, MAE, and R-squared are used to evaluate and compare model performance.

3. **Frontend Development (VS Code)**:
   - Using Flask and HTML, a user-friendly web interface is developed to allow users to input car details and receive predicted car prices.
   - The frontend interface enables users to select car make, model, year of manufacture, kilometers driven, fuel type, and other relevant features.

4. **Deployment on AWS Cloud (NGINX)**:
   - The project is deployed on AWS cloud infrastructure, leveraging NGINX as the web server.
   - The deployment ensures scalability, reliability, and accessibility of the car price prediction service to users.

### Usage:
1. **Data Preparation and Model Training**:
   - Clone the repository and execute the Jupyter Notebook to perform data exploration, preprocessing, and model training.
   - Follow the instructions provided within the notebook to train and evaluate machine learning models.

2. **Frontend Development**:
   - Utilize VS Code or any compatible editor to modify the Flask application and HTML templates to customize the user interface as needed.
   - Ensure all necessary dependencies are installed and configured correctly.

3. **Deployment on AWS Cloud**:
   - Set up an AWS account and configure necessary permissions and resources.
   - Deploy the Flask application on an EC2 instance, and configure NGINX as the web server to serve the application.
   - Ensure proper security measures and monitoring tools are in place to maintain the availability and performance of the deployed application.

### Conclusion:
The Quikr Car Price Prediction Project demonstrates the end-to-end process of developing a machine learning solution for predicting used car prices and deploying it as a user-friendly web application on the AWS cloud. By providing transparency into the model's predictions, users can make informed decisions when buying or selling cars on the Quikr platform.
