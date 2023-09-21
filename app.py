import streamlit as st
import joblib

# Load the machine learning model
model = joblib.load('lr_model.pkl')

#title
st.title("IRIS Prediction using ML")

# Define the form
with st.form('my_form'):
    sepallengthincm = st.text_input('Enter a sepal length')
    sepallwidthincm = st.text_input('Enter sepal width')
    petallengthincm = st.text_input('enter petal length')
    petalwidthincm = st.text_input('enter petal width')

    submit_button = st.form_submit_button('Submit')

# Make a prediction and display the result
if submit_button:
    # Convert the user's input to numerics
    sepallengthincm = float(sepallengthincm)
    sepallwidthincm = float(sepallwidthincm)
    petallengthincm = float(petallengthincm)
    petalwidthincm = float(petalwidthincm)

    # Make a prediction
    prediction = model.predict([[sepallengthincm,sepallwidthincm,petallengthincm,petalwidthincm]])

    # Display the prediction
    if(prediction==[0]):
        st.write('The name of the flower is : Iris-setosa')
    elif(prediction==[1]):
        st.write('The name of the flower is : Iris-versicolor')
    else:
        st.write('The name of the flower is : Iris-virginica')
