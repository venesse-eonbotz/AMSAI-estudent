import time
import cv2
from pyzbar.pyzbar import decode
from models import Student

# cam = cv2.VideoCapture(0)
# cam.set(5, 640)
# cam.set(6, 480)
#
# camera = True
# while camera == True:
#     success, frame = cam.read()
#
#     for i in decode(frame):
#         print(i.type)
#         print(i.data.decode('utf-8'))
#         time.sleep(6)
#
#         cv2.imshow("Date", frame)
#         cv2.waitKey(3)

# query = Student.objects.all()
# value = input()
# student = {"RegisterID": value[12:]}
# print(student)


