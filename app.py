####### Importing the libraries
import streamlit as  st
import pickle
import numpy as np

#### Loading the data
df = pickle.load(open('laptop.pkl','rb'))
pipe = pickle.load(open('pipe.pkl','rb'))

### Creating the GUI
st.title('Laptop Price Prediction System')

### Form
company =  st.selectbox('Company', df['Company'].unique())     ### Company of the laptop
type = st.selectbox('Type', df['TypeName'].unique())        ### Type of the laptop
ram = st.selectbox('RAM(GB)',[2,4,6,8,12,16,24,32,64])     ### Ram of the laptop
weight = st.number_input('Weight')                                    ### Weight of the laptop
touchscreen = st.selectbox('TouchScreen',['Yes','No'])         ### TouchScreen of the laptop
ips = st.selectbox('IPS Panel',['Yes', 'No'])                  ### IPS Panel of the laptop
screen_size = st.number_input('Screen Size')                   ### Screen_size of the laptop
resolution = st.selectbox('Screen Resolution', ['1920x1080','1366x768','1600x900',   ###### Screen Resolution of the laptop
                '3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
cpu = st.selectbox('CPU(Processor)', df['CPU'].unique())                ### CPU of the laptop
hdd = st.selectbox('HDD(GB)',[0,128,256,512,1024,2048])        #### HDD of the laptop
ssd = st.selectbox('SSD(GB)',[0,128,256,512,1024])             #### SSD of the laptop 
gpu = st.selectbox('GPU', df['GPU'].unique())                  #### GPU of the laptop
os = st.selectbox('Operating System',df['OS'].unique())        #### OS of the laptop


##### Button 
if st.button('Predict Price'):
    #### input
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == "Yes":
        ips = 1
    else:
        ips = 0
    
    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    ppi = ((x_res**2) + (y_res**2))**0.5/screen_size

    input = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
    input = input.reshape(1,12)

    st.title("The Price of predicted Laptop is " + str(int(np.exp(pipe.predict(input)[0]))))
    

    
