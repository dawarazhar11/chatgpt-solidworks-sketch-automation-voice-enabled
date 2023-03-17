# SolidWorks Sketch Automation using OpenAI and PySldWrap

This project demonstrates how to use OpenAI's GPT-3 API and PySldWrap to automate sketch creation in SolidWorks. The program listens to user commands through the microphone, generates text prompts using OpenAI, and creates a sketch based on the user's input using PySldWrap.

## Prerequisites
- SolidWorks 2021
- Python 3.8 or above
- OpenAI API Key
- PySldWrap

## Installation
1. Clone this repository to your local machine.
2. Install the required packages using `pip install -r requirements.txt`.
3. Set up an [OpenAI](https://openai.com/) account and get an API key.
4. Update the `config.ini` file with your OpenAI API key.
5. Add the path to your local PySldWrap directory in the `PYTHONPATH` environment variable.

## Usage
1. Open SolidWorks before running the program.
2. Run the program using `python solidworks_sketch.py`.
3. The program will listen to your command through the microphone.
4. Once the program recognizes a valid command, it will generate a text prompt using OpenAI's GPT-3 API.
5. Based on your input, the program will create a sketch using PySldWrap in SolidWorks.
6. Follow the instructions displayed on the console to complete the sketch.
7. Once the sketch is complete, it will be saved to the location specified by the user.

## Supported Commands
- Draw a rectangle
- Draw a circle

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
