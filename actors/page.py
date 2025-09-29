import streamlit as st
from st_aggrid import AgGrid
from datetime import datetime
import pandas as pd
from actors.service import ActorService


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de Atores/Atrizes')
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid'
        )
    else:
        st.warning('Nenhum Ator/Atriz encontrado.')

    
    st.title('Cadastrar novo ator')
    name = st.text_input('Nome do Ator/Atriz')
    birthday = st.date_input(
        label='Data de Nascimento',
        value=datetime.today(),
        min_value=datetime(1600, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    nacionality_dropdown =  [
    'AF',
    'AR',
    'AU',
    'BE',
    'BR',
    'CL',
    'CN',
    'CO',
    'DE',
    'DK',
    'EG',
    'ES',
    'FR',
    'GR',
    'IN',
    'IT',
    'JP',
    'KR',
    'MX',
    'NG',
    'NL',
    'PT',
    'RU',
    'SE',
    'TR',
    'UK',
    'UA',
    'US',
    'ZA',
]
    nacionality = st.selectbox(
        label='Nacionalidade',
        options=nacionality_dropdown,
    )
    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nacionality=nacionality,
        )
        if new_actor:
            st.success('Ator adicionado com sucesso.')
            st.rerun()
        else:
            st.error('Erro ao cadastrar o Ator/Atriz. Verifique os campos')