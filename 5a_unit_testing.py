def test_emotion_predictor():
    result = emotion_predictor("I am happy")
    assert "happy" in result["emotions"]