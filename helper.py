import ijson
import json
from typing import Dict, List, Generator, Any

def process_json_file(filename:str, prefix:str = 'item') -> Generator[Dict[str, Any], None, None]:
	try:
		with open(filename, 'rb') as file:
			yield from ijson.items(file, prefix)
	
	except FileNotFoundError as e:
		print(f"ERROR: file not found at {filename}")
	except ijson.JSONError as e:
		print(f"ERROR: JSON parsing failed {e}")