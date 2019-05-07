from jamo import h2j, j2hcj,j2h
import numpy as np


def JAMO_CHO(chosung):
    table = np.array(["_","~","ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"])##0->공백2~20까지 숫자

    return np.where(table == chosung)[0][0]

def JAMO_JUNG(jungsung):
    table = np.array(["ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅙ","ㅚ","ㅛ","ㅜ","ㅝ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"])

    return np.where(table==jungsung)[0][0]

def JAMO_JONG(jongsung):
    table = np.array(["","ㄱ","ㄲ","ㄳ","ㄴ","ㄵ","ㄶ","ㄷ","ㄹ","ㄺ","ㄻ","ㄽ","ㄾ","ㄿ","ㅁ","ㅂ","ㅄ","ㅅ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"])

    return np.where(table==jongsung)[0][0]
def Special_Characters(specialChar):
    table = np.array(["!","(",")",",","-",".",":",";","?","''"," "])

    return np.where(table==specialChar)