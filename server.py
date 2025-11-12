from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector  # Import your function

app = Flask("Emotion Detection")

@app.route("/emotionDetector", methods=["POST"])
def emotionDetector():
    data = request.get_json()
    text_to_analyze = data.get("text", "")

    result = emotion_detector(text_to_analyze)

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({
        "emotion_scores": result,
        "response_text": response_text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)