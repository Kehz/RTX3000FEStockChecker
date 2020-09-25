import urllib.request
import random
from playsound import playsound
import webbrowser
import requests, json, time
from datetime import datetime
from time import sleep

# Checks whether or not the item is in stock.
# If in stock it will launch the webpage indicated in launch_on_alert on your default browser
# and play the sound file bell.mp3
def check_stock(): 
    stock_page = 'https://api-prod.nvidia.com/direct-sales-shop/DR/products/en_us/USD/5438481700'
    launch_on_alert = 'https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3080/'
    stock_api = requests.get(stock_page)
    stock = json.loads(stock_api.content)
    item_name = stock['products']['product'][0]['displayName']
    stock_status = stock['products']['product'][0]['inventoryStatus']['status']
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if (stock_status != 'PRODUCT_INVENTORY_OUT_OF_STOCK'):
        print(f'Item : [{item_name}] is now in stock at {current_time}. Launching webpage')
        webbrowser.open(launch_on_alert, new=1)
        playsound('bell.mp3')
    
    else:
        print(f'Item : [{item_name}] is out of stock at {current_time}')
# Randomly checks stock between a peroid of 8 to 15 seconds
# Feel free to change intervals but MAY be risky checking to often
def random_check():
    while True:
        gen_random_interval = random.randint(8, 15)
        check_stock()
        print(f'Checking stock again in {gen_random_interval} seconds')
        sleep(gen_random_interval)
random_check()

