import streamlit as st

st.title("Welcome to Tech Panda's Streamlit App")

st.markdown("""This is a simple Streamlit app created by Tech Panda. 

"You can use this app to :rainbow[demonstrate] the capabilities of  

"Streamlit and how easy it is to create interactive web applications with Python.""")

if st.button("Click me!"):
 st.balloons()

name = st.text_input("Enter your name", key = "name")

if name:
    st.write(f"Hello, {name}!")

if "theme" not in st.session_state:
    st.session_state.theme = "light"

def toggle_theme():
    is_light = st.session_state.theme == "light"
    st.session_state.theme = "dark" if is_light else "light"
    st._config.set_option("theme.base", st.session_state.theme)

# dm =st.toggle("dark mode", key = "dark_mode") 




if st.button("🌙 Dark Mode" if st.session_state.theme == "light" else "☀️ Light Mode") :
    toggle_theme()
    st.rerun()




   

all_user = ["bala","raj","kumar"]


col1, col2 = st.columns(2)

with col1:
    st.metric(label = "Temperature", value = "25 °C", delta = "1.2 °C")

with col2:
    st.metric(label = "Humidity", value = "60 %", delta = "-5 %")

st.sidebar.title("Sidebar")

category = st.sidebar.selectbox("Select a category", ["Category 1", "Category 2", "Category 3"])

tab1 , tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.write("This is Tab 1")

with tab2:
    st.write("This is Tab 2")

# pages = [st.Page("home.py",title = "home")]        

# pg = st.sidebar.pages(pages)

# pg.run()

with st.container(border = True):
    users = st.multiselect("Select users", all_user,default = ["bala"])
