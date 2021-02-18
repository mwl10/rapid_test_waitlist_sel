from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from config import keys 

def scrip(k, browser): 
	browser.implicitly_wait(10000)

	browser.get("https://www.techbeamers.com/selenium-webdriver-waits-python/")

	time.sleep(2)
	browser.find_element_by_xpath('/html/body/app-root/welcome/div/div/section/div[2]/div[3]/div/button').click()
	time.sleep(2)
	browser.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-service/div/div/div/section/div[2]/div/button[2]/div/div/div[2]/span/span').click()
	time.sleep(2)
	browser.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-service/div/div/div/section/div[2]/button').click()
	time.sleep(2)
	browser.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-resource/div/div/div/div/div[2]/button[1]/div').click()
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="name02"]').send_keys(k['f_name'])
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="name03"]').send_keys(k['l_name'])
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="phone01"]').send_keys(k['tel'])
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="AUwcZ8ZlfWBDC9pxyZSy"]').send_keys(k['age'])
	time.sleep(2)
	browser.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-confirm-page/div/div/div/div[2]/form/div[1]/dynamic-form/form-multi-select/div/div[1]/ww-multiselect/ng-select/div/div/div[2]/input').send_keys(k['insurance_keyword'])
	time.sleep(2)
	browser.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-confirm-page/div/div/div/div[2]/form/div[1]/dynamic-form/form-multi-select/div/div[1]/ww-multiselect/ng-select/ng-dropdown-panel/div[2]').click()
	time.sleep(2)
	browser.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-confirm-page/div/div/div/div[2]/form/div[1]/button').click()

if __name__ == "__main__":
	browser = webdriver.Firefox()
	scrip(keys, browser)





