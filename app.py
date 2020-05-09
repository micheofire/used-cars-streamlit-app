import streamlit as st
import joblib
import pandas as pd
import numpy as np
from PIL import Image


def load_data(dataset):
    df = pd.read_csv(dataset)
    return df


col = ['trans', 'origin', 'engine', 'year', 'brand_honda', 'brand_lexus',
       'brand_mercedes-benz', 'brand_toyota', 'brand_volkswagen',
       'model_accord coupe ex-l v-6 automatic',
       'model_avensis 2.4 exclusive automatic', 'model_avensis verso',
       'model_c350', 'model_camry', 'model_camry 2.4 se automatic',
       'model_corolla', 'model_corolla automatic',
       'model_corolla le 4-speed automatic', 'model_corolla le automatic',
       'model_cr-v', 'model_e350', 'model_es 330', 'model_es 350',
       'model_glk 350', 'model_gx 470 sport utility', 'model_hiace',
       'model_highlander limited v6 4x4', 'model_lt', 'model_matrix',
       'model_rav4', 'model_rav4 4wd', 'model_rav4 limited', 'model_rx',
       'model_rx 330 4wd', 'model_sienna', 'model_venza']
test = pd.DataFrame([np.zeros(36)], columns=col)


year_array = np.arange(2000,2021)
toyota_models = ['avensis 2.4 exclusive automatic', 'avensis verso','camry','camry 2.4 se automatic',
 'corolla','corolla automatic','corolla le 4-speed automatic','corolla le automatic','hiace',
 'highlander limited v6 4x4','matrix','rav4','rav4 4wd','rav4 limited','sienna','venza']
honda_models = ['accord coupe ex-l v-6 automatic', 'cr-v']
benz_models = ['c350', 'e350', 'glk 350']
lexus_models = ['es 330', 'es 350', 'gx 470 sport utility', 'rx', 'rx 330 4wd']
volks_models = ['lt']


transmission = {"Automatic":1, "Manual":0}
engine = {"Petrol":1, "Diesel":0}
origin = {"Foreign":1, "Local":0}
year = {i: year_array[i] for i in range(1, len(year_array))}
brand = {"Lexus":"1", "Honda":"2", "Mercedes-Benz":"3", "Toyota":"4", "Volkswagen":"5"}
toyota = {i: toyota_models[i] for i in range (0, len(toyota_models))}
honda = {i: honda_models[i] for i in range (0, len(honda_models))}
benz = {i: benz_models[i] for i in range (0, len(benz_models))}
lexus = {i: lexus_models[i] for i in range (0, len(lexus_models))}
volks = {i: volks_models[i] for i in range (0, len(volks_models))}



#Get the keys
def get_value(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return int(value)
        
#Find the keys in the dictionary
def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
        
        
        



def main():
    """Used Cars Ml App"""
    st.title("Used Cars ML App")
    st.subheader("Dashboard") 
    
    #menu
    menu = ["May", "April"]
    choices = st.sidebar.selectbox("Select month",menu)
    
    #Load Model
    model1 = joblib.load(choices.lower()+".pkl")
    
    #short description
    st.subheader("Prediction for " + choices)
    
    #Add sliders and selectbox to the dashboard
    Transmission = st.sidebar.selectbox("Transmission type", tuple(transmission.keys()))
    Engine = st.sidebar.selectbox("Engine type", tuple(engine.keys()))
    Origin = st.sidebar.selectbox("Use Origin", tuple(origin.keys()))
    Year = st.sidebar.slider("Year", 2000,2020)
    Brand = st.sidebar.selectbox("Brand", tuple(brand.keys()))
    if Brand == "Lexus":
        Model = st.sidebar.selectbox("Model", tuple(lexus.values()))
    elif Brand == "Toyota":
        Model = st.sidebar.selectbox("model", tuple(toyota.values()))
    elif Brand == "Honda":
        Model = st.sidebar.selectbox("model", tuple(honda.values()))
    elif Brand == "Volkswagen":
        Model = st.sidebar.selectbox("model", tuple(volks.values()))
    elif Brand == "Mercedes-Benz":
        Model = st.sidebar.selectbox("model", tuple(benz.values()))
            
    test["trans"] = get_value(Transmission, transmission)
    test["engine"] = get_value(Engine, engine)
    test["origin"] = get_value(Origin, origin)
    test["year"] = Year
    test["brand_"+Brand.lower()] = 1
    test["model_"+Model.lower()] = 1
            
            
            
    if st.button("Evaluate"):
        predicted = int(model1.predict(test))
        message = "Used " + str(Year) + " " + str(Brand)+ " " + str(Model)+' in Nigeria is expected to range from ₦' + str(predicted) + ' to ₦' + str(predicted+100000) + '. It is safe to buy or sell at this price range'
        st.write(message)
           





if __name__ == "__main__":
    main()
