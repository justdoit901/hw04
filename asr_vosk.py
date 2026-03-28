from vosk import Model, KaldiRecognizer
import wave
import json

# 配置路径
MODEL_PATH = "vosk_model_cn"  
AUDIO_PATH = "dub.wav"        

# 加载模型
model = Model(MODEL_PATH)
wf = wave.open(AUDIO_PATH, "rb")
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)

# 识别音频
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    rec.AcceptWaveform(data)

# 输出结果
result = json.loads(rec.FinalResult())
print("识别结果：", result["text"])
