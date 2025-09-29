import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from datetime import datetime
from movies.service import MovieService
from actors.service import ActorService
from genres.service import GenreService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    for movie in movies:
        if 'genre' in movie:
            movie['genre'] = ", ".join([g['name'] for g in movie['genre']])
        if 'actors' in movie:
            movie['actors'] = ", ".join([a['name'] for a in movie['actors']])
    
    if movies:
        st.write('Lista de Filmes')
        movies_df = pd.json_normalize(movies)
        AgGrid(
            data=movies_df,
            reload_data=True,
            key='movies_grid'
        )
    else:
        st.warning('Nenhum filme encontrado.')

    st.title('Cadastrar novo filme')

    title = st.text_input('Título')
    release_date = st.date_input(
        label='Lançamento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    
    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.multiselect('Gênero', list(genre_names.keys()))
    selected_genres_ids = [genre_names[name] for name in selected_genre_name]


    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actors_name = st.multiselect('Atores/Atrizes', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actors_name]

    resume = st.text_area('Resumo')

    duration_minutes = st.number_input(
        'Duração (Minutos)',
        min_value=0,
        max_value=600,
    )

    release_date = st.date_input(
        'Data de lançamento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )

    poster = st.file_uploader("Enviar pôster", type=["png", "jpg", "jpeg"])

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            genre=selected_genres_ids,
            actors=selected_actors_ids,
            duration_minutes=duration_minutes,
            release_date=release_date,
            resume=resume,
            poster=poster,
        )
        if new_movie:
            st.success('Filme adicionado com sucesso')
            st.rerun()
        else:
            st.error('Erro ao cadastrar o filme. Verifique os campos.')
