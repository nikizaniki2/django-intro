import pytest
from rest_framework.test import APIClient

from posts.models import Post
from django.contrib.auth.models import User
from django.urls import reverse


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



def test_user_post(client, user):
    post = {
        "title" : "TEST",
        "content" : "TEST content!",
    }
    link = '/restapi/post/'

    response = client.post(link, post)
    assert response.status_code == 201
    assert Post.objects.get(title="TEST", content="TEST content!", author=user.id)

def test_delete_perm(client, post_factory):
    post_factory()
    post = Post.objects.get(title="Example")
    link = reverse('post-detail', kwargs={'pk': post.id})

    response = client.delete(link)

    assert response.status_code == 204
    assert Post.objects.filter(title="Example").exists() == False