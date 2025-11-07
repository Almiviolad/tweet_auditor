import ijson
import json
from typing import Dict, List, Generator, Any

def process_json_file(filename:str, prefix:str = 'item') -> Generator[Dict[str, any]]:
	try:
		with open(filename, 'rb') as file:
			yield from ijson.items(file, prefix)
	
	except FileNotFoundError as e:
		print(f"ERROR: file not found at {filename}")
	except ijson.JSONError as e:
		print(f"ERROR: JSON parsing failed {e}")


filename = "large_tweet_archive_50MB.json"
JSON_PREFIX = "item"

for tweet in process_json_file(filename, JSON_PREFIX):
	tweet_id = tweet.get("tweet").get("")
	tweet_text = tweet.get('tweet', "Malformed tweet for tweet {")
	tweet_text = tweet.get("tweet", "Malformed tweet").get("full_text", "No text found for tweet{tweet.get")