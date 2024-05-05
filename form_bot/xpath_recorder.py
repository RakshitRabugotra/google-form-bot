"""
Records xPaths
"""
import json

# Internal Types
from .types.element_type import ElementType

# Internal Utilities
from logger import logger
from .utils import first_different_index

# The file to store the xPaths in the disk
JSON_FILE = "./store/page.json"


class XPathSet:
    """
    Represents a mapping of various attributes related to HTML element
    """

    def __init__(self, name: str, elementType: str, options: list[str] = []):
        self.__name = name
        self.__options = options
        # Check if the type is valid
        try:
            ElementType.assert_valid(elementType)
        except AssertionError as ae:
            logger.error(
                f"Given element-type for: {name} is invalid, got: {elementType} | {ae}")
            elementType = []
        finally:
            self.__type = elementType

    @classmethod
    def from_dict(cls, xPathSet: dict[str, str | list[str]]):
        name: str = xPathSet["name"]
        type: str = xPathSet["type"]
        options: list[str] = xPathSet["options"]
        return cls(name, type, options)

    @property
    def name(self):
        return self.__name

    @property
    def options(self):
        return self.__options

    @property
    def type(self):
        return self.__type

    def add_option(self, xPath: str):
        """
        Adds the option to the option list
        """
        self.__options.append(xPath)

    # Overload the dict method
    def __dict__(self):
        return {
            'name': self.name,
            'type': self.type,
            'options': self.options
        }


class XPathRecorder:
    json_file = JSON_FILE

    def __init__(self, path_to_json: str = None):
        self.__xPaths: list[XPathSet] = self.__load_paths()
        self.recording = False
        self.json_file = JSON_FILE if path_to_json is None else path_to_json
        self.can_record = len(self.__xPaths) <= 0

    @property
    def xPaths(self):
        return self.__xPaths

    def start_recording(self):
        self.recording = True

    def stop_recording(self):
        self.recording = False

    def record_element(self, name: str, firstXPath: str, lastXPath: str, numOptions: int, elementType: str = None):
        """
        Records the element for answer
        """

        # Check if we can record
        if not self.can_record or not self.recording:
            return

        # Get the first different element index
        diff_index = first_different_index(firstXPath, lastXPath)

        # Generate xPaths based on given first and last xPath with the given range
        xPath = XPathSet(name, elementType)

        if (diff_index == -1) or lastXPath is None:
            # The paths are same, so only 1 path exists
            xPath.add_option(firstXPath)
        else:
            # The paths are different, so generate a range of options
            for i in range(1, numOptions + 1):
                xPath.add_option(
                    firstXPath[:diff_index]
                    + str(i)
                    + firstXPath[diff_index + 1:]
                )

        # Record the xPath
        self.xPaths.append(xPath)

        # Write the xPaths to json file
        self.__write_paths()

    def record_submit(self, xPath: str):
        """
        Records the submit button of the form
        """
        self.record_element(name="submit", firstXPath=xPath,
                            lastXPath=None, numOptions=0, elementType=ElementType.SUBMIT)

    # Private functions
    def __load_paths(self):
        """
        Loads the already saved config for the page
        """
        # Try loading from json_file
        data = []
        try:
            with open(self.json_file, mode='r') as page:
                data = json.load(page)
        except FileNotFoundError as error:
            logger.error(msg=error)
            data = []
        except json.decoder.JSONDecodeError as decodeError:
            logger.error(msg=decodeError)
            data = []

        return list(map(lambda xPathSet: XPathSet.from_dict(xPathSet), data))

    def __write_paths(self):
        """
        Writes the saved xPaths for the 
        """
        with open(self.json_file, mode='w') as page:
            json.dump(list(
                map(lambda xPathSet: xPathSet.__dict__(), self.xPaths)
            ), page, indent=2)
