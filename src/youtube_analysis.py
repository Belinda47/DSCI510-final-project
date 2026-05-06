# AI generated:

import pandas as pd
import matplotlib.pyplot as plt


def load_youtube_data(file_path):
    youtube = pd.read_csv(file_path)
    return youtube


def prepare_youtube_data(youtube):
    youtube["engagement_rate"] = (
        youtube["likes"] +
        youtube["comments"]
    ) / youtube["views"]

    return youtube


def run_youtube_analysis(file_path):
    youtube = load_youtube_data(file_path)
    youtube = prepare_youtube_data(youtube)

    print("YouTube average engagement rate:")
    print(youtube["engagement_rate"].mean())

    print("\nTop YouTube videos by engagement:")
    print(
        youtube.sort_values(
            by="engagement_rate",
            ascending=False
        ).head(5)
    )

    return youtube
