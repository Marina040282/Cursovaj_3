import json


class IndexDAO:

    def __init__(self, path):
        """ При создании экземпляра DAO нужно указать путь к файлу с данными"""
        self.path = path

    def load_posts(self):
        """ Загружает данные из файла и возвращает обычный list и ошибку при загрузке файла"""
        posts = []
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                posts = json.load(file)
        except Exception as e:
            return posts, e

        return posts, None

    def search_posts(self, substr):
        """ Поиск информации по тегу и возвращение только тех постов, где встречается данный тег,
        возвращает ошибку при чтении файла"""
        posts = []
        load_posts, error = self.load_posts()
        for post in load_posts:
            if substr in post["content"]:
                posts.append(post)

        return posts, error
