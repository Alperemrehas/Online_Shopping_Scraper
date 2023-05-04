# Online_Shopping_Scraper

# Takealot Scraper

A Python program that scrapes Takealot's website for product data based on keywords entered by the user. The program uses the PyQt5 framework for creating the user interface and the Selenium webdriver to interact with the website and extract data.

## Installation

1. Clone or download the repository.
2. Install the required packages using the following command:

```python
pip install PyQt5 selenium
```

3. Download the Chrome webdriver executable from the [official website](https://sites.google.com/a/chromium.org/chromedriver/downloads) and save it in the same directory as the code file.

## Usage

Run the program using the following command:

```python
python takealot_scraper.py
```

The program will open a PyQt5 window that prompts the user to enter a keyword for the search. After entering the keyword, click on the "Search" button to initiate the web scraping process.

The program will launch a headless instance of Google Chrome using Selenium webdriver and navigate to Takealot's website. It will enter the keyword in the search box and extract the product data from the first page of search results. If more than one page of search results is available, the program will navigate to the next page and extract the data until there are no more pages left.

The scraped data will be displayed in the terminal window.

## Customization

The following variables can be customized in the code to modify the behavior of the program:

- `BACKGROUND_COLOR`: The background color of the PyQt5 window.
- `ENTRY_COLOR`: The background color of the search box.
- `BUTTON_COLOR`: The background color of the "Search" button.
- `webdriver_path`: The path to the Chrome webdriver executable. Update this variable with the correct path on your system.
