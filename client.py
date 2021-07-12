import grpc
import cv2
import base64
import numpy as np
from protobufs.fallalert_pb2 import FallAlarmRequest
from protobufs.fallalert_pb2_grpc import FallAlarmServiceStub

# make an RPC request
channel = grpc.insecure_channel("10.60.108.95:8005")
# channel = grpc.insecure_channel("localhost:8005")

client = FallAlarmServiceStub(channel)

request = FallAlarmRequest(ws="./50waystofall.mp4", gpu="cpu", get_image=True)
results = client.Alarm(request)
for result in results:
    np_array = np.frombuffer(base64.b64decode(result.image_bytes), np.uint8)
    if len(np_array) > 1:
        img_matrix = np_array.reshape(360, 640, 3)
        # cv2.imshow("Output", img_matrix)
        # if cv2.waitKey(1) == 27:
        #     break
    if result.alarm:
        print(result.alarm)
        print(result.timestamp)


