import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Joke
from .serializers import JokeSerializer

@api_view(['POST'])
def fetch_and_store_jokes(request):
    url = "https://v2.jokeapi.dev/joke/Any?amount=10"
    jokes = []

    for _ in range(10):  # Fetch 10 pages of jokes
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            jokes.extend(data['jokes'])

    for joke in jokes:
        new_joke = Joke(
            category=joke['category'],
            type=joke['type'],
            joke=joke['joke'] if joke['type'] == 'single' else None,
            setup=joke['setup'] if joke['type'] == 'twopart' else None,
            delivery=joke['delivery'] if joke['type'] == 'twopart' else None,
            nsfw=joke['flags'].get('nsfw', False),
            political=joke['flags'].get('political', False),
            sexist=joke['flags'].get('sexist', False),
            safe=joke['safe'],
            lang=joke['lang']
        )
        new_joke.save()

    return Response({"message": "Jokes fetched and stored successfully!"}, status=status.HTTP_201_CREATED)