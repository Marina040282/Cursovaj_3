from flask import Blueprint, render_template, request
from .dao.main_dao import IndexDAO

import logging

# Создаем блупринт
main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")
logging.basicConfig(filename='basic.log', level=logging.INFO)

# Создаем DAO
mainn_dao = IndexDAO("./data/posts.json")


# Создаем вьюшку главной страницы
@main_blueprint.route('/')
def page_index():
    return render_template("index.html")


# Создаем вьюшку странички ленты по тегу
@main_blueprint.route('/search')
def page_tag():
    substr = request.args.get('s')
    logging.info(f'Поиск: {substr}')
    posts, error = mainn_dao.search_posts(substr)
    if error:
        logging.info(f'Ошибка: {error}')
        return 'Ошибка!'
    return render_template("post_list.html", posts=posts, substr=substr)
