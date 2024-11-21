import streamlit as st


skill_col_size = 5

#Página sobre

sobre = st.Page(
    page="pages/sobre.py",
    title="Sobre mim",
    icon=":material/account_circle:",
    default=True,
)

contato = st.Page(
    page="pages/contato.py",
    title="Contato",
)


projetos = st.Page(
    page="pages/projetos.py",
    title="Projetos",
)

eng_software = st.Page(
    page="pages/eng_software.py",
    title="Engenharia de software",
)


#Navigation
pg = st.navigation(
    {
        "Info": [sobre, contato],
        "Projects": [projetos],
        "Estudos": [eng_software],
    }
)


def menu():
    bar1, bar2, bar3, bar4 = st.columns([1,1,1,1])
    bar1.page_link("pages/sobre.py", label="Sobre" ' :information_source: ')
    bar2.page_link("pages/contato.py", label="Contato" ' :e-mail: ')
    bar3.page_link("pages/projetos.py", label="Projetos" '	:clipboard: ')
    bar4.page_link("pages/eng_software.py", label="Engenharia de Software" ' :computer: ')
    st.write("")

info = {'brief':
              """    
                Olá, eu sou o Davi Versan, estudante de engenharia de software no Instituto de Tecnologia e Liderança - 
                INTELI, uma faculdade que une negócios e computação através de uma metodolgia baseada por projetos. Neste 
                site você terá acesso a meu portfólio de projetos, informações de contato e atualizações de estudo.
              """,
        'nome':"Davi D'avila Versan", 
        'faculdade':'Instituto de Tecnologia e Liderança - INTELI',
        'cidade':'São Paulo, SP',
        'interesses':'Data Science, Cloud Computing, DevOps, IA ',
        'habilidades':['Python','Javascript','HTML & CSS','Node.js','Streamlit', 'MongoDB','PostgreSQL','MySQL','SQLite','Github'],
        }

#Contatos
phone = "(44)997099004"
email = "theversan@gmail.com"
linkedin_link = "https://www.linkedin.com/in/daviversan/"
github_link = "https://github.com/theVersan"


linkedin_logo = '''                                                                                                                                          
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-linkedin" style="font-size: 25px;"></i>                                                                           
'''

github_logo = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-github" style="font-size: 25px;"></i>                                                                           
'''

#Logo


pg.run()
