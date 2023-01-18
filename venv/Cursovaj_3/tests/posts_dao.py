from app.posts.dao.posts_dao import PathDAO
from app.posts.dao.comments_dao import CommentsDAO

import pytest


@pytest.fixture()
def posts_dao():
    posts_dao_instance = PathDAO("./data/posts.json")
    return posts_dao_instance


@pytest.fixture()
def comments_dao():
    comments_dao_instance = CommentsDAO("./data/comments.json")
    return comments_dao_instance


keys_should_be = {
    "poster_name",
    "poster_avatar",
    "pic",
    "content",
    "views_count",
    "likes_count",
    "pk"}

keys_should_be_comments = {
    "post_id",
    "commenter_name",
    "comment",
    "pk"}


class TestPostsDao:

    def test_get_posts_al(self, posts_dao):
        """ Проверяем, верный ли список постов возвращается """
        posts = posts_dao.get_posts_all(self)
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_posts_by_user(self, posts_dao):
        """ Проверяем, верный ли список постов возвращается определенного пользователя """
        posts = posts_dao.get_posts_by_user(self, 'leo')
        assert type(posts) == list
        assert len(posts) > 0
        assert set(posts.keys()) == keys_should_be

    def test_search_for_posts(self, posts_dao):
        """ Проверяем, верный ли список постов возвращается по ключевому слову """
        posts = posts_dao.search_for_posts(self, 'кот')
        assert type(posts) == list
        assert len(posts) > 0
        assert set(posts.keys()) == keys_should_be

    def test_get_post_by_pk(self, posts_dao):
        """ Проверяем, верный ли пост возвращается при запросе одного поста """
        posts = posts_dao.get_post_by_pk(self, 1)
        assert type(posts) == list
        assert posts["pk"] == 1
        assert set(posts.keys()) == keys_should_be

    def get_comments_all(self, comments_dao):
        """ Проверяем, верный ли список коментариев возвращается """
        comments = comments_dao.get_comments_all(self)
        assert type(comments) == list, "возвращается не список"
        assert len(comments) > 0, "возвращается пустой список"
        assert set(comments[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_comments_by_post_id(self, comments_dao):
        """ Проверяем, верный ли возвращаются комментарии определенного поста """
        comments = comments_dao.get_comments_by_post_id(self, 1)
        assert type(comments) == list
        assert len(comments) > 0
        assert set(comments.keys()) == keys_should_be
