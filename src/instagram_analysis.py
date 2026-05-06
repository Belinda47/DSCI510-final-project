# AI generated:

import pandas as pd
import matplotlib.pyplot as plt


def hashtag_group(x):
    if x <= 2:
        return "Low (0-2)"
    elif x <= 5:
        return "Medium (3-5)"
    else:
        return "High (6+)"


def load_instagram_data(file_path):
    ig = pd.read_csv(file_path)
    return ig


def prepare_instagram_data(ig):
    ig["std_engagement_rate"] = (ig["likes"] + ig["comments"]) / ig["reach"]
    ig["topic"] = ig["content_category"].str.lower()
    ig["hashtag_group"] = ig["hashtags_count"].apply(hashtag_group)
    return ig


def run_instagram_analysis(file_path):
    ig = load_instagram_data(file_path)
    ig = prepare_instagram_data(ig)

    print("Instagram average engagement rate:")
    print(ig["std_engagement_rate"].mean())

    print("\nAverage comment rate by media type:")
    print(ig.groupby("media_type")["comment_rate"].mean())

    print("\nAverage comment rate by hashtag group:")
    print(ig.groupby("hashtag_group")["comment_rate"].mean())

    print("\nTop topics by comment rate:")
    print(ig.groupby("topic")["comment_rate"].mean().sort_values(ascending=False).head(5))

    return ig
