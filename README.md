# SolidWorks Sketch Automation

This project demonstrates how to use the ChatGPT API and SOLIDWORKS API with speech recognition to automate sketch creation in SOLIDWORKS based on user's verbal commands. The project integrates ChatGPT, SOLIDWORKS API, and speech recognition to provide an interactive and efficient approach to creating sketches in SOLIDWORKS.

## Description

The Python script `solidworks_sketch.py` listens to verbal commands, interprets them using the ChatGPT API, and generates corresponding sketches in SOLIDWORKS through the SOLIDWORKS API. Users can create various sketch types and add dimensions based on their spoken input.

## Installation

1. Clone this repository or download the source code.

2. Install the required Python packages:

"pip install -r requirements.txt"

3. Copy the solidworks.py file from the pySW repository into your project folder.

4. Set up your ChatGPT API key in the solidworks_sketch.py script. Replace 'your_api_key' with your actual ChatGPT API key.

## Usage

1. Open a terminal or command prompt, navigate to the project folder, and run the following command:

python solidworks_sketch.py

2. The script will listen for your verbal commands to create the desired sketch in SOLIDWORKS.

3. After creating the sketch, the script will prompt you to provide dimensions verbally.

4. The script will add dimensions to the sketch based on your input.

## Contributing

Feel free to submit issues, feature requests, and pull requests to improve the project.

## License

MIT License
