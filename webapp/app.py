import streamlit as st
import base64
import pickle
import numpy as np 
import joblib

st.set_page_config(page_title= 'Laptop Price Predictor', layout="wide")

with open('./webapp/static/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown("<h1 class = 'title'>Laptop Price Predictor</h1>",unsafe_allow_html=True)
st.markdown("<hr style = 'color:red;'>",unsafe_allow_html=True) 

# set background
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64('./webapp/background/back.jpg')
page_bg_img = f"""
    <style> 
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0, 0, 0, 0)
    }}
    [data-testid="stToolbar"] {{
        right: 2rem;
    }}
    
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

def prediction(list):
    filename = './model/predictor_model.pkl'
    with open(filename, 'rb') as file:
         model = joblib.load(file)
    
    pred_value = model.predict([list])
    return pred_value

# input fields
c1, c2 = st.columns(2)
with c1:
    company_options = ['---','Acer','Apple', 'Asus', 'Dell', 'HP',
       'Lenovo', 'MSI', 'Toshiba', 'Other']
    company = st.selectbox('Select Brand', company_options)

    cpu_options = ['---', 'Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'AMD', 'Other']
    cpu = st.selectbox('Select Processor', cpu_options)

    ram_options = ['---','2','4','6','8','12','16','24','32','64']
    ram = st.selectbox('Select RAM (GB)', ram_options)

    type_options = ['---','2 in 1 Convertible', 'Gaming', 'Netbook',
       'Notebook', 'Ultrabook', 'Workstation',]
    type = st.selectbox('Select Type', type_options)

    os_options = ['---', 'Windows','Linux', 'Mac', 'Other']
    os = st.selectbox('Select Operating System', os_options)

with c2:

    gpu_options = ['---', 'AMD', 'Intel', 'Nvidia']
    gpu = st.selectbox('Select GPU', gpu_options)

    hdd_options = ['---', '0', '500', '1000', '2000']
    hdd = st.selectbox('Select HDD (GB)', hdd_options)

    ssd_options = ['---', '0', '128', '256', '512', '1000']
    ssd = st.selectbox('Select SSD (GB)', ssd_options)

    touch_options = ['---', 'Touch Screen', 'No Touch Screen']
    touch_input = st.selectbox('Select Touchscreen', touch_options)
    if touch_input == 'Touch Screen':
        touch = 1
    else: 
        touch = 0

    IPS_options = ['---', 'IPS Panel', 'No IPS Panel']
    IPS_input = st.selectbox('Select IPS Panel', IPS_options)
    if IPS_input == 'IPS Panel':
        ips = 1
    else: 
        ips = 0




company_list = ['Acer','Apple', 'Asus', 'Dell', 'HP','Lenovo', 'MSI', 'Other', 'Toshiba']
typename_list = ['2 in 1 Convertible', 'Gaming', 'Netbook','Notebook', 'Ultrabook', 'Workstation']
opsys_list = ['Linux', 'Mac', 'Other', 'Windows']
cpu_list = ['AMD','Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Other']
gpu_list = ['AMD', 'Intel', 'Nvidia']

  
feature_list = []
if company_options == '---' or cpu_options == '---' or ram_options == '---' or gpu_options == '---' or type_options == '---' or os_options == '---' or hdd_options == '---' or ssd_options == '---' or touch_input == '---' or IPS_input == '---':
    st.empty()
else:
    feature_list.append(int(ram))
    feature_list.append(touch)
    feature_list.append(ips) 
    feature_list.append(int(hdd))
    feature_list.append(int(ssd))

    def traverse_list(lst, value):
        for item in lst:
            if item == value:
                feature_list.append(1)
            else:
                feature_list.append(0)     

    traverse_list(company_list, company)
    traverse_list(typename_list, type)
    traverse_list(opsys_list, os)
    traverse_list(cpu_list, cpu)
    traverse_list(gpu_list, gpu)

    print(feature_list)
    pred_value = prediction(feature_list)
    # pred_value = np.round(pred_value[0],2)*221

    
    st.write(pred_value)