import asyncio
import os

import edge_tts
from groq import Groq


class VoiceAssistant:
    """
    Voice Assistant

    Features
    --------
    1. Speech-to-Text (Groq Whisper)
    2. Text-to-Speech (Edge-TTS)
    """

    def __init__(self, api_key: str):

        self.client = Groq(api_key=api_key)

    # ======================================================
    # Speech -> Text
    # ======================================================

    def speech_to_text(self, audio_path: str) -> str:

        if not os.path.exists(audio_path):
            raise FileNotFoundError(
                f"Audio file not found: {audio_path}"
            )

        with open(audio_path, "rb") as audio_file:

            transcription = self.client.audio.transcriptions.create(

                file=(
                    os.path.basename(audio_path),
                    audio_file.read(),
                ),

                model="whisper-large-v3-turbo",

                language="en",

                response_format="verbose_json",
            )

        return transcription.text.strip()

    # ======================================================
    # Text -> Speech
    # ======================================================

    async def generate_voice(
        self,
        text: str,
        output_file: str = "response.mp3",
    ) -> str:

        communicate = edge_tts.Communicate(

            text=text,

            voice="en-US-AriaNeural",

            rate="+0%",

            pitch="+0Hz",
        )

        await communicate.save(output_file)

        return output_file

    # ======================================================
    # Public Method
    # ======================================================

    def speak(self, text: str) -> str:

        if not text.strip():
            return ""

        try:

            try:
                loop = asyncio.get_running_loop()

                # Running inside an event loop
                temp_file = "response.mp3"

                loop.create_task(
                    self.generate_voice(
                        text,
                        temp_file
                    )
                )

                return temp_file

            except RuntimeError:

                # Normal execution
                return asyncio.run(
                    self.generate_voice(text)
                )

        except Exception as e:

            print(f"Voice Error: {e}")

            return ""
