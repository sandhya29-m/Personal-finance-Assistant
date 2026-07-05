import asyncio
import edge_tts
from groq import Groq


class VoiceAssistant:

    def __init__(self, api_key):

        self.client = Groq(
            api_key=api_key
        )

    # -------------------------------------
    # Speech -> Text
    # -------------------------------------

    def speech_to_text(self, audio_path):

        with open(audio_path, "rb") as audio_file:

            transcription = self.client.audio.transcriptions.create(

                file=(
                    audio_path,
                    audio_file.read()
                ),

                model="whisper-large-v3-turbo",

                response_format="verbose_json",

                language="en"

            )

        return transcription.text

    # -------------------------------------
    # Text -> Speech
    # -------------------------------------

    async def generate_voice(
        self,
        text,
        output_file="response.mp3"
    ):

        communicate = edge_tts.Communicate(

            text=text,

            voice="en-US-AriaNeural"

        )

        await communicate.save(output_file)

        return output_file

    # -------------------------------------

    def speak(self, text):

        return asyncio.run(

            self.generate_voice(text)

        )