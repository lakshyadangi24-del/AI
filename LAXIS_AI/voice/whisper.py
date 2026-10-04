import whisper
import speech_recognition as sr

from core.logger import logger


class WhisperEngine:

    def __init__(self, model_name="base"):
        logger.info("Loading Whisper...")
        self.model = whisper.load_model(model_name)
        logger.info("Whisper Loaded")

    def listen(self):

        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        with open("voice.wav", "wb") as f:
            f.write(audio.get_wav_data())

        result = self.model.transcribe("voice.wav")

        return result["text"]