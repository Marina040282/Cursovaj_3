import json


class PathDAO:

    def __init__(self, path):
        """ При создании экземпляра DAO нужно указать путь к файлу с данными"""
        self.path = path

    def get_posts_all(self):
        """ Загружает данные из файла и возвращает посты"""
        posts = []
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                posts = json.load(file)
        except Exception as e:
            return posts, e

        return posts, None

    def get_posts_by_user(self, poster_name):
        """ Функция возвращает посты определенного пользователя.
         Функция должна вызывает ошибку `ValueError` если такого пользователя нет и пустой список, если у пользователя нет постов."""
        post_name = []
        posts, error = self.get_posts_all()
        try:
            for post in posts:
                if post["poster_name"] == poster_name:
                    post_name.append(post)
        except ValueError:
            return post_name

        return post_name

    def search_for_posts(self, teg):
        """ возвращает список постов по ключевому слову"""
        post_teg = []
        posts, error = self.get_posts_all()
        for post in posts:
            if teg in post["content"]:
                post_teg.append(post)
        return post_teg, error

    def get_post_by_pk(self, pk):
        """ Функция возвращает один пост по его идентификатору.
          Функция должна вызывает ошибку `ValueError` если такого пользователя нет и пустой список, если у пользователя нет постов."""
        post_pk = []
        posts, error = self.get_posts_all()
        try:
            for post in posts:
                if post["pk"] == pk:
                    post_pk = post
        except ValueError:
            return post_pk

        return post_pk
