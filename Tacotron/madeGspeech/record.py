import pyaudio
import wave
import time


RATE = 48000
CHANNELS = 2
#
FORMAT = pyaudio.paInt16
DEVICE_INDEX = 2

CHUNK = 1024
SAMPLING_PER_SEC = RATE // CHUNK
RECORD_SEC = 5

pa = pyaudio.PyAudio()

try:
    if pa.is_format_supported(RATE, input_device=DEVICE_INDEX, input_channels=CHANNELS, input_format=FORMAT):
        # input stream 객체
        stream = pa.open(rate=RATE, channels=CHANNELS, format=FORMAT, input=True,
                        input_device_index=DEVICE_INDEX, frames_per_buffer=CHUNK, start=False)
    else:
        print("지원하지 않는 형식입니다.")
        pa.terminate()
        exit()

except:
    print("샘플링 속도 또는 장치 설정 문제입니다.")
    pa.terminate()
    exit()

frames=[]

stream.start_stream()
print("녹음 시작")
start_t = time.time()

try:
    # 최대 버퍼 크기의 1/2 만 읽어들이기 때문에 반복은 2 배로 해야한다
    for i in range(int(SAMPLING_PER_SEC*RECORD_SEC*2)):
        # 기본적으로 little endian으로 데이터가 출력 된다
        string_data = stream.read(CHUNK//2, exception_on_overflow=True)
        frames.append(string_data)

except IOError as e:
    print("오버 플로우")
    stream.close()
    pa.terminate()
    exit()

print("녹음 시간",time.time()-start_t)
print("녹음 종료")

stream.stop_stream()
stream.close()
pa.terminate()

now = time.localtime()
w = wave.open("record_"+str(now.tm_min)+'_'+str(now.tm_sec)+'.wav', 'wb')
w.setnchannels(CHANNELS)
w.setsampwidth(pa.get_sample_size(FORMAT))
w.setframerate(RATE)
w.writeframes(b''.join(frames))
w.close()