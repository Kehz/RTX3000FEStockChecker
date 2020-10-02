# RTX3080StockChecker
Simple python script that will play a sound and launch the website when chosen RTX 3000 series is in stock. It will not add to cart and checkout for you.
Intended for you to not have to spam refresh all day waiting. When 3070 Lanches it'll be added as well
THIS IS ONLY FOR THE FOUNDERS EDITIONS LOCATED ON NVIDIA'S WEBSITE


## Intructions
1. Download and Install latest version of Python from [Here](https://www.python.org/downloads/) 
2. Download the source folder [Here](https://github.com/Kehz/RTX3000FEStockChecker/archive/master.zip) and extract it wherever. 
3. Open up your command prompt and type "pip install playsound" and "pip install requests".
4. Run "run.bat" or through python by doing "python stockchecker.py" in a terminal
5. Choose which card you want through the terminal by inputting (1) or (2) etc..

## Options
You can change some of the code to refresh at a faster rate than the default by changing the code on line 58
gen_random_interval = random.randint(8, 15) sets it to refresh between a random interval between 8 and 15. Change those values to what you want. Lower values MAY cause the site to ip ban you for a bit but im not too sure since it hasn't happened to me yet.

You can also change the alert sound thats played by replacing  "bell.mp3" that is located in the downloaded folder RTX3000FESTOCKCHECKER.
For simplicity's sake just make sure that your new alert sound is nammed "bell.mp3" or you can just change the code on line 50 playsound('bell.mp3') to the name of your new file
