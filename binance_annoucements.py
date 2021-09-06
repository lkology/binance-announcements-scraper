import json
import requests
from bs4 import BeautifulSoup

def get_binance_announcement_catalogs():
    url = 'https://www.binance.com/en/support/announcement'

    response = requests.request("GET", url)

    if response.status_code != 200:
        raise RuntimeError(f'Failed to retrieve Binance Announcements Page, got status code: {response.status_code}')

    soup = BeautifulSoup(response.text, "html.parser")
    script = soup.find("script", {"id": "__APP_DATA"})

    if not script:
        raise RuntimeError('Failed to retrieve script tag from Binance Announcements Page')
        
    data = json.loads(script.string)

    return data['routeProps']['42b1']['catalogs']
