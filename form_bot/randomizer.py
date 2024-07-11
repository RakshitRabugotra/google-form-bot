"""
Utility to generate random choices
"""
from typing import Literal
import random
import csv
from .gemini import generate_response

# Utility to load different names from the csv file
def load_names(file: str = 'names.csv') -> dict:
    """
    Loads the different names from the csv file
    """
    names = []
    with open(file, mode='r+', encoding='utf-8') as rFile:
        reader = csv.DictReader(rFile)
        names = [item for item in reader]
    
    return names


"""
CONSTANTS
"""
GENDER_OPTIONS = ['male', 'female']
AGE_RANGE = range(18, 30)
EMAIL_SEPARATORS = ['.', 'x', '0']
EMAIL_DOMAINS = ['gmail.com', 'outlook.com', 'yahoo.com']
NAMES = load_names()

# Utility functions
def random_gender(options: list[str] = GENDER_OPTIONS) -> str:
    """
    Generates random gender
    """
    return random.choice(options)


def random_person(gender: str) -> str:
    """
    Generates a random name, gender, age for a given gender
    """
    # Check if the gender is present the gender options, if not throw error
    assert gender in GENDER_OPTIONS
    # Else choose a random person
    person_name = None

    # The range for male names ends at this
    male_range_end = int(len(NAMES) / 2)
    # The range for female names starts with this
    female_range_start = male_range_end + 1

    match gender:
        case 'male':
            person_name: str = random.choice(NAMES[:male_range_end])['name']
        case 'female':
            person_name: str = random.choice(NAMES[female_range_start:])['name']
        case _:
            raise Exception("Generating person for unknown gender")
    return {
        'name': person_name,
        'gender': gender,
        'age': random.choice(AGE_RANGE),
        'email': person_name.replace(" ", random.choice(EMAIL_SEPARATORS)).lower() + '@' + random.choice(EMAIL_DOMAINS) 
    }

def random_radio(radio_options: list[str]) -> str:
    """
    Returns a random option from the given list of options
    """
    return random.choice(radio_options)


def random_checkbox(checkbox_options: list[str], i_min: int = 1, i_max: int = None) -> list[str]:
    """
    Returns a subset of the options given
    """
    # If the maximum number of choices isn't defined, then make it the maximum length
    if i_max is None:
        i_max = len(checkbox_options)

    # Copy the options array
    choices = checkbox_options[:]

    # Generate a random number which gives the number of elements to be chosen
    count_elements = random.randint(i_min, i_max)

    options = []
    while count_elements != 0:
        # Choose a random item from the sequence
        chosen_element = random.choice(choices)
        # Append that item to the options
        options.append(
            chosen_element
        )
        # Remove from the checkbox_options
        choices.remove(chosen_element)
        # Decrease the counter
        count_elements -= 1

    # Return the chosen options
    return options


def generate_text(prompt: str) -> str:
    """
    Generates random text for the given prompt
    """
    return generate_response(prompt)


if __name__ == '__main__':
    print("names: ", NAMES)