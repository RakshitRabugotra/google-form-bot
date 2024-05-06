# Google Form Bot

<p align="justify">This bot can fill out your google form responses (TEXT, RADIO, CHECKBOX) and generates text using Gemini behind the hood</p>

### Sample to try: [Google Form](https://forms.gle/HucQVYPoUvxEHGVr9)

## Required Settings for the form

- The bot uses `Chrome` as it's browser. Make sure it's installed properly.

- The bot is able to fill out:

    <ul>
    <li>Names</li>
    <li>Gender choices</li>
    <li>Radio inputs</li>
    <li>Checkbox inputs</li>
    <li>Text inputs (Short or Long paragraph)</li>
    </ul>

- The only required setting for the form is to disable the `requires sign-in`

  ![Required Form Setting](docs/required-form-setting.png)

## Setting up environment

<p>If you don't have `Python` installed in your system, download it from <a href='https://python.org/downloads'>python.org downloads</a></p>

Run the following script in the terminal in project folder

```bash
$ git clone https://github.com/RakshitRabugotra/google-form-bot.git
```

Change into the cloned repo folder

```bash
$ cd google-form-bot
```

Make a python virtual environment

```bash
$ python -m pip venv venv
```

Install all the dependencies

```bash
$ python -m pip install -r requirements.txt
```

## Setting up Gemini API for Text inputs

1. Get your `Gemini` API key from: [Google AI Studio]("https://aistudio.google.com/app/apikey)

   ![GEMINI_API_KEY_CREATE](docs/image.png)

2. Copy the `API Key` and paste it in the `.env.example` file as `GEMINI_API_KEY`:

   ```ini
   LOG_FILENAME=app.log
   LOG_ENCODING=utf-8
   GEMINI_API_KEY=<YOUR_GEMINI_KEY>
   RESPONSE_MIN_LENGTH=<NUMBER_OF_WORDS>
   ```

3. Rename `.env.example` to `.env`

## Getting the XPath of the element:

The XPath of element is used to uniquely identify it in the DOM (Document Object Model)

1. Choose a section:

   ![Chosen Section](docs/chosen-section.png)
   Press `F12` to open 'Developer's Console' and click on element selector icon in the top left of the developer's menu

2. Selecting an option and copying `XPath`:

   ![Chosen Element](docs/chosen-element.png)
   Click on the text part of the element to select it in the DOM

   ![alt text](docs/dom-selection.png)
   After selecting in the dom click on the element as shown in right side of the window.

   ![Copy XPath](docs/copy-xpath.png)
   Right click it and goto `Copy`, then `Xpath` to copy the XPath of the element. Use it as the `xpath_first` in the next example

3. Do the same for the last element and use it as the `xpath_last` in the next example

## Recording a `TEXT INPUT` element

The `name` of the element should be the actual question asked in the form (blue arrow).

The `xpath_first` should be this text input's XPath. (purple-arrow) <br/>Whereas `xpath_last` should be set to `None`.

![alt text](docs/text-input.png)

## Running the main file

- Modify the function snippet `record_elements` in `main.py` and add the `XPath` of the HTML element to record:

  ![record_elements function](docs/record-elements.png)

- Run the `main.py` by doing:
  ```bash
  $ python main.py
  ```
