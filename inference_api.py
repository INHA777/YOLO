# import the inference-sdk
from inference_sdk import InferenceHTTPClient

# initialize the client
CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="JdV8057SQM8Mx47K63BM"
)

# infer on a local image
result = CLIENT.infer("frame_00622.jpg", model_id="occupied-or-empty/1")
print(result)





