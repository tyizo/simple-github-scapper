try:
    import requests
except ImportError:
    print('Please install requests library!')
try:
    from colored import fg
except ImportError:
    print('Please install colored library!')
try:
    from time import sleep
except ImportError:
    print('Please install time library!')

green = fg(82) # Colors
dark_green = fg(77)
light_green = fg(48)

logo = (dark_green+""" 
            _____ _ _   _   _        _      ______                                
            |  __ (_) | | | | |     | |     /  ___|                                
            | |  \/_| |_| |_| |_   _| |__   \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
            | | __| | __|  _  | | | | '_ \   `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
            | |_\ \ | |_| | | | |_| | |_) | /\__/ / (_| (_| | |_) | |_) |  __/ |   
            \____/_|\__\_| |_/\__,_|_.__/   \____/ \___\__,_| .__/| .__/ \___|_|   
                                                | |   | |              
                                                |_|   |_|                           - By Tyizo!\n""") # Logo
print(logo)
try:
    ask = input('[+] Do you love Tyizo ? y/n: ')
    if ask == 'y':
        while True:
            def scapper():
                # Ask user to put the username.
                target = input(dark_green + '[+] Enter GitHub Username: ')
                # Calling The Api.
                r = requests.get(f'https://api.github.com/users/{target}')
                name = 'Name: ' + str(r.json()['name']) + '\r'
                bio = 'Bio: ' + str(r.json()['bio']) + '\r'
                idd = 'Username id: ' + str(r.json()['id']) + '\r'
                followers = 'Followers: ' + str(r.json()['followers']) + '\r'
                following = 'Following: ' + str(r.json()['following']) + '\r'
                avatar_url = 'Avatar url is: ' + r.json()['avatar_url'] + '\n'
                print(light_green + name + bio + idd)
                print(light_green + followers)
                print(light_green + following)
                print(light_green + avatar_url)
                print(dark_green + '[*] Done! , you can close the app.')
            scapper()
            break

        re = input('[*] Do you wanna repeat ? y/n: ')
        if re == 'y' or re == 'Y': scapper()
        elif re == 'n' or re == 'N':
            input('Bye bye!')
            sleep(3)
            exit()
    else:
        print('Bye!')
        sleep(3)
except NameError:
    print('[!] There is an error!')
    sleep(2)
    exit()
