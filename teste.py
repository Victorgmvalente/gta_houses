from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

url = 'https://www.properly.ca/buy/search/toronto/?bounds=%7B%22sw%22%3A%7B%22lat%22%3A43.61041508001185%2C%22lng%22%3A-79.44768465373454%7D%2C%22ne%22%3A%7B%22lat%22%3A43.760618926197054%2C%22lng%22%3A-79.3137887797111%7D%7D&sorting=prod-global-listings-close-date&showSold=true'
driver.get(url)

button = driver.find_element(by=By.CLASS_NAME, value = 'ToggleMapListButton__Container-sc-4o5aow-0.dqpmfA')
button.click()
#'ListingCard__TextWrapper-sc-13ynupq-5.bkHfVC'

#teste = driver.find_element(by=By.CLASS_NAME, value ='ListingCard__TextWrapper-sc-13ynupq-5.bkHfVC')
teste = driver.find_element(by=By.CLASS_NAME, value ='ListingCard__ListingCardWrapper-sc-13ynupq-4.qEBFc')
#house_txt = teste.text
for propriedae in teste:
    
#house_list = []
#house_list.append(house_txt)

#df = pd.DataFrame(house_list)
#df.to_parquet('teste1.parquet')
#df.to_parquet('teste1.csv')

print(teste.text)



#<span class="ToggleMapListButton__Container-sc-4o5aow-0 dqpmfA">
#<button data-cy="srp-map-list-toggle-button" 
#class="ToggleMapListButton__StyledButton-sc-4o5aow-1 WSTRm">List</button></span>

#<span class="ToggleMapListButton__Container-sc-4o5aow-0 dqpmfA">
#<button data-cy="srp-map-list-toggle-button" 
#class="ToggleMapListButton__StyledButton-sc-4o5aow-1 cMjqjR">Map</button></span>
#//*[@id="__next"]/div/main/div/div/div[2]/div[2]/ul/li[1]/div/div/div/div[2]/p[1]
#//*[@id="__next"]/div/main/div/div/div[2]/div[2]/ul/li[1]/div/div/div/div[2]/div[2]/div/div[1]

#<div class="ListingCard__TextWrapper-sc-13ynupq-5 bkHfVC">
#<div class="ListPrice__ListPriceDetailsContainer-sc-15lf7ey-0 laLJxm">
#<div class="ListPrice__PriceAndListAgoContainer-sc-15lf7ey-1 bQHfeP">
#<div data-testid="list-price" class="ListPrice__ListPriceContainer-sc-15lf7ey-2 eSzqUf text-bold">
##Sold for $XXX,XXX</div></div><div class="ListPrice__ListingBadges-sc-15lf7ey-3 ixBKDZ">
#<div data-cy="listing-card-badge-listed-time"class="ListingBadge__BadgeWrapper-sc-1swqg25-0 jEOSvz">
#<div data-testid="listing-badge" class="ListingBadge__Text-sc-1swqg25-1 cJUqRn">
#Today</div><svg width="18" height="18" viewBox="0 0 18 18" xmlns="http://www.w3.org/2000/svg" 
#class="ListingBadge__StyledIcon-sc-1swqg25-2 dRcSNf" xmlns:xlink="http://www.w3.org/1999/xlink" 
#focusable="false" aria-hidden="true"><path fill="#ffc043"
