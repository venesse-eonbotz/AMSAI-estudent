# # Install Courier SDK: pip install trycourier
# from trycourier import Courier
#
# client = Courier(auth_token="pk_prod_NF8JH9JFRPMNNDQRWR45VTF023B1")
#
# resp = client.send_message(
#     message={
#       "to": {
#         "email": "nanatutee@gmail.com"
#       },
#       "content": {
#         "title": "Welcome to Courier!",
#         "body": "Want to hear a joke? {{joke}}"
#       },
#       "data":{
#         "joke": "Why does Python live on land? Because it is above C level"
#       }
#     }
# )
import random, string

random_no = ''.join(random.choices(string.digits, k=6))
code = f"{random_no}"
print(code)
print(random_no)