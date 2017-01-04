#coding=UTF-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time



driver = webdriver.Chrome()

driver.implicitly_wait(30)

driver.get("http://www.extremerebate.com/")

search_windows = driver.current_window_handle

driver.maximize_window()

driver.implicitly_wait(30)

driver.find_element_by_xpath("//a[@class='signInOrUp']").click()

driver.implicitly_wait(30)
    
driver.find_element_by_xpath("//div[div[span[text()='Remember me']]]/div/div[@class='signItem']/input[@name='email']").send_keys("lvmintest2@163.com")

driver.implicitly_wait(30)

driver.find_element_by_xpath("//div[div[span[text()='Remember me']]]/div/div[@class='signItem']/input[@name='password']").send_keys('123456A')

driver.implicitly_wait(30)
    
driver.find_element_by_xpath("//button[text()='LOGIN']").click()

driver.implicitly_wait(30)

driver.find_element_by_xpath("//input[@placeholder='Search products by name' and @name = 'titleContent']").send_keys("test\n")

title = driver.find_element_by_xpath("//a[@href='http://www.extremerebate.com/test-1483427982-1000-pn.html']")

ActionChains(driver).context_click(title).perform()

driver.find_element_by_xpath("//a[@href='#!/?id=5861d0e7b88d2a0a0c8b4567']").click()

driver.find_element_by_xpath("//input[@type='checkbox']").click()

driver.find_element_by_xpath("//input[@type='checkbox']").click()

driver.find_element_by_xpath("//button[@id='request']").click()

driver.find_element_by_xpath("//a[text()='MY REQUEST']").click()

driver.get("https://www.pingjiaduo.com/site/login")

driver.maximize_window()

driver.find_element_by_xpath("//input[@name='email']").send_keys("lvmintest2@163.com")

driver.find_element_by_xpath("//input[@name='password']").send_keys("123456A")

driver.implicitly_wait(30)

driver.find_element_by_xpath("//button[@id='loginSubmit']").click()

driver.implicitly_wait(30)
#feature 01: add new products 

#driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()

#driver.implicitly_wait(30)
"""
driver.find_element_by_xpath("//textarea[@name='url']").send_keys("https://www.amazon.com/gp/product/0399226907/ref=s9_acsd_top_hd_bw_b2oXDC7_c_x_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=GWKWTQMCXNDFN5VG02YE&pf_rd_t=101&pf_rd_p=1aec0c37-151a-5f6b-be6f-4c0daf4f2810&pf_rd_i=2578998011\nhttps://www.amazon.com/gp/product/0694003611/ref=s9_acsd_simh_hd_bw_b2oXDC7_c_x_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=YGXV11W6T6VFYTMZ83DY&pf_rd_t=101&pf_rd_p=1aec0c37-151a-5f6b-be6f-4c0daf4f2810&pf_rd_i=2578998011")
driver.find_element_by_xpath("//button[@request='close']").click()

#feature 02: personal center
driver.find_element_by_xpath("//form[@id='logOutForm']/a").click()
driver.find_element_by_xpath("//ul[@class='dropdown-menu dropdown-menu-usermenu pull-right']/li[1]").click()
"""
driver.find_element_by_xpath("//ul[@class='sub-menu-list']/li[2]").click()

driver.find_element_by_xpath("//div[label[text()='״̬']]/ul[@class='col-lg-10 col-md-10 item-list']/li[2]").click()













