# Basic

## Why?
- No navigation


# Create comment
## Now
- Navigite to post/9/comment/new (page refresh)
- Handle in views.py
- Navigate back to prev pare (page refresh again)

## Rest API
- Set of URLs.

### Enpoint
- Receives requests at a URL. (/restapi/comment/create)
- Returns data when it's ready, or error.


- No nagate
- Click a button that makes an `async` request to REST api:

POST
```js
$.post(
    url: "/restapi/comment/create",  // URL to API endpoint
    data: {
        "content": "New comment"
    }
)
    .then(response => {})  // Success handler
    .catch(error => {})  // Error handler
```

- Click a button
- Loading (non-blocking)
- Success/Error

# Django REST
https://www.django-rest-framework.org/api-guide/testing/#apiclient

## Serializers
JSON <==> Model

https://www.django-rest-framework.org/api-guide/serializers/
https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
