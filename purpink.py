from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # prevents opening browser window
options = options
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.purpink.co.ke/collections/her")

product_names = driver.find_elements_by_class_name("product-thumbnail__title")
product_prices = driver.find_elements_by_class_name("money")

filename = "purpink.csv"
headers = ("Brand,Price(Ksh) \n")
f = open(filename, "w")
f.write(headers)

for (product, price) in zip(product_names, product_prices):
    firstPrice = price.text.strip("KSh").split(",")
    finalPrice = "".join(firstPrice)
    #print(product.text + "," + finalPrice)
    f.write(product.text + "," + finalPrice + "\n")
