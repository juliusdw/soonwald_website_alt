from soonwald.website import app


def ttest_index():
    with app.test_client() as test_client:
        # mimic a browser: 'GET /', as if you visit the site
        response = test_client.get('/')

        # check that the HTTP response is a success
        assert response.status_code == 200
        html_content = response.data.decode()

        assert "<html>" in html_content
