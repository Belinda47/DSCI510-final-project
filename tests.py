from src.youtube_api import get_youtube_data

# AI generated:

def test_youtube_api():
    api_key = "YOUR_API_KEY"

    data = get_youtube_data(api_key)

    assert "items" in data
    print("API works!")
    print("Number of videos retrieved:", len(data["items"]))


if __name__ == "__main__":
    test_youtube_api()
