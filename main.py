from form_bot.xpath_recorder import XPathRecorder, XPathSet
from form_bot.types.element_type import ElementType
from form_bot.driver import Driver


def record_elements() -> XPathRecorder:
    """
    Records the element for the webpage
    """
    recorder = XPathRecorder("./store/page.json")

    # Required for recording the elements, else defaults to the JSON file
    recorder.start_recording()

    # Record email
    email_element = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input'
    recorder.record_element("Email", email_element, None, 1, ElementType.EMAIL)

    # Record name
    name_element = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    recorder.record_element("Name", name_element, None, 1, ElementType.NAME)

    # Record gender
    gender_male = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'
    gender_female = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span'
    recorder.record_gender_element("Gender", gender_male, gender_female)

    # Age of the responder
    age_element = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'
    recorder.record_element("Age", age_element, None, 1, ElementType.AGE)

    # question 1
    ques_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span'
    ques_last = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span'
    recorder.record_element("What recipes do you know?", ques_first, ques_last, 4, ElementType.CHECKBOX)

    # question 2
    ques_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'
    ques_last = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[2]/div/span'
    recorder.record_element("How responsive are you on a scale of 10", ques_first, ques_last, 5, ElementType.RADIO)

    # Text area 
    text_area = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea'
    recorder.record_element(
        "Should we be able to see information about every citizen in every country?", text_area, None, 1, ElementType.TEXT)

    # Submit button
    recorder.record_submit_element('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    # To prevent from recording any more elements
    recorder.stop_recording()

    return recorder


# The main function
if __name__ == '__main__':

    # Get the records from the recorder
    xpath_records = record_elements().xPaths

    # Create a driver instance
    url: str = "https://docs.google.com/forms/d/e/1FAIpQLSet3sr4fnwEIyRdf-12QXU4DgDfXXIUblz-6_Q0F8tGBoDb3Q/viewform"
    driver = Driver(
        url=url,
        xPaths=xpath_records
    )

    # Check if the driver is good to go
    if not driver.is_good:
        print("The driver is not ready to go... check XPaths")
        exit(-1)

    # Run the driver for specified number of responses
    responses = 5
    driver.run(responses=responses)
    # Exit normally
    exit(0)
