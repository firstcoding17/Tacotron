##녹음 틀고
##녹음 텍스트로 변환
import speech_recognition as sr
import pyaudio
import wave


r = sr.Recognizer()
mic = sr.Microphone()

class Voice:
    def startVoice(void):
        with mic as source:
            audio = r.listen(source)
        return audio


kaudio = r.recognize_google(Voice.startVoice(),language='ko-KR')










