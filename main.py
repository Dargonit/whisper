import whisper

#Several flavors of Whisper are available: tiny, base, small, medium, and large
model = whisper.load_model("medium")
result = model.transcribe("./files/Conference.wav")
print(result["text"])