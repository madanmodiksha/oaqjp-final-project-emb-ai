import emotion_detection
import unittest

class TestEmotionAnalyser(unittest.TestCase):
     def test_emotion_analyzer(self):
        res = emotion_detection.emotion_detector("I am glad this happened")
        self.assertEqual(res[0]['dominant_emotion'], 'joy')

        res = emotion_detection.emotion_detector("I am really mad about this")
        self.assertEqual(res[0]['dominant_emotion'], 'anger')

        res = emotion_detection.emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(res[0]['dominant_emotion'], 'disgust')

        res = emotion_detection.emotion_detector("I am so sad about this")
        self.assertEqual(res[0]['dominant_emotion'], 'sadness')

        res = emotion_detection.emotion_detector("I am really afraid that this will happen	")
        self.assertEqual(res[0]['dominant_emotion'], 'fear')
        
unittest.main()