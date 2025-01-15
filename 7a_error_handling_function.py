def emotion_predictor(text):
    if not text:
        return {"error": "No input provided", "status": 400}
    emotions = {"happy": 0.8, "sad": 0.1, "angry": 0.1}
    return {"text": text, "emotions": emotions}