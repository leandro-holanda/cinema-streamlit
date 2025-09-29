import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from reviews.service import ReviewService
from movies.service import MovieService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        st.write('Lista de Reviews')
        review_df = pd.json_normalize(reviews)
        AgGrid(
            data=review_df,
            reload_data=True,
            key='reviews_grid'
        )
    else:
        st.warning('Nenhuma avaliação encontrada.')


    st.title('Cadastrar uma nova avaliação')

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))

    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1,
    )

    comment = st.text_area('Comente sobre o filme')

    if st.button('Avaliar'):
        new_review = review_service.create_review(
            movie=movie_titles[selected_movie_title],
            stars=stars,
            comment=comment
        )
        if new_review:
            st.success('Avaliação realizada com sucesso')
            st.rerun()
        else:
            st.error('Erro ao avaliar o filme. Verifique os campos.')
