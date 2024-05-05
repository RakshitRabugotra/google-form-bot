"""
Utility to generate random choices
"""
import random
from .gemini import generate_response

# Constants
GENDER_OPTIONS = ['Male', 'Female']


# Utility functions
def random_gender(options: list[str] = GENDER_OPTIONS) -> str:
    """
    Generates random gender
    """
    return random.choice(options)


def random_name(gender: str) -> str:
    """
    Generates a random name
    """
    # Check if the gender is present the gender options, if not throw error
    assert gender in GENDER_OPTIONS
    # Else choose a random


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


def random_text(prompt: str) -> str:
    """
    Generates random text for the given prompt
    """
    return generate_response(prompt)
