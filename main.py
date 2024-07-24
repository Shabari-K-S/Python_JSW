import base64
import io
import streamlit as st
from PIL import Image
import os
import mysql.connector
from dotenv import load_dotenv

icon = Image.open("./assets/favicon.png")
st.set_page_config(page_title="JSW", page_icon=icon, layout="wide", initial_sidebar_state="expanded")


st.markdown("""
<style>
    .block-container{
        padding-top:10px;
        padding-bottom:10px;
        padding-left:20px;
    }
MainMenu, header, footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)

load_dotenv()
MYSQL_HOST = os.getenv("DB_HOST")
MYSQL_USER = os.getenv("DB_USER")
MYSQL_PASSWORD = os.getenv("DB_PASSWORD")
MYSQL_DATABASE = os.getenv("DB_NAME")
MYSQL_PORT = os.getenv("DB_PORT")

# create a connection
# create a session state

if "connection" not in st.session_state:
    st.session_state.connection =  mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        port=MYSQL_PORT
    )

if st.session_state.connection.is_connected():
    pass
else:
    print("Connection failed")

if "accessLevel" not in st.session_state:
    st.session_state.accessLevel = None


cursor = st.session_state.connection.cursor()

if "login" not in st.session_state:
    st.session_state.login = False

if __name__ == "__main__":
    if not st.session_state.login:
        Login1, Login2 = st.columns([1,1], vertical_alignment= "center")
        with Login1:
            
            bg = Image.open("./assets/login-left.png")
            buffered = io.BytesIO()
            bg.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            st.write("<img src='data:image/png;base64,{}' style='width: calc(100vh + 30%);position: absolute; margin-left:-20px;margin-top:-10px; overflow: hidden;'>".format(img_str), unsafe_allow_html=True)
            logo = Image.open("./assets/logo.png")
            st.write("<div style='text-align:;margin-top:calc(100vh - 40%); color: #333;'></div>", unsafe_allow_html=True)
            Login11,Login12,Login13 = st.columns([1,2,1])
            with Login12:
                st.image(logo, width=300)
        with Login2:
            l1,l2,l3 = st.columns([1,2,1])
            with l2:
                st.write("<h1 style='text-align: center; color: #333;'>Login</h1>", unsafe_allow_html=True)
                st.write("""
                        <div style='width:100px;height:20px'></div>
                        <p style='color:#333; text-align: center;font-size:20px'>Welcome to JSW OHC</p>
                        <div style='width:100px;height:50px'></div>
                    """, unsafe_allow_html=True)
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                # Login with mysql server
                st.markdown("""
                    <style>
                        button[kind="primary"] {
                            all: unset;
                            background-color: #22384F;
                            color: white;
                            border-radius: 5px;
                            text-align: center;
                            cursor: pointer;
                            font-size: 20px;
                            width: 95%;
                            padding: 10px ;
                        }
                        [data-testid="stHeader"]{
                            background-color: transparent;
                        }
                    </style>""", unsafe_allow_html=True)
                if st.button("Login", type="primary"):
                    cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
                    result = cursor.fetchall()
                    if result:
                        st.session_state.accessLevel =  result[0][2]
                        st.write("Login Success")
                        st.session_state.login = True
                        st.rerun()
                    if username == "" or password == "":
                        st.warning("Please enter username and password")
                    else:
                        st.error("Username and password are incorrect")
    else:
        if st.session_state.accessLevel == "admin":
            st.switch_page("./pages/admin_dashboard.py")
        
        if st.session_state.accessLevel == "doctor":
            st.switch_page("./pages/dashboard.py")
        
        if st.session_state.accessLevel == "nurse":
            st.switch_page("./pages/dashboard.py")