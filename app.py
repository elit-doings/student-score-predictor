import streamlit as st
import pickle

with open("doings.pkl", "rb") as f:
    doings = pickle.load(f)

st.title("Student score predictor")
st.write("Enter how many hours you don use study, make you get prediction of your exams score")

hours = st.slider("Hours studied", 0, 21, 1)

if st.button("Predict"):
    prediction = doings.predict([[hours]])
    st.success(f"Predicted Score: {prediction[0]:.2f}")

    if prediction[0]<50:
        st.warning("You gots try study more!")

    elif prediction[0]<70:
        st.info("Not bad, but try do do more sha!")

    else:
        st.balloons()
        st.success("You don do do oh, nice one")