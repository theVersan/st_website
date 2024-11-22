import streamlit as st
from app import *

st.set_page_config(page_title='Projetos', page_icon="📚", layout="wide", initial_sidebar_state="collapsed")
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
    menu()

    st.header("📚 Projetos", divider="rainbow")
    st.write("")

    def experience_unit(title, position, date, location, content):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.subheader(title)
        with col3:
            st.write("")
            st.markdown("###### " + date)
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.markdown("###### " + position)
        with col3:
            st.markdown("######   " + location)
        st.write(content)

        left_column,  right_column, space_column = st.columns([2,2,10.5])
        left_column.link_button('Repositório', "https://www.chewy.com")
        right_column.link_button('Documentação', "https://github.com/theVersan")

    for exp in Experience:
        experience_unit(*exp)
        