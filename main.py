from form_bot.xpath_recorder import XPathRecorder, XPathSet
from form_bot.types.element_type import ElementType
from form_bot.driver import Driver


def record_elements() -> XPathRecorder:
    """
    Records the element for the webpage
    """

    # Creates an instance of recorder
    # OPTIONAL MODIFY: You can change this tow whatever you like
    recorder = XPathRecorder("./store/page.json")

    # Required for recording the elements, else defaults to the JSON file
    recorder.start_recording()

    # Record an element
    xpath_first: str = '<xpath_of_first_element>'
    xpath_last: str = '<xpath_of_last_element>'

    # MODIFY: set this to the number of options you have in the form
    num_options: int = 6

    # MODIFY: set this to the type of Element type
    element_type: str = ElementType.RADIO

    # Call the record element function
    recorder.record_element("<name of your choice>", xpath_first,
                            xpath_last, num_options, element_type)

    ...  # More elements to record

    # Submit button
    recorder.record_submit('<xpath_of_submit_button>')

    # To prevent from recording any more elements
    recorder.stop_recording()

    return recorder


# The main function
if __name__ == '__main__':

    # Get the records from the recorder
    xpath_records = record_elements().xPaths

    # Create a driver instance
    url: str = "https://forms.gle/HucQVYPoUvxEHGVr9"  # URL of the google form
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
