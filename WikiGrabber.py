import requests

def fetch_wikipedia_full(topic):
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": True,
        "titles": topic,
        "redirects": 1
    }

    headers = {
        "User-Agent": "MyWikipediaApp/1.0 (contact: youremail@example.com)"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        return f"failed to fetch ({response.status_code})"

    data = response.json()
    pages = data["query"]["pages"]

    # pages is a dict with unknown key (page id), so we extract it like this:
    page = next(iter(pages.values()))

    return page.get("extract", "no content found")


print("starting...")

topic = input("what topic do you want to learn about? ")
text = fetch_wikipedia_full(topic)

print(text)