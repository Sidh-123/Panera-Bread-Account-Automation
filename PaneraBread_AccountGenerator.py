# Website for joining My Panera:
    # https://www.panerabread.com/en-us/mypanera/sign-up-with-mypanera.html
    
# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as ec
from datetime import date, timedelta, datetime
import string
import random
import numpy as np
import re
import time
from fake_useragent import UserAgent
import undetected_chromedriver as uc
import pandas as pd
import gspread as gs
import pygsheets as pg
import gspread_pandas as gsp
from seleniumbase import Driver
import subprocess

# Extra Functions
def password_generator():
    password = ''
    for index in range(6):
        password += random.choice(string.ascii_letters)
    password += str(random.randint(0,9))
    password += "$"
    return password

def date_in_x_days(x):
    today = date.today()
    plus_x_days = today + timedelta(x)
    formatted_date = str(plus_x_days)[5:7] + str(plus_x_days)[7:]
    formatted_date = re.sub('-', '', formatted_date)  
    return formatted_date

def random_phone_no():
    phone_no = '630'
    for index in range(7):
        phone_no += str(random.randint(0,9))
    return phone_no

def random_email_letters():
    email = ''
    for index in range(20):
        email += str(random.choice(string.ascii_letters))
    email += "@gmail.com"
    return email

def random_email_names():
    df = pd.read_csv('list_of_names.csv', header=None)
    email = str(df.sample(n=1).iloc[0,0]) + str(df.sample(n=1).iloc[0,0]) + str(df.sample(n=1).iloc[0,0]) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + '@gmail.com'
    return email

def write_to_sheet(service_path, spreadsheet_id, sheet_name, dataframe):
    gc = pg.authorize(service_file=service_path)
    sh = gc.open_by_key(spreadsheet_id)
    wks = sh[0]
    wks.append_table(start='A1', values = dataframe.values.tolist(), dimension='ROWS', overwrite=False)

# Main function

def create_account():
    # Set browser for Chrome
    options = uc.ChromeOptions()
    # path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    options.add_argument('--start-maximized')
    user_agent = UserAgent()
    user_agent_rand = user_agent.random
    print(user_agent_rand)
    # user_agent_rand = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    options.add_argument(f'--user-agent={user_agent_rand}')
    # options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_experimental_option('useAutomationExtension', False)
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_argument("--headless")
    # options.add_argument('--proxy-server=107.152.98.5:4145')
    browser = uc.Chrome(options=options)
    # browser = Driver(uc=True, incognito=True)
    print('Browser/driver created.')
    # browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    # browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    time.sleep(random.uniform(3.5, 5))
    browser.delete_all_cookies()
    print("Cookies Deleted.")

    time.sleep(random.uniform(3.5, 5))

    # Action Chains Object for Moving Cursor
    actions = ActionChains(browser)
    
    # Wait Period
    wait_period = WebDriverWait(browser, 30)

    time.sleep(random.uniform(3.5, 5))

    # Access join website for Panera Bread
    # browser.get('https://www.panerabread.com/en-us/mypanera/meet-mypanera.html')
    # browser.get('https://www.panerabread.com/en-us/home.html')
    browser.get('https://www.panerabread.com/en-us/mypanera/sign-up-with-mypanera.html')
    print('Initial Website Accessed.')
    # time.sleep(random.randint(1,5))
    # join_elem = wait_period.until(ec.element_to_be_clickable((By.XPATH, '//a[@title="Join MyPanera"]')))
    # join_elem.click()
    # print("Join Button Clicked.")
    time.sleep(random.uniform(3.5, 5))
        
    # First Name Elem
    # time.sleep(random.randint(1,5))
    time.sleep(random.uniform(3.5, 5))
    first_name_elem = wait_period.until(ec.presence_of_element_located((By.XPATH, '//*[@id="firstName"]')))
    browser.execute_script("arguments[0].scrollIntoView(true);", first_name_elem)
    # actions.move_to_element(first_name_elem).perform()
    time.sleep(.5)
    first_name_elem.click()
    time.sleep(.5)
    first_name_elem.send_keys('Sidh')
    print('First Name Input Success.')

    # Last Name Elem
    # time.sleep(random.randint(1,5))
    time.sleep(random.uniform(3.5, 5))
    last_name_elem = browser.find_element(By.ID, 'lastName')
    browser.execute_script("arguments[0].scrollIntoView(true);", last_name_elem)
    last_name_elem.click()
    time.sleep(.5)
    last_name_elem.send_keys('Dhi')
    print('Last Name Input Success.')

    # Phone Number Elem
    # time.sleep(random.randint(1,5))
    time.sleep(random.uniform(3.5, 5))
    phone_no_elem = browser.find_element(By.ID, 'phone')
    browser.execute_script("arguments[0].scrollIntoView(true);", phone_no_elem)
    phone_no_elem.click()
    time.sleep(.5)
    random_phone_number = random_phone_no()
    phone_no_elem.send_keys(random_phone_number)
    print('Phone Number Input Success.')

    # Email Address Elem
    # time.sleep(random.randint(1,5))
    time.sleep(random.uniform(3.5, 5))
    email_address_elem = browser.find_element(By.ID, 'email')
    browser.execute_script("arguments[0].scrollIntoView(true);", email_address_elem)
    email_address_elem.click()
    time.sleep(.5)
    random_email_address = random_email_names()
    email_address_elem.send_keys(random_email_address)
    print('Email Address Input Success.')

    # Password Elem
    # time.sleep(random.randint(1,5))
    time.sleep(random.uniform(3.5, 5))
    password_elem = browser.find_element(By.ID, 'sign-up-password')
    browser.execute_script("arguments[0].scrollIntoView(true);", password_elem)
    password_elem.click()
    time.sleep(.5)
        # password_elem.send_keys(str(password_generator()) + Keys.RETURN)
    password_elem.send_keys('qqqqqq1$')
    print('Password Input Success.')

    # Birthday Elem
    # time.sleep(random.randint(1,5))
    time.sleep(random.uniform(3.5, 5))
    birthday_elem = browser.find_element(By.ID, 'birthday')
    browser.execute_script("arguments[0].scrollIntoView(true);", birthday_elem)
    birthday_elem.click()
    time.sleep(.5)
    birthday_date = str(date_in_x_days(3))
    birthday_elem.send_keys(birthday_date)
    print('Birthday Input Success.')

    # Submit New Account After Waiting
    # time.sleep(random.randint(1,5))
    time.sleep(random.uniform(3.5, 5))
    submit_button_elem = wait_period.until(ec.element_to_be_clickable((By.CLASS_NAME, 'iw-sign-up-form-cta')))
    # extra_elem = wait_period.until(ec.invisibility_of_element_located((By.CLASS_NAME, 'pds-snackbar-container')))
    browser.execute_script("arguments[0].scrollIntoView(true);", submit_button_elem)
    time.sleep(.5)
    submit_button_elem.click()
    print('Submit Button Clicked.')

    # Check for Sign-up Success
    time.sleep(random.uniform(3.5, 5))
    is_joined = False
    if str(browser.current_url) == 'https://www.panerabread.com/content/panerabread_com/en-us/home.html':
        is_joined = True
        print('Sign-up Success!')
    else:
        print('FAILURE: Sign-up Failed!')

    if is_joined:
        df = pd.DataFrame({'Email Addresses' : [random_email_address], 
                           'Date Created' : [str(date.today())], 
                           'Birthday Date' : [str(date.today() + timedelta(3))], 
                           'Time of Creation' : [str(datetime.now())[str(datetime.now()).index(' '):str(datetime.now()).index(' ') + 9]],
                           'Phone Number' : str(random_phone_number)})
        try:
            write_to_sheet(r'C:\Users\sidhd\OneDrive\Documents\Python Script Projects\Panera Bread Automation\panera-bread-account-generator-0762cc37b188.json',
                        '16anUsPZsRsHw9OdZPC7UhAqWYTZw2acaFY2csIfIrco',
                        'Account List',
                        df)
        except pg.exceptions.InvalidArgumentValue:
            pass
        print('Account Information Added to Google Spreadsheet.')
    else:
        print('FAILURE: Account Information Not Added!')


    # Finish Execution of Script
    # input("Press Enter to Close")
    time.sleep(random.uniform(3.5, 5))
    browser.quit()
    print('Browser Exited.')
    # if 'ERROR' in str(subprocess.run(['taskkill', '/f', '/im', 'chrome.exe'])):
    #     print('FAILURE: Task not Killed, Chrome Instance not Found.')
    # else:
    #     print('Task Killed.')
    subprocess.run(['taskkill', '/f', '/im', 'chrome.exe'])
    time.sleep(120)
    print('Program Ended.')

# Executes create_account()
create_account()