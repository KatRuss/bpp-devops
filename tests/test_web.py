from t_consts import WEB_URL
from selenium import webdriver
from bs4 import BeautifulSoup
from pytest import fixture
import os


@fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@fixture
def soup():
    html_file = open("index.html", "r", encoding="utf-8")
    index = html_file.read()
    s = BeautifulSoup(index, "lxml")

    yield s


def test_app_live(browser, soup):
    """LIVE: Tests that the website is currently live"""
    # Get intended title of webpage
    web_title = soup.title.string

    # If the title of the tested webpage is the same, we can assume the website is live
    browser.get(WEB_URL)
    assert web_title in browser.title
    browser.close()


def test_random_button(browser):
    """LOCAL: Tests that the random generator
    button works and gives a valid result"""
    browser.get(os.path.realpath("index.html"))

    text_box = browser.find_element(value="randomName")
    initial_text = text_box.text

    button = browser.find_element(value="button")
    button.click()

    new_text = text_box.text

    # Test the new world is actually valid
    # and not just a string of random characters
    word_split = new_text.split()
    adjectives = ["Secret", "Mighty", "Brave", "Swift", "Clever", "Clover"]
    animals = ["Squirrel", "Tiger", "Eagle", "Fox", "Bear", "Zebra"]

    assert (
        initial_text != new_text
        and word_split[0] in adjectives
        and word_split[1] in animals
    )
