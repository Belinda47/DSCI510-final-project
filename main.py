# AI generated:

from src.config import INSTAGRAM_DATA_PATH, TIKTOK_DATA_PATH, YOUTUBE_DATA_PATH
from src.instagram_analysis import run_instagram_analysis
from src.tiktok_analysis import run_tiktok_analysis
from src.youtube_analysis import run_youtube_analysis
from src.platform_comparison import compare_platforms


def main():
    print("Running DSCI 510 Final Project Pipeline")

    instagram_df = run_instagram_analysis(INSTAGRAM_DATA_PATH)
    tiktok_df = run_tiktok_analysis(TIKTOK_DATA_PATH)
    youtube_df = run_youtube_analysis(YOUTUBE_DATA_PATH)

    comparison = compare_platforms(instagram_df, tiktok_df, youtube_df)

    print("\nFinal comparison completed.")
    print(comparison)


if __name__ == "__main__":
    main()
