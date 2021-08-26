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

def test_post_pagination(client, post_factory):
    posts_amount = 20
    pagination_by_amount = 5

    page_count = round(posts_amount/pagination_by_amount)
    
    # create posts
    for i in range(posts_amount):
        post_factory(content="Test Post {}".format(i))
    
    # get post data
    post_response = client.get('/restapi/post/')
    post_response = post_response.data

    # test post amount
    assert post_response['count'] == posts_amount

    # test post per page
    assert len(post_response['results']) == pagination_by_amount

    # next page test (pagination)
    post_response = client.get(post_response['next'])
    post_response = post_response.data
    assert len(post_response['results']) == pagination_by_amount

    # Test next page end
    post_response = client.get('/restapi/post/')
    post_response = post_response.data
    
    for page_number in range(page_count-1):
        url = 'http://testserver/restapi/post/?page='
        assert post_response['next'] == url + str(page_number + 2)
        post_response = client.get(post_response['next'])
        post_response = post_response.data
    assert post_response['next'] == None