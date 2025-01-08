from django.shortcuts import render
from django.http import JsonResponse
import requests

ANILIST_QUERY = """
query ($search: String) {
  Media(search: $search, type: ANIME) {
    id
    title {
      romaji
      english
      native
    }
    description
    genres
    coverImage {
      large
    }
    episodes
  }
}
"""
ANILIST_API_URL = "https://graphql.anilist.co"

def home(request):
    #return render(request, 'core/index.html')  # Render the template
    anime_list = [
        {"title": "Attack on Titan", "genre": "Action"},
        {"title": "Naruto", "genre": "Adventure"},
        {"title": "One Piece", "genre": "Fantasy"},
    ]
    return render(request, 'core/index.html', {'anime_list': anime_list})


def search_anime(request):
    search_query = request.GET.get("query", "")  # Get the search query from the URL
    if search_query:
        anime_data = fetch_anime_data(search_query)
        return JsonResponse(anime_data)  # Return the API data as JSON
    else:
        return JsonResponse({"error": "No search query provided"}, status=400)
    

def fetch_anime_data(search_query):
    headers = {"Content-Type": "application/json"}
    variables = {"search": search_query}

    response = requests.post(
        ANILIST_API_URL,
        json={"query": ANILIST_QUERY, "variables": variables},
        headers=headers,
    )

    if response.status_code == 200:
        return response.json().get("data", {}).get("Media", {})
    else:
        return {"error": f"Failed to fetch data: {response.status_code}"}
