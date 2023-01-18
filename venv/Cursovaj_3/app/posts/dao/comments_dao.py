import json


class CommentsDAO:

    def __init__(self, path):
        self.path = path

    def get_comments_all(self):
        # """ Загружает данные из файла и возвращает комментарии"""
        comments = []
        with open(self.path, "r", encoding="utf-8") as file:
            comments = json.load(file)

        return comments

    def get_comments_by_post_id(self, post_id):
        # """ Функция возвращает комментарии определенного поста.
        # Функция должна вызывать ошибку ValueError если такого поста нет и пустой список, если у поста нет комментов."""
        post_comments = []
        comments = self.get_comments_all()
        try:
            for comment in comments:
                if comment["post_id"] == post_id:
                    post_comments.append(comment)
        except ValueError:
            return post_comments

        return post_comments
