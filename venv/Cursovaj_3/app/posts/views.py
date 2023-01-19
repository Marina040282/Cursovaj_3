import logging, datetime

from flask import Blueprint, render_template, request, jsonify
from .dao.posts_dao import PathDAO
from .dao.comments_dao import CommentsDAO

# Создаем блупринт
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder="templates")
logging.basicConfig(filename='./logs/api.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# Создаем DAO
posts_dao = PathDAO("./data/posts.json")
comments_dao = CommentsDAO("./data/comments.json")


# Создаем вьюшку главной страницы
@posts_blueprint.route('/')
def page_index():
    posts, error = posts_dao.get_posts_all()
    if error:
        return f'Ошибка! Что-то пошло не так...{error}'

    return render_template("index.html", posts=posts)


# Создаем вьюшку одного поста с комментариями
@posts_blueprint.route("/posts/<int:pk>")
def post(pk):
    post = posts_dao.get_post_by_pk(pk)
    comments = comments_dao.get_comments_by_post_id(pk)
    return render_template('post.html', post=post, comments=comments)


# Создаем вьюшку постов пользователя
@posts_blueprint.route("/users/<username>")
def user_posts(username):
    posts = posts_dao.get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts, username=username)


# Создаем вьюшку поиска по тегу
@posts_blueprint.route('/search')
def page_tag():
    substr = request.args.get('s')
    posts, error = posts_dao.search_for_posts(substr)
    if error:
        return f'Ошибка! {error}'
    return render_template("search.html", posts=posts, substr=substr)


# Создаем вьюшку обработки полного списока постов в виде JSON-списка
@posts_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts():
    logging.info('Запрос /api/posts')
    posts, number_posts, error = posts_dao.get_posts_all()
    return jsonify(posts)


# Создаем вьюшку которая возвращает один пост в виде JSON-словаря
@posts_blueprint.route('/api/posts/<int:postid>', methods=['GET'])
def get_posts_by_id(postid):
    logging.info('Запрос /api/posts')
    return jsonify(posts_dao.get_post_by_pk(postid))
