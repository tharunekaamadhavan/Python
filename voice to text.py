import speech_recognition as sr

# Record audio
def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recording...")
        audio = recognizer.listen(source)
        print("Recording finished.")
    return audio

# Convert speech to text
def speech_to_text(audio):
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

# Write text to Notepad file
def write_to_notepad(text):
    with open("transcribed_text.txt", "w") as file:
        file.write(text)
    print("Transcribed text saved to 'transcribed_text.txt'")

    # Open the file in read mode
    with open("transcribed_text.txt", 'r') as file:
    # Loop through each line in the file
        for line in file:
        # Print each line
            print(line.strip())


# Main function
def main():
    audio = record_audio()
    text = speech_to_text(audio)
    if text:
        write_to_notepad(text)

if __name__ == "__main__":
    main()
