import os
from dotenv import load_dotenv

# Gemini API
import google.generativeai as genai

# Load the environment variables
load_dotenv()

# The maximum length of a response
response_min_length = os.getenv('RESPONSE_MIN_LENGTH')

try:
    response_min_length = int(os.getenv('RESPONSE_MIN_LENGTH'))
except (ValueError, TypeError):
    response_min_length = 0
finally:
    response_min_length = max(response_min_length, 50)

# Configure Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Create the text-to-text model
model = genai.GenerativeModel('gemini-pro')


def generate_response(prompt: str, length: int = response_min_length):
    """
    Generate content for the question asked
    """
    # To get the answer in plaint text
    prompt += "\nAnswer in plain text, do not use list"

    # If the length is specified
    if length is not None:
        prompt += f"\n(Answer in {length} words, make finished sentences)"
    else:
        prompt += "\n(Use many words as required)"

    return model.generate_content(prompt, generation_config=genai.types.GenerationConfig(
        # One one candidate
        candidate_count=1,

        temperature=1.0
    )).text


if __name__ == '__main__':
    prompt = "How does influencer marketing impact your awareness and perception of brands?"
    text = generate_response(prompt, 200)
    print(len(text.split(" ")))
    print(text)
