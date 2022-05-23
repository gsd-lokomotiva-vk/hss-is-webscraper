import json


def load_json(filepath: str):
	with open(filepath, "r", encoding="utf-8") as f:
		json_data = json.load(f)
		return json_data
