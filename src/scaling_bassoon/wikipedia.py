import requests


def random_page(lang: str):
    api_url = f"https://{lang.lower()}.wikipedia.org/api/rest_v1/page/random/summary"
    with requests.get(api_url) as response:
        response.raise_for_status()
        return response.json()

