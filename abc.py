from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\Users\daidale\Downloads\chromedriverfile\chromedriver.exe")
driver.get("http:www.google.com")
driver.close()
print("Execution is done")
