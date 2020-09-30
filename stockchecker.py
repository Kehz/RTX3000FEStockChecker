"""This script scans for changes in the store api pages check if an chosen card is in stock
if it is instock then it will open the webpage of selected graphics card and play a notification
sound"""
import random
import webbrowser
import json
from time import sleep
from datetime import datetime
from playsound import playsound
import requests


STOCK_PAGE = ''
LAUNCH_PAGE = ''

def select_card():
    """Runs on startup and allows for user to input which card they want to search for."""
    global STOCK_PAGE
    global LAUNCH_PAGE
    stock_3090 = 'https://api-prod.nvidia.com/direct-sales-shop/DR/products/en_us/USD/5438481600'
    page_3090 = 'https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090/'
    stock_3080 = 'https://api-prod.nvidia.com/direct-sales-shop/DR/products/en_us/USD/5438481700'
    page_3080 = 'https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3080/'

    choice = int(input('Enter the number choice for which card you want\n[1] RTX 3080\n[2] RTX 3090\n'))

    if choice == 1:
        STOCK_PAGE = stock_3080
        LAUNCH_PAGE = page_3080
    elif choice == 2:
        STOCK_PAGE = stock_3090
        LAUNCH_PAGE = page_3090

def check_stock():
    """Checks the api to see if the inventory is out of stock
    and will launch website when in instock"""
    stock_api = requests.get(STOCK_PAGE)
    try:
        stock = json.loads(stock_api.content)
    except json.decoder.JSONDecodeError:
        print('API IS NOT RESPONDING. LINK MAY BE DOWN, PLEASE WAIT UNTIL IT IS BACK UP.')
        return
    item_name = stock['products']['product'][0]['displayName']
    stock_status = stock['products']['product'][0]['inventoryStatus']['status']
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if stock_status != 'PRODUCT_INVENTORY_OUT_OF_STOCK':
        print(f'Item : [{item_name}] is now in stock at {current_time}. Launching webpage')
        playsound('bell.mp3')
        webbrowser.open(LAUNCH_PAGE, new=1)
        halt = input('Press ENTER to continue scanning for stock')
    else:
        print(f'Item : [{item_name}] is out of stock at {current_time}')

def random_check():
    """Randomly checks stock between a peroid of 8 to 15 seconds
    Feel free to change intervals but MAY be risky checking to often"""
    while True:
        gen_random_interval = random.randint(8, 15)
        check_stock()
        print(f'Checking stock again in {gen_random_interval} seconds')
        sleep(gen_random_interval)
select_card()
random_check()
