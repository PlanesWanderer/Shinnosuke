import requests
import azure.cognitiveservices.speech as speechsdk

SPEECH_KEY = "8527e4126d2e466887fc5db1cd9f0486"
SPEECH_REGION = "eastus"

def test_azure_connection():
    try:
        response = requests.get(f'https://{SPEECH_REGION}.api.cognitive.microsoft.com/sts/v1.0/issueToken', 
                                headers={'Ocp-Apim-Subscription-Key': SPEECH_KEY})
        if response.status_code == 200:
            print("成功连接到 Azure 服务")
        else:
            print(f"连接失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"连接错误: {str(e)}")

if __name__ == "__main__":
    test_azure_connection()