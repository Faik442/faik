import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


with open('quotes.csv', 'w') as f:
    f.write("Quotes, Author, Tag \n")

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
driver_path = '/home/faik/Selenium Chrome Driver/chromedriver'
driver = webdriver.Chrome(driver_path, chrome_options=opts)

max_page_num = 10
for i in range(1, max_page_num + 1):
    url = "http://quotes.toscrape.com/page/" + str(i) + "/"

    driver.get(url)

    quote = driver.find_elements_by_css_selector('.text')
    author = driver.find_elements_by_css_selector('.author')
    tag = driver.find_elements_by_css_selector('.tag')

    num_qoutes = len(quote)
    with open('quotes.csv', 'a') as f:
        for i in range(num_qoutes):
            f.write(quote[i].text + ", " + author[i].text + ", " + tag[i].text + "\n")

driver.close()
