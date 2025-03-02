import requests, os
from requests.exceptions import Timeout

if os.name == 'posix':
    os.system('clear')
else:
    os.system('cls')

file_name = input("LIST URL [.txt] : ")
with open(file_name, 'r') as file:
    urls = file.readlines()

red = str('\033[1;91m')
green = str('\033[1;32m')
white = str('\033[0m')

for url in urls:
    url = url.strip()  # Menghapus karakter baris baru di akhir setiap URL yang dibaca
    try:
        response = requests.get(url, timeout=4)  # Set timeout menjadi 4 detik
        if response.status_code == 200:
            cookies = response.cookies
            if cookies:
                a = '\n' + url + green + ' [ HAS COOKIES ] - ' + white + str(response.status_code)
                print(a)
                loc = 'hascookies.txt'
                with open(loc, 'a') as file:
                    file.write(str(a) + '\n')
                for cookie in cookies:
                    print('\ncookie name:' + '\n' + cookie.name, ":", '\ncookie value:' + '\n' + cookie.value)
            else:
                print('\n' + url + red + ' [ NO COOKIES ] - ' + white + str(response.status_code))
        else:
            print('\n' + url + red + ' [ ERROR ] - ' + white + str(response.status_code))
    except Timeout:
        print('\n' + url + red + ' [ TIMEOUT ] - ' + white + 'Connection timed out')
        continue
    except Exception as e:
        print('\n' + url + red + ' [ ERROR ] - ' + white + str(e))
        continue

print('done')
