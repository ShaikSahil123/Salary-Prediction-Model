import pickle
import streamlit as st

model = pickle.load(open("Data.pkl","rb"))

def Fun():
    st.title("Prediction of the Salary of an Employee based on the Year of Experience")
    disp = st.number_input("Enter the year of Experience of the employee :")
    pred = st.button("Start")

    if pred:
        op = model.predict([[disp]])
        st.write("The Predicted Salary of the Employee is : ",op[0])

Fun()