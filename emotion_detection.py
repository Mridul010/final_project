import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    my_obj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=my_obj)
    if response.status_code == 200:
        result = response.json()
        
        emotions = result["emotionPredictions"][0]["emotion"]
        
        anger = emotions.get("anger", 0)
        disgust = emotions.get("disgust", 0)
        fear = emotions.get("fear", 0)
        joy = emotions.get("joy", 0)
        sadness = emotions.get("sadness", 0)
        
        emotions_dict = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness
        }
        dominant_emotion = max(emotions_dict, key=emotions_dict.get)
        dominant_score = emotions_dict[dominant_emotion]

        if dominant_emotion == "joy" and dominant_score > 0.5:
            sentiment = "Positive"
        elif dominant_emotion in ["anger", "disgust", "fear", "sadness"] and dominant_score > 0.5:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return {
            "label": sentiment,
            "score": round(dominant_score, 3)
        }
    else:
        return {"label": "Error", "score": 0}