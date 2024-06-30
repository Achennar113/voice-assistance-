# Vajra Voice Assistant

## Overview

Vajra is a simple voice assistant that can respond to various voice commands such as playing a song, telling the time, providing information from Wikipedia,
and telling jokes. It features a graphical user interface (GUI) using Tkinter, and incorporates speech recognition, text-to-speech, and multimedia functionality.

## Features

- **Voice Commands**: Triggered by the wake word "Vajra".
  - Play songs from YouTube
  - Tell the current time
  - Provide a summary of a person or topic from Wikipedia
  - Tell jokes
  - **GUI**: A simple graphical interface with a background image.
  - **Multithreading**: Ensures the GUI remains responsive while processing voice commands.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install Dependencies**:
    ```bash
    pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes pillow requests
    ```

3. **Run the Application**:
    ```bash
    python vajra.py
    ```

## Files

- `vajra.py`: The main script for the voice assistant.
- `README.md`: This readme file.

## Usage

1. **Start the Application**:
    - Run the `vajra.py` script.
    - The GUI window will appear with a background image.

2. **Interact with Vajra**:
      - Click anywhere in the window to start the voice recognition.
      - Say "Vajra" followed by your command, such as:
      - "Vajra, play Despacito"
      - "Vajra, what time is it?"
      - "Vajra, tell me about Albert Einstein"
      - "Vajra, tell me a joke"

3. **Commands**:
      - `play <song>`: Plays the specified song on YouTube.
      - `time`: Tells the current time.
      - `tell me about <topic>`: Provides a brief summary of the specified topic from Wikipedia.
      - `joke`: Tells a random joke.

## Customization

- **Background Image**:
  - The background image URL can be modified in the `vajra.py` script:
    ```python
  - image_url = "https://t3.ftcdn.net/jpg/04/91/09/72/360_F_491097264_CGuzXDvKPkKBTxUnX0Jg9k5rbinL3Xhv.jpg"
    ```

## Troubleshooting

- **Microphone Access**: Ensure your microphone is properly set up and accessible by the application.
- **Dependencies**: Make sure all required libraries are installed.
- **Internet Connection**: An active internet connection is required for accessing YouTube, Wikipedia, and for fetching the background image.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [pywhatkit](https://pypi.org/project/pywhatkit/)
- [Wikipedia](https://pypi.org/project/wikipedia/)
- [pyjokes](https://pypi.org/project/pyjokes/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Requests](https://pypi.org/project/requests/)

Feel free to modify and enhance this project to better suit your needs!
