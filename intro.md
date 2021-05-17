# Tutorials
[Videos](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

# Models (DB):
1. Create a python class. Example: class Question.
2. python manage.py makemigrations. Transpiles class properties to SQL code. Creates SQL table (questions).
3. ORM (Obj-Relational-Model) handles operations between code and database.
Examples:

```
from .models import Question
Question.objects.all() => lists all Questions that are saved in the database, presented as the python class.
Question.objects.filter(lambda question: id < 5)
Question.objects.count()
question = Question.objects.first()
question.question_text = "New question?"
question.save() => saves to DB
```
# URLs (Site):
1. python manage.py runserver
2. Listens for all the described urls in urls.py files.
3. Every urls.py file lists tuples that describe the urls in urlpatterns list:
## Example:
```
    urlpatterns = [
        path('<int:question_id>/', views.detail, name='detail'),
    ]
```

4. Navigate to URL from browser. (localhost:8000/polls/1/)
5. Django searches for matching URL regex in the registered urlpatterns.
6. If there is a match, calls the the associated view. In our case views.detail is called.
The browser request is passed as a param. Every view method, accepts "request" as its first parameter.
Django request: the browser request (GET/POST/PUT/DELETE), wrapped with bonus Django info.
Request contains the request type (GET/POST/PUT/DELETE), payload, user login information, cookies, etc.

## Example:
```
request.user.isAuthenticated() -> checks if you are logged in.
```

# Views:
1. views.py => Contains methods with logic per URL (views). Views process requests to the matching URL.
In our case def detail(request, question_id)

2. Renders HTML (a file from templates/foo.html). Can pass context as a dictionary.
## Example:
```
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    action_url = reverse('polls:detail', args=(question.id,))

    context = {
        'question': question,
        "action_url": action_url
    })
    
    return render(request, 'polls/detail.html', context)
```
3. Context can be handled by Django template language:
## Example in .html file:
```
From context (keys):
{{ question }}
{{ action_url }}
```
Context variables get replaced with the values from the context that the view method provided.


# Facebook (with Django)

## Prerequisite:
```
models.py
class Profile:
    self.name = name
```
## GETTING PROFILE PAGE (GET):
0. Get profile page -> facebook.com/profile/nsek.
1. urls.py ['/profile/<profile_id>', view.profile, name='profile']
2. views.py
```
def profile(request, profile_id):
    profile = Profiles.objects.get(profile_id=profile_id) # Gets your profile from the database
    return render(request, 'profiles/profile.html', { name: profile.name })
```
3. Templates (html)
```
    <div>
        This is my profile page.
        My name is: {{ name }}

        <form action="...">
        <input type="submit" />
    </div>
```
## CREATING A POST (POST request):
0. Let's say that the for submites "content" - a text
1. Views.py
```
def create_post(request):
    new_post = Post.objects.create(content=request.POST["content"], owner=request.user)
    new_post.save()
    return render(request, 'post/detail.html', { content: post.content })
```
2. Templates (html)
```
    <div>
        You created a new post!
        It says: {{ content }}
    </div>
```
## DELETE A POST (DELETE request):
0. Post model
```
class Post:
    def __init__(self, content, owner):
        self.content = content
        self.owner = owner

You are on page:
    <button onClick={ request({
        method: "DELETE",
        URL: 'post/delete/5
    })>
    </button>
```
1. urls.py ['/post/delete/<post_id>', view.delete_post, name='profile']
2. views.py

```
def delete_post(request, post_id):
    deleted_post = Post.object.get(id=post_id)
    daleted_post.delete()  # deletes from DB
    return render(request, 'post/deleted.html', { content: deleted_post.content })
```
3. Templates (html)
```
    <div>
        You deleted a post ;(
        It said: {{ content }}
    </div>
```