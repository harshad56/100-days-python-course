from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Start Chrome browser using Selenium
driver = webdriver.Chrome()

# Open the Google Chrome Dino game
driver.get('chrome://dino')

# Wait for the game to load
time.sleep(2)

# Find the game body to send commands
game_body = driver.find_element_by_tag_name('body')

# Press space to start the game
game_body.send_keys(Keys.SPACE)

# Simulate the game by making the dinosaur jump every 1 second (you can adjust the timing)
while True:
    game_body.send_keys(Keys.SPACE)
    time.sleep(1)
