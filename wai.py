import requests
import time
from urllib.parse import urlparse, parse_qs
import json

headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://app.w-coin.io',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://app.w-coin.io/'
}
def wai(session_url):
    parsed_url = urlparse(session_url)
    query_params = parse_qs(parsed_url.fragment)
    tgWebAppData = query_params.get('tgWebAppData', [None])[0]
    user_data = json.loads(parse_qs(tgWebAppData)['user'][0])
    identifier = str(user_data['id'])
    json_data = {
                'identifier':identifier,
                'password': identifier,
            }
    res = requests.post('https://starfish-app-fknmx.ondigitalocean.app/wapi/api/auth/local', json=json_data).json()
    headers['authorization'] =  'Bearer '+res['jwt']
    response = requests.get(
        'https://starfish-app-fknmx.ondigitalocean.app/wapi/api/users-permissions/passive-income/claim?timestamp='+str(int(time.time()))+'}&hash='+tgWebAppData,
        headers=headers,
    )
    print(response.json())
    
if __name__ =='__main__':
    url = input('Enter your session link : ')
    wai(url)
