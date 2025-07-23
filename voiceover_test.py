from gtts import gTTS

segments = {
    "part1_intro.mp3": "There are two special cases for posits.",
    "part2_zero_case.mp3": "Only zeros equal zero.",
    "part3_inf_case.mp3": "A single one following only zeros equals plus or minus infinity.",
}

for filename, text in segments.items():
    tts = gTTS(text)
    tts.save(filename)
    print(f"Saved {filename}")

