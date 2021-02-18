from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
def scrip(): 

	browser = webdriver.Firefox()

	browser.get("https://v2.waitwhile.com/welcome/mmdgraham")

	time.sleep(2)
	browser.find_element_by_xpath('/html/body/app-root/welcome/div/div/section/div[2]/div[3]/div/button').click()
	time.sleep(2)
	browser.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-service/div/div/div/section/div[2]/div/button[2]/div/div/div[2]/span/span').click()
	time.sleep(2)
	browser.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-service/div/div/div/section/div[2]/button').click()
	time.sleep(2)
	browser.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-resource/div/div/div/div/div[2]/button[1]/div').click()
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="name02"]').send_keys("Anna")
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="name03"]').send_keys("Molloy")
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="phone01"]').send_keys("9173738847")
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="AUwcZ8ZlfWBDC9pxyZSy"]').send_keys("19")
	time.sleep(2)
	browser.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-confirm-page/div/div/div/div[2]/form/div[1]/dynamic-form/form-multi-select/div/div[1]/ww-multiselect/ng-select/div/div/div[2]/input').send_keys('blue')
	time.sleep(2)
	browser.find_element_by_xpath('/html/body/app-root/public-landing-page/main/div/div/public-confirm-page/div/div/div/div[2]/form/div[1]/dynamic-form/form-multi-select/div/div[1]/ww-multiselect/ng-select/ng-dropdown-panel/div[2]').click()
	time.sleep(2)
#browser.find_element_by_xpath('//*[@id="public-waitlist-confirm"]/div/div/div[2]/form/div[1]/button').click()

scrip()

# browser.quit()class="ng-dropdown-panel-items scroll-host"

# #browser.find_element_by_xpath("//*[@id="a9ae4aa4ff37-2"]")

# keys = {
#         # need the url before hand
#         "start_url": "https://v2.waitwhile.com/welcome/mmdgraham",
#         # must be capital letters
#         "name": "Matthew Lowery",
#         "tel": 4439870848,
#         # address can be 'jigged' to use for multiple orders; i.e. use rd instead of road st instead of st
#         "address": "1 heaven way",
#         # or adding/withdrawing an apt number when you live in a house

# }



