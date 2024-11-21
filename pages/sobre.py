import streamlit as st
from app import info
from app import menu
from app import *

st.set_page_config(page_title="Contacts", page_icon="🌏",initial_sidebar_state="collapsed",layout="wide") #

margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
    menu()
    st.layout='centered'

st.header("Sobre mim",divider='rainbow')


col1, col2, col3 = st.columns([1.3, 0.2, 1])


with col1:
        st.write(info['brief'])
        st.markdown(f"###### :technologist: Nome: {info['nome']}")
        st.markdown(f"###### 	:mortar_board: Faculdade: {info['faculdade']}")
        st.markdown(f"###### 📍 Cidade: {info['cidade']}")
        st.markdown(f"###### 📚 Interesses: {info['interesses']}")
        st.markdown("###### :computer: Formação: Engenharia de software")

        with open("assets/Curriculo_estagio_new (1).pdf", "rb") as file:
            pdf_file = file.read()

        st.download_button(
            label="Baixe meu :blue[currículo]",
            data=pdf_file,
            file_name="Currículo-Davi_Versan",
            mime="assets/Curriculo_estagio_new (1).pdf")

with col3:
        st.image("assets/lnkd_pic.jpg", width=360)

#Skills

st.subheader("Minhas :blue[habilidades]", divider="rainbow")

def skill_tab():
      rows, cols = len(info['habilidades'])//skill_col_size, skill_col_size
      habilidades = iter(info['habilidades'])
      if len(info['habilidades'])%skill_col_size!=0:
            rows+=1
      for x in range(rows):
            columns = st.columns(skill_col_size)
            for index_ in range(skill_col_size):
                  try:
                        columns[index_].button(next(habilidades))
                  except:
                        break
with st.spinner(text="Loading section"):
      skill_tab()