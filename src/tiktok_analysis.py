# AI generated:

import pandas as pd
import matplotlib.pyplot as plt


def load_tiktok_data(file_path):
    tiktok = pd.read_csv(file_path)
    return tiktok


def prepare_tiktok_data(tiktok):
    tiktok["engagement_rate"] = (
        tiktok["likes"] +
        tiktok["comments"] +
        tiktok["shares"]
    ) / tiktok["views"]

    return tiktok


def run_tiktok_analysis(file_path):
    tiktok = load_tiktok_data(file_path)
    tiktok = prepare_tiktok_data(tiktok)

    print("TikTok average engagement rate:")
    print(tiktok["engagement_rate"].mean())

    print("\nTop TikTok videos by engagement:")
    print(
        tiktok.sort_values(
            by="engagement_rate",
            ascending=False
        ).head(5)
    )

    return tiktok
