import pytest

from ...models import Post
from django.contrib.auth.models import User


@pytest.fixture
def user():
    return User.objects.create(username='user', password='testpass')

def post(user):
    return Post.objects.create(user=user, )

def test_user(user):
    print(user.__dict__)
