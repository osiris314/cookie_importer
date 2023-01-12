from selenium import webdriver
import time
import os
import colorama
from colorama import Fore

colorama.init(autoreset=True)

global domain
global option
lines = []

os.system('cls')
print(Fore.GREEN + '1) ' + Fore.WHITE + 'Facebook')
print(Fore.GREEN + '2) ' + Fore.WHITE + 'Google')
print(Fore.GREEN + '3) ' + Fore.WHITE + 'Instagram')
print(Fore.GREEN + '4) ' + Fore.WHITE + 'Twitter')

website_option = input('Type option: ' + Fore.GREEN)

print(Fore.WHITE)
os.system('cls')

if website_option == '1':
    cookie_file = (r'cookies/facebook_cookies.txt')
    option = 'facebook'
elif website_option == '2':
    cookie_file = (r'cookies/google_cookies.txt')
    option = 'google'
elif website_option == '3':
    cookie_file = (r'cookies/instagram_cookies.txt')
    option = 'instagram'
elif website_option == '4':
    cookie_file  = (r'cookies/twitter_cookies.txt')
    option = 'twitter'

with open(cookie_file, 'r') as fp:
    line_numbers = [0, 1, 2]
    for i, line in enumerate(fp):
        if i in line_numbers:
            lines.append(line.strip())
        elif i > 5:
            break

if os.path.getsize('cookies/facebook_cookies.txt') == 0 and option == 'facebook':
    print(Fore.RED + 'Cookie File is empty!' + Fore.WHITE)
    print(Fore.YELLOW + 'Manualy type cookie values.' + Fore.WHITE)
    xs = input('Type ' + Fore.CYAN + 'XS ' + Fore.WHITE + 'value: ')
    lines.append(xs)
    c_user = input('Type ' + Fore.CYAN + 'C_USER ' + Fore.WHITE + 'value: ')
    lines.append(c_user)

if os.path.getsize('cookies/google_cookies.txt') == 0 and option == 'google':
    print(Fore.RED + 'Cookie File is empty!' + Fore.WHITE)
    print(Fore.YELLOW + 'Manualy type cookie values.' + Fore.WHITE)
    hsid = input('Type ' +Fore.CYAN + 'HSID ' + Fore.WHITE + 'value: ')
    lines.append(hsid)
    sid = input('Type ' + Fore.CYAN + 'SID ' + Fore.WHITE + 'value: ')
    lines.append(sid)
    ssid = input('Type ' + Fore.CYAN + 'SSID' + Fore.WHITE + 'value: ')
    lines.append(ssid)

if os.path.getsize('cookies/instagram_cookies.txt') == 0 and option == 'instagram':
    print(Fore.RED + 'Cookie File is empty!' + Fore.WHITE)
    print(Fore.YELLOW + 'Manualy type cookie values.' + Fore.WHITE)
    session_id = input('Type ' + Fore.CYAN + 'SESSIONID ' + Fore.WHITE + 'value: ')
    lines.append(session_id)

if os.path.getsize('cookies/twitter_cookies.txt') == 0 and option == 'twitter':
    print(Fore.RED + 'Cookie File is empty!' + Fore.WHITE)
    print(Fore.YELLOW + 'Manualy type cookie values.' + Fore.WHITE)
    auth_token = input('Type ' + Fore.CYAN + 'AUTH_TOKEN ' + Fore.WHITE + 'value: ')
    lines.append(auth_token)

browser = webdriver.Chrome()

def load_facebook_cookies():
    try:
        browser.add_cookie({"name": "xs", "domain":domain, "value": lines[0]})
        browser.add_cookie({"name": "c_user", "domain":domain, "value": lines[1]})
        browser.refresh()
        while True:
            time.sleep(99999)
    except Exception as e:
        print(Fore.RED + e + Fore.RED + '')
        browser.close()

def load_google_cookies():
    try:
        browser.add_cookie({"name": "HSID", "domain":domain, "value": lines[0]})
        browser.add_cookie({"name": "SID", "domain":domain, "value": lines[1]})
        browser.add_cookie({"name": "SSID", "domain":domain, "value": lines[2]})
        browser.refresh()
        while True:
            time.sleep(99999)
    except Exception as e:
        print(Fore.RED + e + Fore.RED + '')
        browser.close()
    
def load_instagram_cookies():
    try:
        browser.add_cookie({"name": "sessionid", "domain":domain, "value": lines[0]})
        browser.refresh()
        while True:
            time.sleep(99999)
    except Exception as e:
        print(Fore.RED + e + Fore.RED + '')
        browser.close()

def load_twitter_cookies():
    try:
        browser.add_cookie({"name": "auth_token", "domain":domain, "value": lines[0]})
        browser.refresh()
        while True:
            time.sleep(99999)
    except Exception as e:
        print(Fore.RED + e + Fore.RED + '')
        browser.close()

if website_option == '1':
    domain = 'www.facebook.com'
    browser.get("https://www.facebook.com")
    load_facebook_cookies()
elif website_option == '2':
    domain = 'www.google.com'
    browser.get("https://www.google.com")
    load_google_cookies()
elif website_option == '3':
    domain = 'instagram.com'
    browser.get("https://www.instagram.com")
    load_instagram_cookies()
elif website_option == '4':
    domain = 'twitter.com'
    browser.get("https://www.twitter.com")
    load_twitter_cookies()