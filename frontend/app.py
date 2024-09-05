import streamlit as st
import requests

st.title('Patient Satisfaction Prediction')


wait_time = st.slider('Wait Time (minutes)', 0, 120, 15)
staff_friendliness = st.slider('Staff Friendliness (1-5)', 1, 5, 4)
cleanliness = st.slider('Cleanliness (1-5)', 1, 5, 4)
quality_of_care = st.slider('Quality of Care (1-5)', 1, 5, 4)

if st.button('Predict'):
    response = requests.post('http://localhost:5000/predict', json={
        'wait_time': wait_time,
        'staff_friendliness': staff_friendliness,
        'cleanliness': cleanliness,
        'quality_of_care': quality_of_care
    })
    if response.status_code == 200:
        result = response.json()
        st.write(f"Predicted Satisfaction: {result['satisfaction']:.2f}")
    else:
        st.write(f"Error: {response.status_code} - {response.text}")
