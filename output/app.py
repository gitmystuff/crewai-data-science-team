import gradio as gr
import joblib
import numpy as np

# Load the model and scaler
model = joblib.load('iris_model.joblib')
scaler = joblib.load('scaler.joblib')

def predict_iris(sepal_len, sepal_wid, petal_len, petal_wid):
    # Prepare input
    input_data = np.array([[sepal_len, sepal_wid, petal_len, petal_wid]])
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)
    
    # Map numerical prediction back to Iris species name
    species = ['Setosa', 'Versicolor', 'Virginica']
    return species[int(prediction[0])]

# Updated Modern Gradio Syntax
demo = gr.Interface(
    fn=predict_iris,
    inputs=[
        gr.Number(label="Sepal Length (cm)", value=5.1),
        gr.Number(label="Sepal Width (cm)", value=3.5),
        gr.Number(label="Petal Length (cm)", value=1.4),
        gr.Number(label="Petal Width (cm)", value=0.2)
    ],
    outputs=gr.Textbox(label="Predicted Species"),
    title="Iris Species Classifier",
    description="Enter the flower measurements to predict the species."
)

if __name__ == "__main__":
    demo.launch()

# # ```python
# import gradio as gr
# import joblib
# import numpy as np
# from sklearn.preprocessing import StandardScaler

# # Load the model and the scaler
# model = joblib.load('iris_model.joblib')
# scaler = joblib.load('scaler.joblib')  # Assuming a scaler.joblib file was saved during training

# # Define the prediction function
# def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
#     # Create a numpy array from the input
#     input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    
#     # Scale the input data
#     input_scaled = scaler.transform(input_data)
    
#     # Make a prediction
#     prediction = model.predict(input_scaled)
    
#     # Map integer prediction to flower name
#     mapping = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
#     return mapping[prediction[0]]

# # Create a Gradio interface
# iface = gr.Interface(
#     fn=predict_iris,
#     inputs=[
#         gr.inputs.Number(label="Sepal Length (cm)", default=5.1),
#         gr.inputs.Number(label="Sepal Width (cm)", default=3.5),
#         gr.inputs.Number(label="Petal Length (cm)", default=1.4),
#         gr.inputs.Number(label="Petal Width (cm)", default=0.2)
#     ],
#     outputs=gr.outputs.Textbox(label="Predicted Iris Species"),
#     title="Iris Flower Species Predictor",
#     description="Enter the measurements of the iris and get the predicted species."
# )

# # Launch the interface
# if __name__ == "__main__":
#     iface.launch()
# # ```