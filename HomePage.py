import streamlit as st
import pandas as pd
import numpy as np

#pub dataset
pub_data = pd.read_csv('open_pubs.csv', header=None)
pub_data.columns = ['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority']

# Replace \N values with NaN
pub_data = pub_data.replace('\\N', np.nan)

# Drop rows with NaN values
pub_data = pub_data.dropna()

pub_data['longitude'] = pd.to_numeric(pub_data['longitude'], errors='coerce')
pub_data['latitude'] = pd.to_numeric(pub_data['latitude'], errors='coerce')

st.set_page_config(layout="centered")
st.markdown("<h1 style='text-align: center; color: #EB6864; font-weight: bold;'>Open Pubs Application 🍻</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Welcome to our pub finder app!</h2>", unsafe_allow_html=True)

st.image('pub.jpg', use_column_width=True)

# Display some basic information about the dataset
st.write(f"The dataset contains **{len(pub_data)}** pub locations.")
st.write(f"The dataset covers **{len(pub_data['local_authority'].unique())}** local authorities.")
st.markdown("<h2 style='text-align: center; color: #7F45FA;'>Pub Data</h2>", unsafe_allow_html=True)
st.markdown("<style>div.stDataFrame div[data-testid='stHorizontalBlock'] div[data-testid='stDataFrameContainer'] {margin: 0 auto;}</style>", unsafe_allow_html=True)
st.write(pub_data)

st.subheader("Let's Connect:-")
st.text("LinkedIn:- ")
if st.button(' Click Here to Connect with me:point_down:'):
    st.write('https://www.linkedin.com/in/apurva-jain04')
    st.success('Get connected!', icon="✅")

st.text("GitHub:- ")
if st.button(' Click Here to Connect::point_down:'):
    st.write('https://github.com/apurvajain4')
    st.success('Visit!', icon="✅")