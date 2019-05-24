##1 STT
##2 글자 초성 중성 종성으로 쪼개기 리스트로 띄어쓰기 구분
##3 글자를 숫자로 변환 -> 딕셔너리 이용 string 형으로 강제 형변화 예) "ㄱ" : 0.3 그래서 hungul파일에 딕셔너리로 구분
##특수기호 !,?,~는 문장이 끝날 때 음성 볼륨 파악
##시작함수적으면 글자 초성중성분리
import speech_recognition as sr
import time
from datetime import datetime, timedelta
import hgtk
from madeGspeech import hungul as Token


##소리받기
def start():
    r = sr.Recognizer()
    mic = sr.Microphone()
    ST = time.time()

    with mic as source:
        audio = r.listen(source)
        ET = time.time()
        if ET - ST >=6:
            return print("limit 6sec")
        return r.recognize_google(audio,language='ko-KR')
##형변환
class SWAP:

    def list(some):
        return list(some)
    def tuple(some):
        return tuple(some)
    def String(some):
        return str(some)
##문자 쪼개기 만약 띄어쓰기면 ' '출력
def slice(some):

    for i in range(0,len(some)):
        if some[i] == ' ':
            a = ' '
        else: a = hgtk.letter.decompose(some[i])
    return a##문자 하나씩 쪼게서 리스트형테로 저장하길 바람 다른 자료형도 가능

def compareWithHun(some):
    a=[]
    for i in range(0,len(some)):
        if Token.HungulMoum[some[i]] >= 0:
            a+=Token.HungulMoum[some[i]]
        else: a+=Token.HungulJuaum[some[i]]
    return a
##데이터 수치화














