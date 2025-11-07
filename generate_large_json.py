import json, random
from datetime import datetime, timedelta

num_tweets = 50000
start_date = datetime(2022, 1, 1)
tweets = []

for i in range(num_tweets):
    tweet_id = 1590000000000000000 + i
    created_at = (start_date + timedelta(minutes=i)).isoformat() + "Z"
    user_id = 987654321

    tweet = {
        "tweet": {
            "id_str": str(tweet_id),
            "created_at": created_at,
            "full_text": f"This is sample tweet number {i} generated for ijson performance testing.",
            "entities": {
                "hashtags": [{"text": f"Tag{i%10}", "indices": [0, 10]}],
                "user_mentions": [{"screen_name": f"user{i%100}", "name": f"User {i%100}"}],
                "urls": [{"expanded_url": "https://example.com"}],
            },
            "user": {
                "id": user_id,
                "screen_name": "michael_sample",
                "statuses_count": 5000 + i,
                "lang": "en"
            }
        }
    }
    tweets.append(tweet)

with open("large_tweet_archive_50MB.json", "w", encoding="utf-8") as f:
    json.dump(tweets, f)