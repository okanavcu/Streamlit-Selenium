import os

import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-features=VizDisplayCompositor")


def delete_selenium_log():
    if os.path.exists('selenium.log'):
        os.remove('selenium.log')


def show_selenium_log():
    if os.path.exists('selenium.log'):
        with open('selenium.log') as f:
            content = f.read()
            st.code(content)


def run_selenium():
    name = str()
    with webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options) as driver:
        driver.get("https://www.google.com.tr")

        # Arama kutusuna "okan" yaz
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("okan")

        # Enter tuşuna bas
        search_box.submit()

        name = driver.find_element(By.CSS_SELECTOR,'#oFNiHe > div > div > div.eKPi4 > span:nth-child(2) > span.BBwThe').text
        # WebDriver'ı kapat
        driver.quit()
        return name


if __name__ == "__main__":
    delete_selenium_log()
    st.set_page_config(page_title="Selenium Test", page_icon='✅',
        initial_sidebar_state='collapsed')
    st.title('🔨 Selenium Test for Streamlit Sharing')
    st.markdown('''This app is only a very simple test for **Selenium** running on **Streamlit Sharing** runtime.<br>
        The suggestion for this demo app came from a post on the Streamlit Community Forum.<br>
        <https://discuss.streamlit.io/t/issue-with-selenium-on-a-streamlit-app/11563><br>
        This is just a very very simple example and more a proof of concept.
        A link is called and waited for the existence of a specific class and read it.
        If there is no error message, the action was successful.
        Afterwards the log file of chromium is read and displayed.
        ---
        ''', unsafe_allow_html=True)

    st.balloons()
    if st.button('Start Selenium run'):
        st.info('Selenium is running, please wait...')
        result = run_selenium()
        st.info(f'Result -> {result}')
        st.info('Successful finished. Selenium log file is shown below...')
        show_selenium_log()
