from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.common.exceptions import ElementNotVisibleException, TimeoutException, NoSuchElementException
import sys

# Set the background color, entry color, and button color
BACKGROUND_COLOR = "gray"
ENTRY_COLOR = "white"
BUTTON_COLOR = "blue"

webdriver_path = "./chromedriver"  # Update with the correct path to chromedriver executable
options = Options()

def searchWebsite():
    search_entry = ''
    item_name = []
    item_price = []
    item_brand = []
    item_rating = []
    formatted_price = []

    # Grabs the text entered into PyQt5, adds headless arguments to Chrome's webdriver
    search_entry = entry1.text()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    # Update the webdriver path with executable path and options
    driver = Chrome(executable_path=webdriver_path, options=options)    

    # Opens Takealot, searches the keywords and creates a list of items on the first results page
    driver.get('https://www.takealot.com/')
    sleep(8)
    try:
        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'search-field')))
        elem.send_keys(search_entry)
        elem.send_keys(Keys.RETURN)
        sleep(7)
    except TimeoutException:
        print("TimeoutException occurred. Please try again.")
        driver.close()
        app.quit()
        return

    # Check if the webpage has loaded successfully and contains data
    if "No results found" in driver.page_source:
        print("No results found. Please try different keywords.")
        driver.close()
        app.quit()
        return

    # Scrape data from multiple pages of search results
    page = 1
    while True:
        try:
            search_by_item = driver.find_elements(By.CLASS_NAME, 'listings-container.listings-container-module_listings-container_AC4LI')
            print("Len of elements: ",len(search_by_item))
            # Gets the item name and price for each item on the current results page
            for item in search_by_item:
                try:
                    name = item.find_element(By.CLASS_NAME, 'product-title').text
                    brand = item.find_element(By.CLASS_NAME, 'product-card-module_brand-wrapper_Kv3Cy').text
                    price = item.find_element(By.CLASS_NAME, 'currency.plus.currency-module_currency_29IIm').text
                    rating = item.find_element(By.CSS_SELECTOR, 'div.rating i.full.rating-module_full_2aryC').text

                    item_name.append(name)
                    item_brand.append(brand)
                    item_price.append(price)                    
                    item_rating.append(rating)
                    print("Name:", name)
                    print("Brand",brand)
                    print("Price:", price)
                    print("Rating:", rating)

                except ElementNotVisibleException:
                    pass

            # Goes to the next page if available
            try:
                next_page = driver.find_element(By.XPATH, "//a[@class='next']")
                next_page.click()
                sleep(5)
                page += 1
            except NoSuchElementException:
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            driver.close()
            app.quit()
            return
        
    # Display or print the scraped data
    print("Item Names:")
    print(item_name)
    print("Item Prices:")
    print(item_price)
    
    driver.close()
    app.quit()


# Create the PyQt5 UI
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Takealot Scraper")
window.setStyleSheet(f"background-color: {BACKGROUND_COLOR};")

layout = QVBoxLayout()

entry1 = QLineEdit()
entry1.setStyleSheet(f"background-color: {ENTRY_COLOR};")
layout.addWidget(entry1)

button1 = QPushButton("Search")
button1.setStyleSheet(f"background-color: {BUTTON_COLOR};")
button1.clicked.connect(searchWebsite)
layout.addWidget(button1)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
