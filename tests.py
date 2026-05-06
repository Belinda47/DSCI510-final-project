# AI generated:

import pandas as pd

from src.instagram_analysis import hashtag_group
from src.tiktok_analysis import prepare_tiktok_data
from src.youtube_analysis import prepare_youtube_data


def test_hashtag_group():
    assert hashtag_group(1) == "Low (0-2)"
    assert hashtag_group(4) == "Medium (3-5)"
    assert hashtag_group(7) == "High (6+)"
    print("Instagram hashtag group test passed.")


def test_tiktok_engagement_rate():
    sample_data = pd.DataFrame({
        "likes": [100],
        "comments": [20],
        "shares": [10],
        "views": [1000]
    })

    result = prepare_tiktok_data(sample_data)

    assert "engagement_rate" in result.columns
    assert result["engagement_rate"].iloc[0] == 0.13
    print("TikTok engagement rate test passed.")


def test_youtube_engagement_rate():
    sample_data = pd.DataFrame({
        "likes": [200],
        "comments": [50],
        "views": [1000]
    })

    result = prepare_youtube_data(sample_data)

    assert "engagement_rate" in result.columns
    assert result["engagement_rate"].iloc[0] == 0.25
    print("YouTube engagement rate test passed.")


if __name__ == "__main__":
    test_hashtag_group()
    test_tiktok_engagement_rate()
    test_youtube_engagement_rate()

    print("All tests passed.")
