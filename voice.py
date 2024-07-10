import speech_recognition as sr
import pyttsx3
import openai


recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Set OpenAI API key
openai.api_key = 'secret code '

def listen_to_voice():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"Recognized Text: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Request error from Google Speech Recognition service.")
        return None

def speak_text(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    while True:
        print("Please speak your query:")
        user_input = listen_to_voice()
        if user_input:
            print(f"You said: {user_input}")
            openai_response = get_openai_response(user_input)
            print(f"OpenAI Response: {openai_response}")
            speak_text(openai_response)

if __name__ == "__main__":
    main()


