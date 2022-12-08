import requests
import time
from colorama import Fore
import random
import sys
import os

try:
    EnterWebsite = sys.argv[1]
except:
    print(Fore.CYAN + 'Usage:\npython fuzzer.py https://example.com' + Fore.RESET)
    exit()

print(os.path.basename(EnterWebsite))
dir_names = open('directory-names.txt', 'r')

for dir in dir_names:
    url = EnterWebsite + "/" + dir.strip()
    requestWebsite = requests.get(url)
    status_code = requestWebsite.status_code
    randomInt = random.randint(0, 1)

    if status_code == 429: #429 is the response if the server gets to many requests, so put a little delay in here (A.K.A. Ratelimit)
        time.sleep(8)
    else:
        if status_code == 200:
            print(Fore.GREEN + f'[{status_code}] valid!  -  URL: {url}')
        else:
            print(Fore.RED + f'[{status_code}] invalid!  -  URL: {url}')
    time.sleep(randomInt)