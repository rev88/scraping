# from bs4 import BeautifulSoup
# import requests
# source = requests.get("https://www.dice.com/").text
# soup = BeautifulSoup(source, 'html.parser')
# print(soup.prettify())


import datetime
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import logging

from selenium.webdriver.support.wait import WebDriverWait


class Dice:
    try:
        dice_job_email = []
        dice_job_phoneNo = []
        driver = None
        start_time = datetime.now()
        url = ""
        wait = ''
        link_count = 0
        job_count = []
        job_details = {'Job Category': '', 'Date&Time': '', 'Searched Job Title': '', 'Searched Job Location': '',
                   'Job Portal': 'Monster', 'Job Date Posted': '', 'Job Title': '',
                   'Job Company Name': '', 'Job Location': '', 'Job Phone No': '', 'Job Email': '', 'Job Link': '',
                   'Job Description': ''}

        def __init__(self, driver, url):
            try:
                print(self.start_time)
                self.driver = driver
                self.url = url
                self.wait = WebDriverWait(self.driver, 30)
                logging.basicConfig(filemode='a', format='%(name)s - %(levelname)s - %(message)s',
                                    level=logging.INFO)

                logging.info("######################################################################### \n"
                             "                                                                          \n"
                             "===========================Dice Job Search=============================\n"
                             "                                                                          \n"
                             "##########################################################################")
                logging.info(url)
            except Exception as e:
                print("Unknown Exception in Dice class __init__ ", e)
                logging.exception("Unknown Exception in Dice class __init__ ")
                logging.exception(e)

        # search jobs
        def dice_search_jobs(self, jp_common, job_title, job_location):
            try:
                logging.info("In dice_search_jobs")
                print("In dice_search_jobs")

                # Finding Job Title Textbox element and sending text.
                job_title_web_element = jp_common.find_web_element("//*[@id='keywords2']", "Job Title Textbox",
                                                                   "one", self.wait)
                jp_common.web_element_action(job_title_web_element, "send_keys", job_title, "Job Title Textbox")

                # Finding Job Location Textbox element and sending text.
                job_location_web_element = jp_common.find_web_element("//*[@id='location']", "Job Location Textbox",
                                                                      "one", self.wait)
                jp_common.web_element_action(job_location_web_element, "send_keys", job_location,
                                             "Job Location Textbox")

                # Finding Search Button element and clicking it.
                search_web_element = jp_common.find_web_element("//*[@id='doQuickSearch']", "Search Button", "one",
                                                                self.wait)
                jp_common.web_element_action(search_web_element, "click", "", "Search Button")

            except Exception as e:
                print("Unexpected error in dice_search_jobs", e)
                logging.exception("Unexpected exception in dice_search_jobs")
                logging.exception(e)
                self.driver.get_screenshot_as_file("Screenshots\dice_search_jobs_exception.png")

