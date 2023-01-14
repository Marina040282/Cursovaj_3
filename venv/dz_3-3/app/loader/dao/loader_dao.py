import json


class PathDAO:

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

    def save_picture(self, picture):
        """Проверка загружаемого изображения на нужный формат, прописывает путь изображения"""
        filename = picture.filename
        file_type = filename.split('.')[-1]

        if file_type not in ('svg', 'dmp', 'jpg'):
            return

        picture.save(f'./uploads/images/{filename}')
        return f'uploads/images/{filename}'

    def save_post_json(self, posts):
        """ Добавляет новый данные в файл"""
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(posts, file, ensure_ascii=False)

    def add_post(self, post):
        """ Добавляет данные в файл JSON по новому посту"""
        posts, error = self.load_posts()
        posts.append(post)
        self.save_post_json(posts)
