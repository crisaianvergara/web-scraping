from selenium import webdriver
from bs4 import BeautifulSoup


chrome_driver_path = "put your web driver path here"

driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("website to test")
page_source = driver.page_source

soup = BeautifulSoup(page_source, "html.parser")

# Save the HTML content to a file
with open("index.html", "w", encoding="utf-8") as file:
    file.write(str(soup.prettify()))
