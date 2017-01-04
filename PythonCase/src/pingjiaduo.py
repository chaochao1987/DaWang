from selenium import webdriver
from time import sleep






#feature 03: login
driver = webdriver.Chrome()
driver.get("https://www.pingjiaduo.com/site/login")
driver.maximize_window()
driver.find_element_by_xpath("//input[@name='email']").send_keys("lvmintest2@163.com")
driver.find_element_by_xpath("//input[@name='password']").send_keys("123456A")
sleep(5)
driver.find_element_by_xpath("//button[@id='loginSubmit']").click()
sleep(2)
#feature 01: add new products 

driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
sleep(2)
driver.find_element_by_xpath("//textarea[@name='url']").send_keys("https://www.amazon.com/gp/product/0399226907/ref=s9_acsd_top_hd_bw_b2oXDC7_c_x_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=GWKWTQMCXNDFN5VG02YE&pf_rd_t=101&pf_rd_p=1aec0c37-151a-5f6b-be6f-4c0daf4f2810&pf_rd_i=2578998011\nhttps://www.amazon.com/gp/product/0694003611/ref=s9_acsd_simh_hd_bw_b2oXDC7_c_x_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=YGXV11W6T6VFYTMZ83DY&pf_rd_t=101&pf_rd_p=1aec0c37-151a-5f6b-be6f-4c0daf4f2810&pf_rd_i=2578998011")
driver.find_element_by_xpath("//button[@request='close']").click()
"""
#feature 02: personal center
driver.find_element_by_xpath("//form[@id='logOutForm']/a").click()
driver.find_element_by_xpath("//ul[@class='dropdown-menu dropdown-menu-usermenu pull-right']/li[1]").click()

