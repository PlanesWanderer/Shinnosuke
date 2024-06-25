import azure.cognitiveservices.speech as speechsdk
import time

SPEECH_KEY = "8527e4126d2e466887fc5db1cd9f0486"
SPEECH_REGION = "eastus"


def simple_speech_recognition_test():
    # 创建语音配置
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    speech_config.speech_recognition_language = "zh-CN"

    # 创建音频配置
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    # 创建语音识别器
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("请说些什么...")

    # 进行单次语音识别
    result = speech_recognizer.recognize_once()

    # 处理结果
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"识别结果: {result.text}")
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("无法识别语音")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"语音识别被取消: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"错误详情: {cancellation_details.error_details}")

if __name__ == "__main__":
    simple_speech_recognition_test()