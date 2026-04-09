from googleapiclient.discovery import build

api_key = "YOUR_API_KEY"

youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.search().list(
    part="snippet",
    q="social media",
    type="video",
    maxResults=50
)

response = request.execute()

print(response)
