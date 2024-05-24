import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')

Service = Service(executable_path=CM().install())
driver = webdriver.Chrome(service=Service)
driver.maximize_window()
urls = [
    'https://twitter.com/Mr_Derivatives',
    'https://twitter.com/warrior_0719',
    'https://twitter.com/ChartingProdigy',
    'https://twitter.com/allstarcharts',
    'https://twitter.com/yuriymatso',
    'https://twitter.com/AdamMancini4',
    'https://twitter.com/CordovaTrades',
    'https://twitter.com/Barchart',
    'https://twitter.com/RoyLMattox' 
] 
tweets = []
ticker = r'\$\w+'
xpath = '//div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div/div/div/article/div/div/div[2]/div[2]/div[2]';

for url in urls:
    driver.get(url)
    time.sleep(5)
    for i in range(5):
        driver.execute_script('window.scrollBy(0,2000);')
        time.sleep(0.5)
        tweets += [tweet for tweet in driver.find_elements(By.XPATH, xpath) if ticker in tweet.text]

driver.quit()

print('Tweets Containig $ ' + str(len(tweets)))
