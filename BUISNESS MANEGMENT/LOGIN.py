import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.dataframe_explorer import dataframe_explorer
import pandas as pd
import mysql.connector as mc
from matplotlib import pyplot as plt
from PIL import Image
import subprocess

st.set_page_config(
page_title="BUSINESS MANEGMENT",
page_icon=":boat:",
layout="wide",
)
##
##
def login_page():
    st.markdown('<style>div.block-container{padding-top:2rem}</style>',unsafe_allow_html=True)
    A,B=st.columns(2)
    with B:
        a,b=st.columns(2)
        with a:
            st.subheader("WELCOME")
            st.image("BOAT3.jpg")
            username=st.text_input("USERNAME")
            password=st.text_input("PASSWORD",type="password")  
            LOGIN_BUTTON=st.button("LOGIN")

    with A:
        a,b=st.columns(2)
        with b:
            i=Image.open("login.jpg")
            ni=i.resize((400,550))
            st.image(ni,use_column_width=True)

            if LOGIN_BUTTON:
                if username=="maloypariari" and password=="20100172":
                    st.success("SUCCESSFUL")
                    subprocess.Popen(["streamlit","run","MAIN.py"]).wait()
                else:            
                    st.error("CHECK DETAILS AGAIN")              
##
##
if __name__=="__main__":
    login_page()