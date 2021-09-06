import json
import os.path

def load_articles(file):
    if not os.path.isfile(file):
        return []

    with open(file, "r+") as f:
        return json.load(f)

def save_articles(file, articles):
    with open(file, 'w') as f:
        json.dump(articles, f, indent=4)   