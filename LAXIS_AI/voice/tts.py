import asyncio
import edge_tts
import pygame
import os
import tempfile


class TTS:

    def __init__(self):
        pygame.mixer.init()

        # Deep British Male
        self.voice = "en-GB-RyanNeural"

    async def _generate(self, text, filename):

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice
        )

        await communicate.save(filename)

    def speak(self, text):

        filename = tempfile.mktemp(".mp3")

        asyncio.run(self._generate(text, filename))

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

        pygame.mixer.music.unload()

        os.remove(filename)