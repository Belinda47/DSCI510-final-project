# AI generated:

import pandas as pd


def compare_platforms(instagram_df, tiktok_df, youtube_df):

    instagram_avg = instagram_df["comment_rate"].mean()

    tiktok_avg = tiktok_df["engagement_rate"].mean()

    youtube_avg = youtube_df["engagement_rate"].mean()

    comparison = pd.DataFrame({
        "Platform": ["Instagram", "TikTok", "YouTube"],
        "Average Engagement": [
            instagram_avg,
            tiktok_avg,
            youtube_avg
        ]
    })

    print("\nPlatform Comparison:")
    print(comparison)

    return comparison
