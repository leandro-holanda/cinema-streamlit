import requests
import streamlit as st
from login.service import logout


class MovieRepository:

    def __init__(self):
        self.__base_url = 'https://leandroholanda007.pythonanywhere.com/api/v1/'
        self.__movie_url = f'{self.__base_url}movies/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}' 
        }

    def get_movies(self):
        response = requests.get(
            self.__movie_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def create_movie(self, movie):
        files = None
        if movie.get("poster"):
            files = {
                "poster": (movie["poster"].name, movie["poster"].read(), movie["poster"].type)
            }

        data = {
            "title": movie["title"],
            "duration_minutes": movie["duration_minutes"],
            "release_date": movie["release_date"].isoformat() if movie.get("release_date") else None,
            "resume": movie["resume"],
            "genre": movie["genre"],     # lista de IDs
            "actors": movie["actors"],   # lista de IDs
        }

        response = requests.post(
            self.__movie_url,
            headers=self.__headers,
            data=data,
            files=files
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')