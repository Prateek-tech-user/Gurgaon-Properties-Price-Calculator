import numpy as np 
import streamlit as st
import pickle
import pandas as pd
import streamlit

st.title("hello this is Gurgaon Properties")

with open("df.pkl","rb") as file:
    data = pickle.load(file)

with open("pipeline.pkl","rb") as algo:
    pipline = pickle.load(algo)

df = pd.DataFrame(data)
#st.dataframe(df)

st.header("Select your Input")

property_type = st.selectbox("Property type",["house","flat"])
sector = st.selectbox("Select sector",df['sector'].unique().tolist())
bedroom = st.selectbox("Number of Bedrooms",sorted(df['bedRoom'].unique().tolist()))
bathroom = st.selectbox("Number of Bathrooms",sorted(df['bathroom'].unique().tolist()))
balcony = st.selectbox("Number of Balcony",sorted(df['balcony'].unique().tolist()))
Property_age = st.selectbox("Property Age",sorted(df['agePossession'].unique().tolist()))
builtup_area =  float(st.number_input('Built up area'))
servant_room = float(st.selectbox("Servant Room", [0,1]))
store_room = float(st.selectbox("Servant Room", [0,1], key="servant_room_key"))
furnishing_type = st.selectbox("Furnishing Type", sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox("Luxury Category", sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox("Floor Category", sorted(df['floor_category'].unique().tolist()))

if st.button("Predict"):
    data = [[property_type,sector,bedroom,bathroom,balcony ,Property_age,builtup_area,servant_room,store_room,furnishing_type,luxury_category,floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'built_up_area', 'servant room', 'store room',
       'furnishing_type', 'luxury_category', 'floor_category']
    one_df = pd.DataFrame(data,columns=columns)
    #st.dataframe(one_df)
    price = np.expm1(pipline.predict(one_df))[0]  # extract scalar
    st.markdown(f"**Estimated price is ₹{np.round(price * 10000000):,.0f}**")
 


