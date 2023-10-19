from TTS.api import TTS
from playsound import playsound

MODEL_NAME = "tts_models/en/jenny/jenny"
OUTPUT_PATH = "output_tts.wav"
TEXT = "Okay. Let's test the new voice."

TTS(MODEL_NAME).tts_to_file(TEXT, file_path=OUTPUT_PATH)
playsound(OUTPUT_PATH)