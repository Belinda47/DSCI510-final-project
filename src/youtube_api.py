from googleapiclient.discovery import build

def get_youtube_data(api_key):

    youtube = build("youtube", "v3", developerKey=api_key)

    request = youtube.search().list(
        part="snippet",
        q="social media",
        type="video",
        maxResults=50
    )

    response = request.execute()

    return response
