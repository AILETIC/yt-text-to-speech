from gtts import gTTS
from playsound import playsound

TEXT = "This is an Audio example for a AI voice that is not that good."
OUTPUT_PATH = "output_tts.wav"
tts = gTTS(TEXT, lang="en", slow=False)

tts.save(OUTPUT_PATH)
playsound(OUTPUT_PATH)