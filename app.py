import streamlit as st
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews
from login.page import show_login
from movies.service import MovieService
from genres.service import GenreService
from actors.service import ActorService
from reviews.service import ReviewService

def main():
    # Verifica login
    if 'token' not in st.session_state:
        show_login()
        return

    # Sidebar com menu e logout
    st.sidebar.title("🎬 Menu")
    menu_option = st.sidebar.radio(
        "Navegue pelo sistema",
        ['Início', 'Gêneros', 'Atores/Atrizes', 'Filmes', 'Avaliações']
    )

    if st.sidebar.button("🔒 Logout"):
        from login.service import logout
        logout()
        st.experimental_rerun()

    # Tela principal
    if menu_option == 'Início':
        st.title("🏠 Dashboard do Cinema")
        st.subheader(f"Bem-vindo(a), {st.session_state.get('user', 'Usuário')}!")

        # Puxando dados
        try:
            movie_service = MovieService()
            genre_service = GenreService()
            actor_service = ActorService()
            review_service = ReviewService()

            movies = movie_service.get_movies() or []
            genres = genre_service.get_genres() or []
            actors = actor_service.get_actors() or []
            reviews = review_service.get_reviews() or []

            # Estatísticas em cards
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("🎥 Filmes", len(movies))
            col2.metric("📚 Gêneros", len(genres))
            col3.metric("🎭 Atores", len(actors))
            col4.metric("✍️ Avaliações", len(reviews))

            st.markdown("---")

            # Cards clicáveis (simples via botões)
            st.subheader("Acesso rápido")
            if st.button("🎥 Ir para Filmes"):
                show_movies()
            if st.button("📚 Ir para Gêneros"):
                show_genres()
            if st.button("🎭 Ir para Atores/Atrizes"):
                show_actors()
            if st.button("✍️ Ir para Avaliações"):
                show_reviews()

        except Exception as e:
            st.error(f"Erro ao buscar dados: {e}")

    elif menu_option == 'Gêneros':
        show_genres()

    elif menu_option == 'Atores/Atrizes':
        show_actors()

    elif menu_option == 'Filmes':
        show_movies()
    
    elif menu_option == 'Avaliações':
        show_reviews()


if __name__ == '__main__':
    main()
