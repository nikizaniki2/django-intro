import pytest
from rest_framework.test import APIClient

from comments.models import Post, Comment
from django.contrib.auth.models import User

import time

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

@pytest.fixture
def comment_factory(user):
    def _inner(**overrides):
        props = {
            "content":"Example comment!",
            "author": user,
            "post": 1,
        }
        props.update(**overrides)
        return Comment.objects.create(**props)
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


def test_comment_pagination(client, post_factory, comment_factory):
    comment_amount = 7
    
    # (pagination is set in )
    # posts/restapi/views.py 
    # StandardResultsSetPagination()
    # page_size = 2
    pagination_by_amount = 2 

    page_count = round(comment_amount/pagination_by_amount)

    my_post = post_factory(title="My Post")
    
    # create comments
    for i in range(comment_amount):
        comment_factory(content="Test Comment {}".format(i), post=my_post)
    
    # get comment data for post with id of my_post
    comment_response = client.get('/restapi/post/{}/comments'.format(my_post.id))
    comment_response = comment_response.data

    # test commment amount
    assert comment_response['count'] == comment_amount

    # test comments per page
    assert len(comment_response['results']) == pagination_by_amount

    # next page test (pagination)
    comment_response = client.get(comment_response['next'])
    comment_response = comment_response.data
    assert len(comment_response['results']) == pagination_by_amount

    # Test next page end
    comment_response = client.get('/restapi/post/{}/comments'.format(my_post.id))
    comment_response = comment_response.data
    
    for page_number in range(page_count-1):
        url = 'http://testserver/restapi/post/1/comments?page='
        assert comment_response['next'] == url + str(page_number + 2)
        comment_response = client.get(comment_response['next'])
        comment_response = comment_response.data
    assert comment_response['next'] == None