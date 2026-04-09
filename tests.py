from src.youtube_api import get_youtube_data

api_key = "YOUR_API_KEY"

data = get_youtube_data(api_key)

print("API works!")
print("Number of videos retrieved:", len(data["items"]))
