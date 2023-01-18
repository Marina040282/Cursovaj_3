keys_should_be = {
    "poster_name",
    "poster_avatar",
    "pic",
    "content",
    "views_count",
    "likes_count",
    "pk"}


class TestPosts:

    def test_root_status(self, test_client):
        """ ѕровер€ем, получаетс€ ли нужный статус-код и """
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, "—татус-код всех постов неверный"

    def test_root_content(self, test_client):
        response = test_client.get('/', follow_redirects=True)
        assert "Ёто главна€ страничка" in response.data.decode("utf-8"), " онтент страницы неверный"

    def test_api_all_posts(self, test_client):
        response = test_client.get('/api/posts/')
        assert response.status_code == 200
        api_response = response.json
        assert type(api_response) == list
        assert set(api_response[0].keys()) == keys_should_be

    def test_api_post(self, test_client):
        response = test_client.get('/api/posts/1')
        assert response.status_code == 200
        api_response = response.json
        assert type(api_response) == dict
        assert set(api_response.keys()) == keys_should_be
