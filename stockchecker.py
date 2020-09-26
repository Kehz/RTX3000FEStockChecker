import urllib.request
import random
from playsound import playsound
import webbrowser
import requests, json, time
from datetime import datetime
from time import sleep

stock_page = ''
launch_on_alert = ''

# Runs on startup and allows for user to input which card they want to search for.
def select_card():
    global stock_page 
    global launch_on_alert
    rtx_3090_stock = 'https://api-prod.nvidia.com/direct-sales-shop/DR/products/en_us/USD/5438481600'
    rtx_3090_page = 'https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090/'
    rtx_3080_stock = 'https://api-prod.nvidia.com/direct-sales-shop/DR/products/en_us/USD/5438481700'
    rtx_3080_page = 'https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3080/'

    choice = int(input("Enter the number choice for which card you want. \n [1] RTX 3080 \n [2] RTX 3090 \n"))
   
    if (choice == 1):
        stock_page = rtx_3080_stock
        launch_on_alert = rtx_3080_page
    elif (choice == 2):
        stock_page = rtx_3090_stock
        launch_on_alert = rtx_3090_page

# Checks whether or not the item is in stock.
# If in stock it will launch the webpage indicated in launch_on_alert on your default browser
# and play the sound file bell.mp3
def check_stock(): 
    stock_api = requests.get(stock_page)
    try:
        stock = json.loads(stock_api.content)
    except json.decoder.JSONDecodeError:
        print('API IS NOT RESPONDING. LINK MAY BE DOWN, PLEASE WAIT UNTIL IT IS BACK UP.')
        return
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
select_card()
random_check()

