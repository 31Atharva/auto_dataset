import pickle

# Correct path to the trained model
model = pickle.load(open('/Users/atharvadumbre/DataScience/Machine Learning/Linear Regression/Linear Regression Dataset/auto/models/trained_model.pkl', 'rb'))

# Check if the model is loaded
print("Model loaded successfully")
