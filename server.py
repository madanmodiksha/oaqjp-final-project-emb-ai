'''this file is to run the server side of execution'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Dectector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' this function is used to send string message for
    emotion analysis  
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response[1] == 200:
        return response[0]
    return "Invalid text! Please try again!."

@app.route("/")
def render_index_page():
    ''' this function is used to render the template'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
