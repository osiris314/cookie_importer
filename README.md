# cookie_importer
chrome cookie importer

pyVer: 3+

install dependencies: pip install -r requirements.txt

execute: python cookie_importer.py

1) Asks for target website:

![options_menu](https://user-images.githubusercontent.com/29146438/212049676-63740ecc-4922-411a-bd3a-7b1010be6a44.PNG)

if cookie file for target website inside folder cookies is empty,

asks you to manually paste the cookies

![blured_manual_cookies](https://user-images.githubusercontent.com/29146438/212050190-586f6961-d770-425e-a572-b288b9421f41.png)

and opens the target website on a new chrome window with imported cookies.

![blured_logged_in](https://user-images.githubusercontent.com/29146438/212050681-a0d9d3fa-ff5c-4e78-95d0-c6802cdf8095.png)

Required cookies for known websites:

![website_cookies_list](https://user-images.githubusercontent.com/29146438/214552057-43490d23-6228-4dc8-9445-10bf9c8e673e.png)



setup cookie files:

+++++++++++++++++++++++++++++

facebook_cookies.txt

line 1: 'xs_cookie_value'

line 2: 'c_user_cookie_value'

+++++++++++++++++++++++++++++

google_cookies.txt

line 1: 'HSID_cookie_value'

line 2: 'SID_cookie_value'

line 3: 'SSID_cookie_value'

+++++++++++++++++++++++++++++

instagram_cookies.txt

line 1: 'sessionid_cookie_value'

+++++++++++++++++++++++++++++

twitter_cookies.txt

line 1: 'auth_token_cookie_value'

+++++++++++++++++++++++++++++
