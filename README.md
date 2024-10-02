# UAE Real Estate Data Analysis and Price Prediction Website

This data science project series walks through the step-by-step process of building a real estate price prediction website. The project is divided into three main components:

1. **Model Building**: Using the UAE real estate dataset, builded a machine learning model using `sklearn` and linear regression to predict real estate prices based on property features.
2. **Python Flask Server**: Next, developed Python Flask server that loads the trained model and serves HTTP requests for predictions.
3. **Frontend Website**: Finally, created a user-friendly website using HTML, CSS, and JavaScript. This website allows users to input property details (like square feet area, number of bedrooms, etc.) and retrieves predicted prices from the Flask server.

During the model-building phase, we cover almost all core data science concepts, such as data loading and cleaning, outlier detection and removal, feature engineering, dimensionality reduction, `GridSearchCV` for hyperparameter tuning, and K-Fold cross-validation.

## Technologies and Tools Used

- **Python** for backend development
- **Numpy** and **Pandas** for data cleaning
- **Matplotlib** for data visualization
- **Sklearn** for model building
- **Jupyter Notebook**, **Visual Studio Code**, and **PyCharm** as IDEs
- **Python Flask** for creating the HTTP server
- **HTML/CSS/JavaScript** for building the user interface

## Dataset

The dataset contains real estate listings with various features, such as:
- **Price**: Price of the property
- **Location**: Address of the property
- **Size (sqft)**: Size of the property in square feet
- **Bedrooms (BHK)**: Number of bedrooms
- **Bathrooms**: Number of bathrooms
  
You can download the dataset from Kaggle: [UAE Real Estate 2024 Dataset](https://www.kaggle.com/datasets/kanchana1990/uae-real-estate-2024-dataset)

## Key Steps

1. **Data Cleaning**: Handling missing values and converting non-numeric values in the `size`, `bedrooms`, and `bathrooms` columns to numeric values for analysis.
2. **Feature Engineering**: Creating new features such as `Price per Square Feet` to gain deeper insights into property pricing trends.
3. **Outlier Detection**: Identifying and removing outliers to ensure accurate analysis.
4. **Data Visualization**: Visualizing data using histograms, scatter plots, and box plots to understand distributions and relationships between features.
5. **Model Training and Evaluation**: Building a linear regression model, performing hyperparameter tuning with `GridSearchCV`, and evaluating the model using K-Fold cross-validation.
6. **Deploying the Model**: Using Flask to serve the trained model and handle HTTP requests.
7. **Building the User Interface**: Developing a web interface that allows users to enter property details and receive predicted prices.

## Key Steps

![image](https://github.com/user-attachments/assets/c0ef71df-21e4-4663-afbf-baa8054af2fb)

## Usage

To run the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/uae-real-estate-analysis.git
