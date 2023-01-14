import logging

from flask import Blueprint, render_template, request
from .dao.loader_dao import PathDAO

# Создаем блупринт
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder="templates")
logging.basicConfig(filename='basic.log', level=logging.INFO)

# Создаем DAO
loader_dao = PathDAO("./data/posts.json")


# Создаем вьюшку странички  добавления поста
@loader_blueprint.route('/post')
def create_new_post_page():
    return render_template("post_form.html")


# Создаем вьюшку странички после добавления поста
@loader_blueprint.route('/post', methods=['POST'])
def create_new_post():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Не все поля заполнены!'

    picture_path = loader_dao.save_picture(picture)
    if not picture_path:
        logging.info('Не загружено изображение!')
        return 'Не загружено изображение!'

    new_post = {'pic': picture_path, 'content': content}
    loader_dao.add_post(new_post)
    return render_template("post_uploaded.html", picture_path=picture_path, content=content)
