import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    # print(response)
    if response.status_code == 200:
        format_response = json.loads(response.text)
        max_value = 0
        data = {}
        for emotion in format_response['emotionPredictions'][0]['emotion']:
            data[emotion] = format_response['emotionPredictions'][0]['emotion'][emotion]
            if(format_response['emotionPredictions'][0]['emotion'][emotion]>max_value):
                max_emotion = emotion
                max_value = format_response['emotionPredictions'][0]['emotion'][emotion]
        data["dominant_emotion"] = max_emotion
    else:
        data = {"anger": 0.00, "disgust": 0.00, "fear": 0.00, "joy": 0.00, "sadness": 0.00, "dominant_emotion":"None"}
    return data, response.status_code