import openai
from solidworks import SOLIDWORKS
import speech_recognition as sr

# Request the user to input their OpenAI API key
api_key = input("Please enter your OpenAI API key: ")

# Set the API key
openai.api_key = api_key

sw_app = SOLIDWORKS()
sw_app.connect()

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand your command.")
        return None
    except sr.RequestError as e:
        print(f"Error: {e}")
        return None

def create_sketch(sketch_type, *args):
    if sketch_type.lower() == "rectangle":
        instruction = get_chatgpt_response("How do I create a rectangle sketch in SOLIDWORKS using Python API?")
        print("Instruction:", instruction)
        sw_app.create_sketch()
        sw_app.draw_rectangle(*args)
        
    elif sketch_type.lower() == "circle":
        instruction = get_chatgpt_response("How do I create a circle sketch in SOLIDWORKS using Python API?")
        print("Instruction:", instruction)
        sw_app.create_sketch()
        sw_app.draw_circle(*args)
        
    # Add other sketch types here
    else:
        print("Invalid sketch type")

def add_dimensions(dimensions):
    # Add dimensions to the sketch using SOLIDWORKS API based on the provided dimensions
    pass

if __name__ == "__main__":
    while True:
        user_command = recognize_speech()
        if user_command:
            sketch_type = get_chatgpt_response(f"Create {user_command} sketch in SOLIDWORKS")
            print(f"Creating a {sketch_type} sketch...")

            # You can add more conditions here to handle additional sketch types
            if sketch_type.lower() == "rectangle":
                create_sketch("rectangle", 0, 0, 0.1, 0.1)
            elif sketch_type.lower() == "circle":
                create_sketch("circle", 0, 0, 0.05)
            else:
                print("Invalid sketch type")

            print("Sketch created.")
            print("Please provide the dimensions verbally.")
            dimensions_command = recognize_speech()
            if dimensions_command:
                dimensions = get_chatgpt_response(f"Add {dimensions_command
