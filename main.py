import streamlit as st
import joblib
import numpy as np

model = joblib.load("Random_search.pkl")#Uploading the optimized machine Learning model

st.title("House Price Prediction")
st.markdown("---")

bedroom =st.number_input("Enter the number of bedroom",min_value=0,value=0)
bathroom =st.number_input("Enter the number of bathroom",min_value=0,value=0)
living_area =st.number_input("Enter the Living area",min_value=0,value=2000)
condition_of_house =st.number_input("Condition Of House",min_value=0,value=3)
number_of_school=st.number_input("School Min value",min_value=0,value=0)

st.markdown("---")
x=[[bedroom,bathroom,living_area,condition_of_house,number_of_school]]

prediction=st.button("Predict")

if prediction ==True:
    x_array= np.array(x)
    price =int(model.predict(x_array))
    st.write(f"House Price={price}")

else:
    st.write("Please Click")

    

