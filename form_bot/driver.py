# Functional Dependencies
from dotenv import load_dotenv
from logger import logger
import time

# Webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# Internal Types
from form_bot.types.element_type import ElementType

# Internal Dependencies
from form_bot.xpath_recorder import XPathRecorder, XPathSet
import form_bot.randomizer as randomizer

# Load the environment variables
load_dotenv()


class Driver:
    min_response_length = 200

    def __init__(self, url: str, xPaths: list[XPathSet]):
        # Initiate the driver
        self.url = url
        self.xPaths = xPaths
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    @property
    def is_good(self):
        """
        Checks if the Driver is ready to go
        """
        return len(self.xPaths) > 0

    def get_element(self, xPath: str):
        """
        Returns the element found by Xpath
        """
        return self.driver.find_element(By.XPATH, xPath)

    def run(self, responses: int):
        """
        Fill responses for the form
        """
        count = 0

        while (count <= responses):
            # Iterate over each xPath and give response for that based on the input
            for xPath in self.xPaths:
                # Get the options for the
                result = self.__get_results(xPath)

                # Result's element will be a string if the xPath is of type 'text'
                if isinstance(result['element'], str) and ElementType.is_text(xPath.type):
                    # Fill the text response
                    self.get_element(result['element']).send_keys(
                        result['payload']
                    )

                # Results will be a radio
                if isinstance(result['element'], str) and ElementType.is_radio(xPath.type):
                    # Tick the radio element
                    self.get_element(result['element']).click()

                # Result's element will be a list if the xPath is of type 'checkbox'
                if isinstance(result['element'], list) and ElementType.is_check(xPath.type):
                    for option in result['element']:
                        self.get_element(option).click()

                # Sleep for a small amount of time
                time.sleep(0.76)
            # end-for

            # Increment response count with each successful response submission
            count += 1
            # Show the progress
            logger.info(
                f"Responses {count}/{responses} | Progress {(100 * (count / responses)):.2f}%")

            # Refresh with a new window
            self.driver.close()
            self.driver = webdriver.Chrome()
            self.driver.get(self.url)
        # end-while

    def submit_form(self, elementXPath: str) -> None:
        """
        Submits the form
        """
        self.driver.find_element(By.XPATH, elementXPath).click()

    def __get_results(self, xPath: XPathSet):
        """
        Chooses a response, Get the options for radio and checkbox,
        Generates response for a question
        """
        result = {
            'element': xPath.options,
            'payload': None
        }
        # Choose a gender for the response
        # gender = randomizer.random_gender()

        # autopep8: off
        match xPath.type:
            # case ElementType.NAME:
                # element, result = (xPath['options'], randomizer.random_name(gender))

            # case ElementType.GENDER:
                # element, result = (xPath['options'], gender)

            case ElementType.RADIO:
                result['element'] = randomizer.random_radio(xPath.options)

            case ElementType.CHECKBOX:
                result['element'] = randomizer.random_checkbox(xPath.options)

            case ElementType.TEXT:
                result['element'] = xPath.options[0]
                result['payload'] = randomizer.random_text(xPath.name)

            case ElementType.SUBMIT:
                logger.info(f"Generating Result for: {xPath.name}...")
                result['element'] = result['element'][0]
                self.submit_form(result['element'])

            case _:
                logger.error("Element type not understood")
        # autopep8: on

        logger.info(f"Make response: {result}")

        # Return the result
        return result
