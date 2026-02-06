# Iris Classification Model Deployment Manifest

## Model Information
- **Model Name**: iris_model.joblib
- **Model Type**: Support Vector Machine (SVM)
- **Kernel**: RBF
- **C Parameter**: 1.0

## Performance Metrics
- **Accuracy**: 97.78%
- **Precision**: 97.78%
- **Recall**: 97.78%
- **F1 Score**: 97.78%
- **Cross-validation Accuracy**: 96.67% ± 3.33%

## Feature Information
- **Input Features**:
  1. Sepal Length (cm)
  2. Sepal Width (cm)
  3. Petal Length (cm)
  4. Petal Width (cm)
- **Target Classes**: 
  - Setosa (0)
  - Versicolor (1)
  - Virginica (2)

## Preprocessing Requirements
- Features must be scaled using StandardScaler with the same fit as training data
- Input data should be in the same order as the feature list above
- Values should be provided in centimeters as floating point numbers

## Deployment Notes
- Model file has been saved to 'iris_model.joblib' using joblib serialization
- To load the model: `model = joblib.load('iris_model.joblib')`
- Model expects scaled feature values in a numpy array format
- Returns predicted class as integer (0, 1, or 2)

## Model Selection Justification
SVM was selected as the final model due to its superior performance compared to Random Forest (95.56% accuracy) and Decision Tree (93.33% accuracy) classifiers. The SVM model perfectly classified Setosa samples and showed excellent discrimination between Versicolor and Virginica with only one misclassification.
