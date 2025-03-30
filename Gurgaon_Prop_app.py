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
st.dataframe(df)

st.header("Select your property")

Property_type = t.selectbox("Property Type",["Standalone House","Apartment"])

Sector =  st.selectbox("Select sector",df['sector'].unique().tolist())

bedroom = st.selectbox("Select Bedroom",df['bedroom'].unique().tolist())

bathroom = st.selectbox("Select bathroom",df['bathroom'].unique().tolist())

balcony = st.selectbox("No. of Balcony"),df['Balcony'].unique().tolist()

Property_age = st.selectbox("Property Age",sorted(df['agePossession'].unique().tolist()))
builtup_area =  float(st.number_input('Built up area'))
servant_room = float(st.selectbox("Servant Room", [0,1]))
store_room = float(st.selectbox("Servant Room", [0,1], key="servant_room_key"))
furnishing_type = st.selectbox("Furnishing Type", sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox("Luxury Category", sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox("Floor Category", sorted(df['floor_category'].unique().tolist()))

if st.button("Predict"):
    data = [[property_type,sector,bedroom,bathroom,balcony ,Property_age,builtup_area,servant_room,store_room,furnishing_type,luxury_category,floor_category]]
    columns = ['property_type','sector','bedroom','bathroom','balcony' ,'Property_age','builtup_area','servant_room','store_room','furnishing_type','luxury_category','floor_category']
    one_df = pd.DataFrame(data,columns=columns)



