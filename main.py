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

    # Record age
    age_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'
    age_last = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[6]/label/div/div[2]/div/span'
    recorder.record_element("Age", age_first, age_last, 6, ElementType.RADIO)

    # Record gender
    gender_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'
    gender_last = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span'
    recorder.record_element("Gender", gender_first,
                            gender_last, 2, ElementType.RADIO)

    # question 1
    ques_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'
    ques_last = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span'
    recorder.record_element("Social Media Platforms",
                            ques_first, ques_last, 2, ElementType.RADIO)

    # question 2
    ques_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'
    ques_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span'
    recorder.record_element("Sponsored/Branded", ques_first,
                            ques_last, 3, ElementType.RADIO)

    # question 3
    ques_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span'
    ques_last = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[5]/label/div/div[2]/div/span'
    recorder.record_element("Influencer content do you find engaging",
                            ques_first, ques_last, 5, ElementType.CHECKBOX)

    # question 4
    ques_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span'
    ques_last = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[6]/label/div/div[2]/div/span'
    recorder.record_element("After seeing engaging influence content",
                            ques_first, ques_last, 6, ElementType.CHECKBOX)

    # question 5
    ques_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span'
    ques_last = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[5]/label/div/div[2]/div/span'
    recorder.record_element("influencing your engagement with influence content",
                            ques_first, ques_last, 5, ElementType.CHECKBOX)

    # question 6
    ques_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span'
    ques_last = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div[6]/label/div/div[2]/div/span'
    recorder.record_element("engage with an influencer",
                            ques_first, ques_last, 6, ElementType.CHECKBOX)

    # question 7
    ques_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'
    ques_last = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[2]/div/span'
    recorder.record_element("influencer-brand fit impact your likelihood to engage with sponsored content",
                            ques_first, ques_last, 6, ElementType.CHECKBOX)

    # question 8
    ques_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'
    ques_last = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span'
    recorder.record_element("disclosure and transparency in influencer marketing",
                            ques_first, ques_last, 3, ElementType.RADIO)

    # question 9
    ques_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'
    ques_last = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span'
    recorder.record_element("product/service based on an influencer's recommendation",
                            ques_first, ques_last, 3, ElementType.RADIO)

    # question 10
    ques_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'
    ques_last = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span'
    recorder.record_element("your overall purchase decision process",
                            ques_first, ques_last, 4, ElementType.RADIO)

    # question 11
    ques_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'
    ques_last = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span'
    recorder.record_element("other marketing channels (e.g. TV ads, social media ads) in influencing your purchase decisions",
                            ques_first, ques_last, 3, ElementType.RADIO)

    # question 12
    ques_first = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'
    ques_last = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span'
    recorder.record_element("new brands or products through influencer marketing",
                            ques_first, ques_last, 4, ElementType.RADIO)

    # Text area 1
    text_area = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div[1]/div[2]/textarea'
    recorder.record_element(
        "How does influencer marketing impact your awareness and perception of brands?", text_area, None, 1, ElementType.TEXT)

    # Text area 2
    text_area = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/div[1]/div[2]/textarea'
    recorder.record_element(
        "What do you like or dislike about current influencer marketing practices?", text_area, None, 1, ElementType.TEXT)

    # Text area 3
    text_area = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div[1]/div[2]/textarea'
    recorder.record_element(
        "How can brands and influencers improve their strategies to foster better engagement?", text_area, None, 1, ElementType.TEXT)

    # Submit button
    recorder.record_submit(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    # To prevent from recording any more elements
    recorder.stop_recording()

    return recorder


# The main function
if __name__ == '__main__':

    # Get the records from the recorder
    xpath_records = record_elements().xPaths

    # Create a driver instance
    url: str = "https://docs.google.com/forms/d/e/1FAIpQLScpX3l6RcKvMtmq8fETrA7s6-6ONB7ijUZoCKjrQWGlz3xNZA/viewform"
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
