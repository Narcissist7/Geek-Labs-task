import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def getStocksData(tweets, time_stamps, length):
    i = 0
    indexes = []
    stockTweetsSum = 0
    for tweet, time_stamp in zip(tweets,time_stamps): 
        # Check if the tweet contains a stock symbol
        if '$' in tweet:

            # Check if the time indicates the tweet is recent 
            if 'm' in time_stamp or 's' in time_stamp:
            
                # Remove the time unit and convert to integer for comparison
                time_value = int(time_stamp.rstrip('ms'))
            
                # Check if the tweet is within the last 15 minutes
                if 'm' in time_stamp and time_value <= 15:
                    stockTweetsSum += 1
                    i += 1
                    indexes.append(i)
                # checks if the tweet is within the last 15 minutes    
                elif 's' in time_stamp and time_value <= 900:  # 15 minutes * 60 seconds
                    stockTweetsSum += 1
                    i += 1
                    indexes.append(i)

                

    # Return the filtered lists and count of stock symbol mentioned
    return tweets, time_stamps, stockTweetsSum, i
                
tweets = []
timeInMinutes = []
all_tweets = []
all_times = []
xpath = '//div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div/div/div/article/div/div/div[2]/div[2]/div[2]';
timeXPATH = '//div[2]/div/div[3]/a/time';
length = len(all_tweets)  
indexes = []

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
    'https://twitter.com/TriggerTrades',
    'https://twitter.com/AdamMancini4',
    'https://twitter.com/CordovaTrades',
    'https://twitter.com/Barchart',
    'https://twitter.com/RoyLMattox'
] 

for url in urls:
    driver.get(url)
    time.sleep(5)
    for i in range(2):
        driver.execute_script('window.scrollBy(0,1000);')
        time.sleep(1)

    tweets = driver.find_elements(By.XPATH, xpath)
    for tweet in tweets:
        try:
            time_elements = tweet.find_elements(By.XPATH, timeXPATH)
            if time_elements:
                all_tweets.append(tweet.text)
                all_times.append(time_elements[0].text)

        except:
            # If there is an error finding the time element, you can handle it here
            print("Time element not found for a tweet")

# Call the function to filter stock-related tweets and get relevant data
# Arguments:
#   all_tweets: List containing all collected tweets
#   all_times: List containing the corresponding timestamps for each tweet
#   length: Length of the collected tweets

all_tweets,all_times, s, indexes = getStocksData(all_tweets, all_times, length)           

# Returns:
#   all_tweets: List containing filtered tweets
#   all_times: List containing timestamps corresponding to filtered tweets
#   s: Count of stock-related tweets
#   indexes: Indexes of filtered tweets in the original lists

#Displaying to user all the Stock mentions that was collected in 15 minutes
if indexes:
    print(f"Number of Stocks Mentioned in the last 15 Minutes: {len(indexes)} ")
    print("No Stocks News in the last 15 Minutes: ")
    for index in indexes :
        print(f"Tweet: {all_tweets[indexes[index]]}")
        print(f"Time: {all_times[indexes[index]]}")
else:
    print("No matching tweets found")
    
driver.quit()
