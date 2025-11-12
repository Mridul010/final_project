from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST", "GET"])
def emotionDetector():
    if request.method == "POST":
        data = request.get_json()
        text_to_analyze = data.get("text", "") if data else ""
    else:  # GET request
        text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)
    if result.get("dominant_emotion") is None:
        response = ("Invalid text! Please try again!")
        return response
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
        )
    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)