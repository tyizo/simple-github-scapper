import requests
from colored import fg
from time import sleep

# Colors
green = fg(82)
dark_green = fg(77)
light_green = fg(48)

# Logo
logo = (dark_green+""" 

            _____ _ _   _   _        _      ______                                
            |  __ (_) | | | | |     | |     /  ___|                                
            | |  \/_| |_| |_| |_   _| |__   \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
            | | __| | __|  _  | | | | '_ \   `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
            | |_\ \ | |_| | | | |_| | |_) | /\__/ / (_| (_| | |_) | |_) |  __/ |   
            \____/_|\__\_| |_/\__,_|_.__/   \____/ \___\__,_| .__/| .__/ \___|_|   
                                                | |   | |              
                                                |_|   |_|                           - By Tyizo!\n""")
print(logo)

try:
    ask = input('[+] Do you love Tyizo ? y/n: ')
    if ask == 'y':
        # Ask user to put the username.
        target = input(dark_green + '[+] Enter GitHub Username: ')
        # Calling The Api.
        r = requests.get(f'https://api.github.com/users/{target}')
        # Info
        # ============================================================
        name = 'Name: ' + str(r.json()['name']) + '\r'
        bio = 'Bio: ' + str(r.json()['bio']) + '\r'
        idd = 'Username id: ' + str(r.json()['id']) + '\r'
        followers = 'Followers: ' + str(r.json()['followers']) + '\r'
        following = 'Following: ' + str(r.json()['following']) + '\r'
        avatar_url = 'Avatar url is: ' + r.json()['avatar_url'] + '\n'
        # ============================================================
        print(light_green + name + bio + idd)
        print(light_green + followers)
        print(light_green + following)
        print(light_green + avatar_url)

        print(dark_green + '[*] Done! , you can close the app.')
        re = input('[*] Do you wanna repeat ? y/n: ')
        # Reapet the app again .
        while True:
            if re == 'y':
                target = input(dark_green + '[+] Enter GitHub Username: ')
                r = requests.get(f'https://api.github.com/users/{target}')
                # ============================================================
                name = 'Name: ' + str(r.json()['name']) + '\r'
                bio = 'Bio: ' + str(r.json()['bio']) + '\r'
                idd = 'Username id: ' + str(r.json()['id']) + '\r'
                followers = 'Followers: ' + str(r.json()['followers']) + '\r'
                following = 'Following: ' + str(r.json()['following']) + '\r'
                avatar_url = 'Avatar url is: ' + r.json()['avatar_url'] + '\n'
                # ============================================================
                print(light_green + name + bio + idd)
                print(light_green + followers)
                print(light_green + following)
                print(light_green + avatar_url)
                print(dark_green + '[*] Done! , you can close the app.')
                re = input('[*] Do you wanna repeat ? y/n: ')
                continue
            elif re == 'n':
                print('[!] Bye Bye !')
                sleep(2)
                exit()
                break

    elif ask == 'n':
        print('[!] Bye Bye !')
        sleep(2)
        exit()

except Exception as e:
    # Error
    print('\n')
    input('[!] There is an error!')
    sleep(2)
    exit()

# and yeah that's it!