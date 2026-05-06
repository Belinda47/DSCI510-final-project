# DSCI 510 Final Project

## Introduction

This project analyzes social media engagement across TikTok, Instagram, and YouTube. The goal of the project is to explore factors that influence engagement metrics such as views, likes, comments, shares, and audience interaction.

The project focuses on comparing engagement patterns across different social media platforms and understanding how content style, livestream interaction, and promotional strategies affect user engagement.

This project was completed for DSCI 510 at the University of Southern California.

---

## Data Sources

| Data Source | Type | Description | Source URL |
|---|---|---|---|
| TikTok Dataset | Kaggle Dataset | TikTok engagement and video performance data | Add URL |
| Instagram Dataset | Kaggle Dataset | Instagram influencer and engagement analytics | Add URL |
| YouTube Data API | API | YouTube video statistics and comments | https://developers.google.com/youtube/v3 |

---

## Analysis

This project performs several types of social media analysis, including:

- Data collection and preprocessing
- Engagement comparison across platforms
- Comment and audience interaction analysis
- Visualization of engagement trends
- Livestream and promotional content analysis

Python libraries such as pandas, matplotlib, and google-api-python-client were used for data processing and analysis.

---

## Summary of Results

The analysis showed that different platforms have different engagement behaviors.

TikTok content tends to generate rapid short-term engagement, while YouTube videos maintain more stable long-term interaction. Livestream-related content also produced higher audience interaction compared to regular posts.

The project also found that audience trust and creator interaction can strongly influence engagement performance.

---
## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Belinda47/DSCI510-final-project.git
cd DSCI510-final-project
```

2. Install required libraries:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file based on `.env.example`:

```env
YOUTUBE_API_KEY=
```

4. Run the main pipeline:

```bash
python main.py
```

5. Run tests:

```bash
python tests.py
```

6. Open the results notebook:

```bash
jupyter notebook results.ipynb
```

## Challenges

Several challenges were encountered during this project.

One of the main difficulties was working with data from multiple social media platforms because each platform uses different engagement metrics and content structures. Data cleaning and standardization were necessary before performing comparisons across TikTok, Instagram, and YouTube.

Another challenge was handling API limitations and missing data. Some engagement metrics were inconsistent across datasets, which required additional preprocessing and validation.

In addition, comparing audience interaction fairly across platforms was difficult because each platform has different recommendation algorithms and user behaviors.

---

## Future Improvements

Several improvements could be made in future versions of this project.

Future work may include collecting larger datasets, adding more social media platforms, and performing deeper sentiment analysis on user comments. More advanced machine learning models could also be applied to predict engagement performance and analyze audience behavior patterns.

Additional visualizations and dashboard tools could also improve the presentation and interpretation of the analysis results.

## Project Structure

```bash
DSCI510-final-project/
│
├── src/
├── docs/
├── results.ipynb
├── tests.py
├── main.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
