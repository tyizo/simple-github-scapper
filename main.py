import requests
from colored import fg
from time import sleep

# Colors
green = fg(82)
dark_green = fg(77)
light_green = fg(48)

# Logo
logo = (dark_green+""" 
            _____ _ _   _   _       _       ______                                
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
        # Ask the user to put user.
        target = input(dark_green + '[+] Enter GitHub Username: ')
        # Calling the api.
        r = requests.get(f'https://api.github.com/users/{target}')
        name = '[-] Name: ' + str(r.json()['name'] + '\n')
        bio = '[-] Bio: ' + str(r.json()['bio'] + '\n')
        idd = '[-] Username id: ' + str(r.json()['id']) + '\n'
        avatar_url = '[-] Avatar url is: ' + r.json()['avatar_url'] + '\n'
        print(light_green + name + bio + idd + avatar_url + '\n')

        print(dark_green + '[*] Done! , you can close the app.')
        re = input('[*] Do you wanna repeat ? y/n: ')
        # Reapet the app again .
        while True:
            if re == 'y':
                target = input(dark_green + '[+] Enter GitHub Username: ')
                r = requests.get(f'https://api.github.com/users/{target}')
                name = 'Name: ' + str(r.json()['name'] + '\n')
                bio = 'Bio: ' + str(r.json()['bio'] + '\n')
                idd = 'Username id: ' + str(r.json()['id']) + '\n'
                avatar_url = 'Avatar url is: ' + r.json()['avatar_url'] + '\n'
                print(light_green + name + bio + idd + avatar_url + '\n')
            elif re == 'n':
                print('[!] Bye Bye !')
                sleep(2)
                exit()
                break

    elif ask == 'n':
        print('[!] Bye Bye !')
        sleep(2)
        exit()

        """
        I remove it cuz i have an error in at: TypeError: unsupported operand type(s) for +: 'int' and 'str'
        I'll fix it in the next version        
        followers = 'Followers: ' + str(r.json()['followers'] + '\n')
        following = 'Following: ' + str(r.json()['following'] + '\n') 
        """

except Exception as e:
    # Error
    print('\n')
    input('[!] There is an error!')
    sleep(2)
    exit()
    