from t_consts import WEB_URL
from selenium import webdriver
from bs4 import BeautifulSoup
from pytest import fixture


@fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@fixture
def soup():
    html_file = open("index.html", "r", encoding="utf-8")
    index = html_file.read()
    soup = BeautifulSoup(index, "lxml")

    yield soup


def test_app_loads(browser, soup):
    # Get intended title of webpage
    web_title = soup.title.string

    # If the title of the tested webpage is the same, we can assume the website is live
    browser.get(WEB_URL)
    assert web_title in browser.title


def test_random_button(browser, soup):

    text_box = browser.find_element(value="randomName")
    initial_text = text_box.text

    button = browser.find_element(value="button")
    button.click()

    new_text = text_box.text

    assert initial_text != new_text
