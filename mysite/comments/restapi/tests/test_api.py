import pytest
from rest_framework.test import APIClient

from comments.models import Post
from django.contrib.auth.models import User


@pytest.fixture
def user():
    return User.objects.create(username='user', password='testpass')


@pytest.fixture
def client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def other_user():
    return User.objects.create(username='other', password='testpass')


@pytest.fixture
def post_factory(user):
    def _inner(**overrides):
        props = {
            "title":"Example",
            "content":"Example content!",
            "author": user,
        }

        props.update(**overrides)
        return Post.objects.create(**props)

    return _inner


def test_post_factory(post_factory):
    # Create some posts
    post_factory()
    post_factory(title="Second")
    post_factory(title="Third", content="Third post content!")

    assert Post.objects.get(title="Example").content == "Example content!"
    assert Post.objects.get(title="Second")
    assert Post.objects.get(content="Third post content!")


def test_list_posts(client, post_factory):
    post_factory(title="First")
    post_factory(title="Second")

    response = client.get('/restapi/post/')
    assert response.status_code == 200

    #responses are now different due to pagination
    response_posts = response.data['results']
    assert len(response_posts) == 2
    assert any(map(lambda post: post.get("title") == "First", response_posts))
    assert any(map(lambda post: post.get("title") == "Second", response_posts))
    # assert any(map(lambda post: post.get("title") == "BANG", response_posts))
