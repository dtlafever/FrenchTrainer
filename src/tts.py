import edge_tts
from playsound3 import playsound
import asyncio

# More voices can be found by running `edge-tts --list-voices` in the terminal
async def async_speak_text(text: str, lang: str = "en-US"):
    if lang == "en-US":
        voice = "en-US-SteffanNeural"
    elif lang == "fr-FR":
        voice = "fr-FR-VivienneMultilingualNeural"
    tts_engine = edge_tts.Communicate(text, voice)
    await tts_engine.save("edge_output.mp3")
    await asyncio.sleep(.1)
    playsound("edge_output.mp3")
