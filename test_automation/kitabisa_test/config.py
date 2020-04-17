from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PIL import Image
import os

class browser():
    options = webdriver.ChromeOptions()
    #forbid auto-close
    options.add_experimental_option("detach", True)
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    #start browser on full screen
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
